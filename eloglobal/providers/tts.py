"""Text-to-speech: the voices of this PC (Piper, Kokoro and the voices built into Windows) - see localvoice.py.

synthesize(text, lang, voice, gender) -> (mono float32 audio, sample_rate)
voice "auto" (or "") = the default voice of the language (localvoice.default_voice).
list_voices(lang) -> [(voice_id, label)]
"""
from __future__ import annotations

import numpy as np

from .. import languages as L
from .. import localvoice as V
from .base import Provider, ProviderError, register


def _is_auto(voice) -> bool:
    return not voice or str(voice).lower() in ("auto", "default")


class TTSProvider(Provider):
    kind = "tts"
    streams = False           # synthesize_stream() hands out audio while it is still being made

    def synthesize(self, text: str, lang: str, voice: str, gender: str = "female") -> tuple[np.ndarray, int]:
        raise NotImplementedError

    def synthesize_stream(self, text: str, lang: str, voice: str, gender: str, on_audio, speed: float = 1.0):
        """Calls on_audio(mono float32 chunk, sample_rate) as the audio arrives. Only for streams = True providers,
        which also apply `speed` themselves (1 = normal)."""
        on_audio(*self.synthesize(text, lang, voice, gender))

    def list_voices(self, lang: str | None = None) -> list[tuple[str, str]]:
        return []


# Each engine's natural pace, a little quicker than reading speed: translations stay close to live
BASE_SPEED = {V.PIPER: 1.05, V.KOKORO: 1.05, V.WINDOWS: 1.1}


@register
class LocalTTS(TTSProvider):
    id = "local"
    name = "Voices on this PC"
    description = ("Natural Piper and Kokoro voices and the voices built into Windows, all running on your PC. "
                   "'auto' picks a voice for each language; a voice is downloaded once the first time it is used "
                   "(about 60-120 MB). Only voices whose licence allows this use are offered. More Windows voices: "
                   "Windows Settings → Time & language → Speech → Add voices.")
    requires = ["onnxruntime"]
    streams = True
    fields = []

    def pick(self, lang: str, voice: str, gender: str) -> V.Voice:
        v = V.default_voice(lang, gender) if _is_auto(voice) else V.get(voice)
        if v is None and not _is_auto(voice):
            v = V.default_voice(lang, gender)                 # a voice that was removed: fall back to auto
        if v is None:
            raise ProviderError(f"No voice for {L.name(lang)} on this PC. Add a Windows voice for it: Windows "
                                "Settings → Time & language → Speech → Add voices.")
        return v

    def synthesize(self, text, lang, voice, gender="female"):
        v = self.pick(lang, voice, gender)
        try:
            return V.synthesize(v.id, text, lang, speed=BASE_SPEED.get(v.engine, 1.0))
        except V.VoiceError as e:
            raise ProviderError(str(e)) from e

    def synthesize_stream(self, text, lang, voice, gender, on_audio, speed=1.0):
        """Sentence by sentence: the first sentence plays while the next ones are made. Piper and Kokoro apply the
        speed themselves (better than stretching), Windows voices through their own speaking rate."""
        v = self.pick(lang, voice, gender)
        try:
            V.synthesize(v.id, text, lang, speed=speed * BASE_SPEED.get(v.engine, 1.0), on_audio=on_audio)
        except V.VoiceError as e:
            raise ProviderError(str(e)) from e

    def ensure(self, lang: str, voice: str, gender: str, on_status=None) -> None:
        """Download the voice now if it is not on this PC yet."""
        v = self.pick(lang, voice, gender)
        if not V.installed(v):
            if on_status:
                on_status(f"Downloading the voice {v.name} ({L.name(v.lang)}, about {v.size_mb} MB, once)…")
            V.download(v)

    def warmup(self):
        pass

    def list_voices(self, lang=None):
        out = []
        for v in V.voices_for(lang):
            tag = "" if V.installed(v) else f"  ⬇ {v.size_mb} MB"
            out.append((v.id, v.label() + tag))
        return out
