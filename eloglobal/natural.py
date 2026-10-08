"""The narrator of the guided tour and the Manual tab, in the language of the app - always a voice of this PC.

Voices come from localvoice.py: Piper / Kokoro voices (downloaded once, the English one ships with the app) and the
voices built into Windows. Nothing is sent anywhere.

The text is turned into speech piece by piece in a background thread, so the first words start quickly and a new
call cuts the previous reading at once. If a voice fails, `on_error(voice, message)` is called from the worker
thread and nothing is played (the caller picks another voice).

prefetch() synthesises the beginning of a text in advance (the next / previous step of the tour), so pressing Next
starts the voice at once.
"""
from __future__ import annotations

import logging
import queue
import re
import threading

import numpy as np

from . import i18n
from . import localvoice as V

log = logging.getLogger("eloglobal.natural")

_CHUNK = 280                       # characters per piece: long enough to sound natural
_SECOND = 140                      # the second is medium, so synthesis always stays ahead of playback
_FIRST = 60                        # the first piece is short, so the voice starts speaking sooner


def _chunks(text: str) -> list[str]:
    """Sentences grouped into pieces; the first piece is kept short so the first words come out fast."""
    sentences = re.split(r"(?<=[.!?:])\s+", text.strip())
    out, cur = [], ""
    for s in sentences:
        limit = (_FIRST, _SECOND)[len(out)] if len(out) < 2 else _CHUNK         # pieces grow: 60, 140, then 280
        if cur and len(cur) + len(s) + 1 > limit:
            out.append(cur)
            cur = s
        else:
            cur = f"{cur} {s}".strip()
    if cur:
        out.append(cur)
    return out


def speed_of(rate: int) -> float:
    """Speed slider (-6 .. +6) -> speed factor (0.52 .. 1.48)."""
    return max(0.5, min(1.6, 1.0 + rate * 0.08))


def narrator_voice(code: str | None = None) -> V.Voice | None:
    """The voice that reads the guide and the Manual in an app language (female voice of the language)."""
    return V.default_voice(code or i18n.current().code, "female")


def preload() -> None:
    """Load the narrator voice now, in this thread. ONNX Runtime holds Python's lock for the second or two it takes
    to load a voice, which would freeze the window - so main.py does it at start-up, before the window exists."""
    v = narrator_voice()
    if v is None or not V.installed(v):
        return
    if v.engine == V.WINDOWS:                    # no ONNX model to load: warm it up without delaying the start
        threading.Thread(target=V.warm_up, args=(v.id,), daemon=True).start()
    else:
        V.warm_up(v.id)


def _can_play() -> bool:
    try:
        import sounddevice  # noqa: F401
        return True
    except Exception:  # noqa: BLE001
        return False


class NaturalNarrator:
    _cache: dict = {}                                # (voice, rate, piece) -> (audio, sample rate), see prefetch()

    def __init__(self, on_error=None):
        self.on_error = on_error
        self._gen = 0
        self._lock = threading.Lock()
        self.available = _can_play() and bool(self.voices())

    # ------------------------------------------------------------------ voices
    def voices(self) -> list[tuple[str, str]]:
        """[(voice id, label)] for the app language: voices on this PC first, then ones that can be downloaded."""
        code = i18n.current().code
        items = V.voices_for(code)
        items.sort(key=lambda v: (not V.installed(v), v.engine == V.KOKORO, v.label()))
        return [(v.id, v.label() + ("" if V.installed(v) else f"  ⬇ {v.size_mb} MB")) for v in items]

    def default_voice(self) -> str:
        v = narrator_voice()
        return v.id if v else ""

    def warm_up(self, voice: str) -> None:
        """Load the voice in the background (and run it once) so the first reading starts at once."""
        v = V.get(voice)
        if v is None or not V.installed(v):
            return
        threading.Thread(target=V.warm_up, args=(voice,), daemon=True).start()

    def refresh(self) -> None:
        self.available = _can_play() and bool(self.voices())

    def _synth(self, voice: str, rate: int, text: str):
        audio, sr = V.synthesize(voice, text, i18n.current().code, speed=speed_of(rate))
        if not len(audio):
            raise RuntimeError("no audio returned")
        return audio, sr

    def prefetch(self, texts: list[str], voice: str, rate: int = 0) -> None:
        """Synthesise the first piece of each text in the background, so speak() can start it at once."""
        v = V.get(voice)
        if v is None or not V.installed(v):
            return

        def work():
            try:
                for text in texts:
                    pieces = _chunks(text)
                    key = (voice, rate, pieces[0]) if pieces else None
                    if key and key not in self._cache:
                        self._cache[key] = self._synth(voice, rate, pieces[0])
                        while len(self._cache) > 12:
                            self._cache.pop(next(iter(self._cache)))
            except Exception as e:  # noqa: BLE001
                log.info("prefetch failed: %s", e)
        threading.Thread(target=work, daemon=True).start()

    # ------------------------------------------------------------------ speaking
    def speak(self, text: str, voice: str, rate: int = 0) -> None:
        """Say `text` now with `voice` (a localvoice id); `rate` is the speed slider (-6 .. +6). Returns at once."""
        self.stop()
        if not text.strip():
            return
        with self._lock:
            gen = self._gen
        q: queue.Queue = queue.Queue(maxsize=2)       # synthesised audio waiting to be played
        threading.Thread(target=self._produce, args=(gen, _chunks(text), voice, rate, q), daemon=True).start()
        threading.Thread(target=self._play, args=(gen, q), daemon=True).start()

    def stop(self) -> None:
        with self._lock:
            self._gen += 1
        if _can_play():
            try:
                import sounddevice as sd
                sd.stop()
            except Exception:  # noqa: BLE001
                pass

    def _alive(self, gen: int) -> bool:
        return gen == self._gen

    def _produce(self, gen, chunks, voice, rate, q):
        try:
            for t in chunks:
                if not self._alive(gen):
                    return
                cached = self._cache.get((voice, rate, t))
                audio, sr = cached if cached is not None else self._synth(voice, rate, t)
                while self._alive(gen):
                    try:
                        q.put((audio, sr), timeout=0.2)
                        break
                    except queue.Full:
                        pass
        except Exception as e:  # noqa: BLE001
            log.warning("narrator voice %s failed: %s", voice, e)
            if self._alive(gen) and self.on_error:
                self.on_error(voice, str(e))
        finally:
            while self._alive(gen):                       # tell the player there is nothing more
                try:
                    q.put(None, timeout=0.2)
                    break
                except queue.Full:
                    pass

    def _play(self, gen, q):
        import sounddevice as sd
        while self._alive(gen):
            try:
                item = q.get(timeout=0.2)
            except queue.Empty:
                continue
            if item is None:
                return
            audio, sr = item
            try:
                sd.play(np.asarray(audio, dtype=np.float32), sr)
                n = len(audio) / float(sr)
                waited = 0.0
                while waited < n + 0.3 and self._alive(gen):
                    threading.Event().wait(0.05)
                    waited += 0.05
            except Exception as e:  # noqa: BLE001
                log.warning("could not play: %s", e)
                return
