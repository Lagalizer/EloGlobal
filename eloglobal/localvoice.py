"""Voices that run on this PC: Piper and Kokoro neural voices, and the voices built into Windows.

Nothing here talks to an online service. Voice files are downloaded once (or shipped with the app) and then run
with ONNX Runtime; the Windows voices come with Windows.

Text -> phonemes: Piper and Kokoro voices were trained on the phonemes of eSpeak NG. eSpeak NG is GPL-3.0, so it is
shipped *unchanged, as its own program* (engines\\espeak-ng\\espeak-ng.exe, with its source code) and only talked
to through a pipe: text in, IPA phonemes out. None of its code is loaded into the app (EloGlobal has its own licence).
The Piper and Kokoro runners below are our own code (they follow the published model formats); no GPL Python
package (piper-tts 1.3+, phonemizer, espeakng-loader) is used.

Only voices whose licence allows commercial use are in the catalogue: voices trained from scratch on public-domain,
CC0 or CC-BY data. Many Piper voices are fine-tuned from the "lessac" voice (Blizzard 2013 data: non-commercial)
or from "ryan" (CC-BY-NC-SA); those are left out on purpose.

Voice ids: "piper:<file>[#speaker]", "kokoro:<voice>", "windows:<voice name>".
"""
from __future__ import annotations

import json
import logging
import os
import queue
import re
import subprocess
import threading
import unicodedata
from dataclasses import dataclass
from pathlib import Path

import numpy as np

from . import languages as L
from .config import BUNDLED_MODELS_DIR, ENGINES_DIR, MODELS_DIR

log = logging.getLogger("eloglobal.voice")

PIPER, KOKORO, WINDOWS = "piper", "kokoro", "windows"
PIPER_URL = "https://huggingface.co/rhasspy/piper-voices/resolve/main"
KOKORO_URL = "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0"
KOKORO_MODEL = "kokoro-v1.0.onnx"           # fp32: the int8 file is 3x slower on CPUs
KOKORO_VOICES = "voices-v1.0.bin"


class VoiceError(Exception):
    pass


# --------------------------------------------------------------------------------------------------- catalogue
@dataclass(frozen=True)
class Voice:
    id: str
    engine: str
    lang: str                     # our language code
    name: str
    gender: str                   # female | male
    licence: str = ""
    credit: str = ""
    files: tuple = ()             # ((url, file name, bytes), ...) - downloaded into MODELS_DIR/<engine>

    @property
    def size_mb(self) -> int:
        return int(sum(f[2] for f in self.files) / 1e6 + 0.5)

    def label(self) -> str:
        eng = {PIPER: "Piper", KOKORO: "Kokoro", WINDOWS: "Windows"}[self.engine]
        return f"{self.name} - {L.name(self.lang)}, {self.gender} ({eng})"


def _piper(file: str, lang: str, name: str, gender: str, size: int, licence: str, credit: str,
           speaker: int | None = None) -> Voice:
    loc, spk, quality = file.split("-")
    base = f"{PIPER_URL}/{loc.split('_')[0]}/{loc}/{spk}/{quality}/{file}"
    vid = f"{PIPER}:{file}" + (f"#{speaker}" if speaker is not None else "")
    return Voice(vid, PIPER, lang, name, gender, licence, credit,
                 ((f"{base}.onnx", f"{file}.onnx", size), (f"{base}.onnx.json", f"{file}.onnx.json", 10_000)))


_KOKORO_FILES = ((f"{KOKORO_URL}/{KOKORO_MODEL}", KOKORO_MODEL, 325_532_387),
                 (f"{KOKORO_URL}/{KOKORO_VOICES}", KOKORO_VOICES, 28_214_398))
_KOKORO_LICENCE = "Apache-2.0"
_KOKORO_CREDIT = "Kokoro-82M by hexgrad (huggingface.co/hexgrad/Kokoro-82M), ONNX export by thewh1teagle"


def _kokoro(voice: str, lang: str, name: str, gender: str) -> Voice:
    return Voice(f"{KOKORO}:{voice}", KOKORO, lang, name, gender, _KOKORO_LICENCE, _KOKORO_CREDIT, _KOKORO_FILES)


_LIBRIVOX = "Bryce Beattie (brycebeattie.com/files/tts), recordings from LibriVox (public domain)"
_MLS = "Multilingual LibriSpeech (openslr.org/94, CC-BY 4.0), Piper voice by the Rhasspy / OHF-Voice project"
_SERENA = ("serena-synthetic-it-27h (huggingface.co/datasets/committa/serena-synthetic-it-27h, CC-BY 4.0, made with "
           "Qwen3-TTS), Piper voice by the OHF-Voice project")
_CARLFM = "my-speech-datasets by carlfm01 (github.com/carlfm01/my-speech-datasets, public domain), Piper voice"
_UK = "ukrainian_tts dataset (github.com/OHF-Voice/voice-datasets, CC0), Piper voice by the OHF-Voice project"
CATALOGUE: list[Voice] = [
    _piper("en_US-kristin-medium", "en", "Kristin", "female", 63_531_379, "Public domain", _LIBRIVOX),
    _piper("en_US-norman-medium", "en", "Norman", "male", 63_531_379, "Public domain", _LIBRIVOX),
    _piper("en_US-john-medium", "en", "John", "male", 63_531_379, "Public domain", _LIBRIVOX),
    _piper("en_GB-cori-medium", "en-GB", "Cori", "female", 63_531_379, "Public domain", _LIBRIVOX),
    # MLS voices have hundreds of speakers: these were picked by intelligibility (Whisper word error rate) and pitch
    _piper("de_DE-mls-medium", "de", "MLS 12", "female", 76_961_079, "CC-BY-4.0", _MLS, 12),
    _piper("de_DE-mls-medium", "de", "MLS 25", "male", 76_961_079, "CC-BY-4.0", _MLS, 25),
    _piper("fr_FR-mls-medium", "fr", "MLS 29", "female", 76_733_750, "CC-BY-4.0", _MLS, 29),
    _piper("fr_FR-mls-medium", "fr", "MLS 46", "male", 76_733_750, "CC-BY-4.0", _MLS, 46),
    _piper("es_ES-carlfm-x_low", "es", "Carlfm", "male", 28_130_791, "Public domain", _CARLFM),
    _piper("it_IT-serena-medium", "it", "Serena", "female", 63_516_051, "CC-BY-4.0", _SERENA),
    _piper("uk_UA-ukrainian_tts-medium", "uk", "Lada", "female", 76_735_663, "CC0-1.0", _UK, 0),
    _piper("uk_UA-ukrainian_tts-medium", "uk", "Mykyta", "male", 76_735_663, "CC0-1.0", _UK, 1),
    _piper("uk_UA-ukrainian_tts-medium", "uk", "Tetiana", "female", 76_735_663, "CC0-1.0", _UK, 2),
    _kokoro("af_heart", "en", "Heart", "female"),
    _kokoro("am_michael", "en", "Michael", "male"),
    _kokoro("bf_emma", "en-GB", "Emma", "female"),
    _kokoro("bm_george", "en-GB", "George", "male"),
    _kokoro("pf_dora", "pt", "Dora", "female"),
    _kokoro("pm_alex", "pt", "Alex", "male"),
    _kokoro("ef_dora", "es", "Dora", "female"),
    _kokoro("em_alex", "es", "Alex", "male"),
    _kokoro("ff_siwis", "fr", "Siwis", "female"),
    _kokoro("if_sara", "it", "Sara", "female"),
    _kokoro("im_nicola", "it", "Nicola", "male"),
    _kokoro("hf_alpha", "hi", "Alpha", "female"),
    _kokoro("hm_omega", "hi", "Omega", "male"),
]
BY_ID = {v.id: v for v in CATALOGUE}

# The voice "auto" means, per language: (female, male). Fast Piper voices first. Languages without a fast voice of
# the catalogue use a Windows voice of that language, then Kokoro (natural, but slower than real time on many CPUs).
DEFAULTS = {
    "en": ("piper:en_US-kristin-medium", "piper:en_US-norman-medium"),
    "en-GB": ("piper:en_GB-cori-medium", ""),
    "de": ("piper:de_DE-mls-medium#12", "piper:de_DE-mls-medium#25"),
    "fr": ("piper:fr_FR-mls-medium#29", "piper:fr_FR-mls-medium#46"),
    "it": ("piper:it_IT-serena-medium", ""),
    "uk": ("piper:uk_UA-ukrainian_tts-medium#0", "piper:uk_UA-ukrainian_tts-medium#1"),
}
# fast but plainer voices, used before Kokoro when Windows has no voice for the language
FAST_FALLBACK = {
    "es": ("piper:es_ES-carlfm-x_low", "piper:es_ES-carlfm-x_low"),
    "es-MX": ("piper:es_ES-carlfm-x_low", "piper:es_ES-carlfm-x_low"),
}
KOKORO_FALLBACK = {
    "en-GB": ("kokoro:bf_emma", "kokoro:bm_george"),
    "pt": ("kokoro:pf_dora", "kokoro:pm_alex"),
    "es": ("kokoro:ef_dora", "kokoro:em_alex"),
    "fr": ("kokoro:ff_siwis", "kokoro:ff_siwis"),
    "it": ("kokoro:if_sara", "kokoro:im_nicola"),
    "hi": ("kokoro:hf_alpha", "kokoro:hm_omega"),
}
_KOKORO_ESPEAK = {"en": "en-us", "en-GB": "en-gb", "pt": "pt-br", "pt-PT": "pt-br", "es": "es", "es-MX": "es",
                  "fr": "fr-fr", "it": "it", "hi": "hi"}


def _search_dirs(engine: str) -> list[Path]:
    return [MODELS_DIR / engine, BUNDLED_MODELS_DIR / engine]


def find_file(engine: str, name: str) -> Path | None:
    for d in _search_dirs(engine):
        p = d / name
        if p.is_file():
            return p
    return None


def installed(v: Voice) -> bool:
    return v.engine == WINDOWS or all(find_file(v.engine, f[1]) for f in v.files)


_download_lock = threading.Lock()


def download(v: Voice, progress=None, cancelled=lambda: False) -> None:
    """Fetch the files of `v` into MODELS_DIR (once). progress(done_bytes, total_bytes).
    One download at a time: the voice threads, the warm-up and the Voice tab can ask for the same voice at once, and
    two downloads writing the same file would leave a broken voice that counts as installed."""
    from .downloads import fetch
    with _download_lock:
        todo = [f for f in v.files if not find_file(v.engine, f[1])]     # again: another thread may have got it
        total, done = sum(f[2] for f in todo), 0
        for url, name, _size in todo:
            def prog(d, _t, base=done):
                if progress:
                    progress(base + d, total)
            fetch(url, MODELS_DIR / v.engine / name, prog, cancelled)
            done += _size


def voices_for(lang: str | None) -> list[Voice]:
    """Catalogue voices + installed Windows voices for a language (all languages when lang is None)."""
    out = [v for v in CATALOGUE if lang is None or L.base(v.lang) == L.base(lang)]
    out += [v for v in windows_voices() if lang is None or L.base(v.lang) == L.base(lang)]
    return out


def default_voice(lang: str, gender: str = "female") -> Voice | None:
    """The voice "auto" means for this language and gender (see DEFAULTS)."""
    i = 1 if gender == "male" else 0
    pair = DEFAULTS.get(lang) or DEFAULTS.get(L.base(lang))
    if pair and pair[i]:
        return BY_ID[pair[i]]
    wins = [v for v in windows_voices() if L.base(v.lang) == L.base(lang)]

    def gendered(vs):
        return ([v for v in vs if v.gender == gender] or vs)[:1]

    picks = gendered([v for v in wins if v.lang == lang])              # a Windows voice of this exact language
    for table in (FAST_FALLBACK, KOKORO_FALLBACK):                    # our voices of this exact language
        pair = table.get(lang)
        if not picks and pair:
            picks = [BY_ID[pair[i]]]
    picks = picks or gendered(wins)                                   # a Windows voice of a related variant
    for table in (FAST_FALLBACK, KOKORO_FALLBACK):
        pair = table.get(L.base(lang))
        if not picks and pair:
            picks = [BY_ID[pair[i]]]
    if picks:
        return picks[0]
    pair = DEFAULTS.get(lang) or DEFAULTS.get(L.base(lang))         # the other gender of a fast voice
    return BY_ID[pair[1 - i]] if pair and pair[1 - i] else None


def get(voice_id: str) -> Voice | None:
    if voice_id in BY_ID:
        return BY_ID[voice_id]
    if voice_id.startswith(WINDOWS + ":"):
        return next((v for v in windows_voices() if v.id == voice_id), None)
    if voice_id.startswith(PIPER + ":"):                 # a Piper voice the user put in the models folder
        name, _, spk = voice_id[len(PIPER) + 1:].partition("#")
        if find_file(PIPER, f"{name}.onnx"):
            lang = L.normalize(name.split("-")[0].replace("_", "-")) or "en"
            return Voice(voice_id, PIPER, lang, name, "female", "see the voice's MODEL_CARD", "")
    return None


# --------------------------------------------------------------------------------------------------- eSpeak NG
def espeak_dir() -> Path | None:
    for d in (ENGINES_DIR / "espeak-ng", Path(os.environ.get("ELOGLOBAL_ESPEAK", "")) if
              os.environ.get("ELOGLOBAL_ESPEAK") else None):
        if d and (d / "espeak-ng.exe").is_file() and (d / "espeak-ng-data").is_dir():
            return d
    return None


_CLAUSE = re.compile(r"[^.,;:!?…。！？]+[.,;:!?…。！？]*")
_FLAGS = re.compile(r"\([a-z-]+\)")                     # "(en)" language switch marks in espeak's output


def clauses(text: str) -> list[tuple[str, str]]:
    """'Hi, how are you?' -> [('Hi', ','), ('how are you', '?')]"""
    out = []
    for m in _CLAUSE.finditer(" ".join(text.split())):
        part = m.group(0).strip()
        words = part.rstrip(".,;:!?…。！？").strip()
        punct = part[len(words):].strip()[:1].replace("…", ".").replace("。", ".").replace("！", "!") \
            .replace("？", "?")
        if words:
            out.append((words, punct))
    return out


class Espeak:
    """One running espeak-ng.exe per voice language. A line of text in, one line of IPA per clause out.

    After each request a sentinel line is sent; its phonemes (learned at start) mark the end of the answer, so the
    program can stay running between sentences (starting it costs ~0.1 s). The sentinel is a made-up word: with a
    real one ("1.") a sentence saying it ("One.", a numbered list) ended the answer early and every later sentence
    got the phonemes of the one before."""

    SENTINEL = "Qxzvjk."

    _instances: dict[str, "Espeak"] = {}
    _ilock = threading.Lock()

    @classmethod
    def for_voice(cls, voice: str) -> "Espeak":
        with cls._ilock:
            inst = cls._instances.get(voice)
            if inst is None:
                inst = cls._instances[voice] = Espeak(voice)
            return inst

    def __init__(self, voice: str):
        self.voice = voice
        self._lock = threading.Lock()
        self._proc = None
        self._q: queue.Queue = queue.Queue()
        self._sentinel = None

    def _start(self):
        d = espeak_dir()
        if d is None:
            raise VoiceError("eSpeak NG is missing (engines\\espeak-ng) - reinstall EloGlobal.")
        flags = 0x08000000 if os.name == "nt" else 0          # CREATE_NO_WINDOW
        self._proc = subprocess.Popen([str(d / "espeak-ng.exe"), f"--path={d}", "-q", "--ipa", "-v", self.voice],
                                      stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                                      bufsize=0, creationflags=flags)
        self._q = queue.Queue()
        q, out = self._q, self._proc.stdout

        def reader():
            for line in iter(out.readline, b""):
                q.put(line.decode("utf-8", "replace").strip())
            q.put(None)
        threading.Thread(target=reader, name=f"espeak-{self.voice}", daemon=True).start()
        self._write(self.SENTINEL)
        self._sentinel = self._read_line(10.0)

    def _write(self, line: str):
        self._proc.stdin.write((line.replace("\n", " ") + "\n").encode("utf-8"))
        self._proc.stdin.flush()

    def _read_line(self, timeout: float) -> str:
        line = self._q.get(timeout=timeout)
        if line is None:
            raise VoiceError("eSpeak NG stopped")
        return line

    def phonemes(self, parts: list[str]) -> list[str]:
        """IPA for each text in `parts` (each one clause, ending with its punctuation)."""
        with self._lock:
            for attempt in (1, 2):
                try:
                    if self._proc is None or self._proc.poll() is not None:
                        self._start()
                    for p in parts:
                        self._write(p)
                    self._write(self.SENTINEL)
                    lines = []
                    while True:
                        line = self._read_line(10.0)
                        if line == self._sentinel:
                            break
                        if line:
                            lines.append(_FLAGS.sub("", line).strip())
                    return lines
                except (OSError, queue.Empty, VoiceError) as e:
                    log.warning("espeak (%s) failed, restarting: %s", self.voice, e)
                    self.close()
                    if attempt == 2:
                        raise VoiceError(f"eSpeak NG could not read the text: {e}") from e
        return []

    def close(self):
        if self._proc is not None:
            try:
                self._proc.kill()
            except OSError:
                pass
            self._proc = None


def phonemize(text: str, voice: str) -> list[str]:
    """Text -> one IPA string per sentence, with the clause punctuation kept ("həlˈoʊ, wˈɜːld!")."""
    cl = clauses(text)
    if not cl:
        return []
    lines = Espeak.for_voice(voice).phonemes([w + (p if p else ".") for w, p in cl])
    if len(lines) != len(cl):                           # espeak split a clause differently: keep the words, lose
        return [" ".join(lines)] if lines else []       # some pauses
    sentences, cur = [], []
    for (_w, p), ph in zip(cl, lines):
        cur.append(ph + (p if p else ""))
        if p in (".", "!", "?", ""):
            sentences.append(" ".join(cur))
            cur = []
    if cur:
        sentences.append(" ".join(cur))
    return sentences


# --------------------------------------------------------------------------------------------------- ONNX runner
def _session(path: Path):
    import onnxruntime as ort
    so = ort.SessionOptions()
    so.intra_op_num_threads = int(os.environ.get("ELOGLOBAL_ORT_THREADS") or max(1, min(8, (os.cpu_count() or 4) // 2)))
    so.inter_op_num_threads = 1
    so.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL
    return ort.InferenceSession(str(path), sess_options=so, providers=["CPUExecutionProvider"])


class PiperModel:
    """A Piper .onnx voice + its .onnx.json (phoneme ids, sample rate, speakers)."""

    _cache: dict[str, "PiperModel"] = {}
    _lock = threading.Lock()

    @classmethod
    def load(cls, name: str) -> "PiperModel":
        with cls._lock:
            m = cls._cache.get(name)
            if m is None:
                onnx = find_file(PIPER, f"{name}.onnx")
                cfg = find_file(PIPER, f"{name}.onnx.json")
                if not onnx or not cfg:
                    raise VoiceError(f"The voice {name} is not downloaded yet.")
                m = cls._cache[name] = PiperModel(onnx, json.loads(cfg.read_text(encoding="utf-8")))
            return m

    def __init__(self, onnx: Path, cfg: dict):
        self.cfg = cfg
        self.sr = int(cfg["audio"]["sample_rate"])
        self.ids = cfg["phoneme_id_map"]
        self.text_phonemes = cfg.get("phoneme_type") == "text"
        self.espeak_voice = (cfg.get("espeak") or {}).get("voice", "en-us")
        inf = cfg.get("inference") or {}
        self.noise, self.length, self.noise_w = (float(inf.get("noise_scale", 0.667)),
                                                 float(inf.get("length_scale", 1.0)), float(inf.get("noise_w", 0.8)))
        self.multi = int(cfg.get("num_speakers", 1)) > 1
        self.sess = _session(onnx)

    def _sentences(self, text: str) -> list[str]:
        if not self.text_phonemes:
            return phonemize(text, self.espeak_voice)
        out, cur = [], []
        for words, p in clauses(text):
            cur.append(unicodedata.normalize("NFD", words.lower()) + p)
            if p in (".", "!", "?", ""):
                out.append(" ".join(cur))
                cur = []
        return out + ([" ".join(cur)] if cur else [])

    def _ids(self, phonemes: str) -> list[int]:
        pad = self.ids.get("_", [0])
        ids = list(self.ids.get("^", [1])) + list(pad)
        for ch in unicodedata.normalize("NFD", phonemes):
            if ch in self.ids:
                ids += self.ids[ch] + pad
        return ids + list(self.ids.get("$", [2]))

    def synthesize(self, text: str, speaker: int | None = None, speed: float = 1.0, on_audio=None) -> np.ndarray:
        """All sentences of `text`; on_audio(sentence audio) is called as each one is ready (streaming)."""
        parts = []
        gap = np.zeros(int(self.sr * 0.12), dtype=np.float32)
        for ph in self._sentences(text):
            ids = self._ids(ph)
            if len(ids) < 4:
                continue
            feeds = {"input": np.array([ids], dtype=np.int64),
                     "input_lengths": np.array([len(ids)], dtype=np.int64),
                     "scales": np.array([self.noise, self.length / max(0.3, speed), self.noise_w], dtype=np.float32)}
            if self.multi:
                feeds["sid"] = np.array([int(speaker or 0)], dtype=np.int64)
            audio = np.clip(np.asarray(self.sess.run(None, feeds)[0], dtype=np.float32).reshape(-1), -1, 1)
            if on_audio:
                on_audio(audio if not parts else np.concatenate([gap, audio]))
            parts += [gap, audio] if parts else [audio]
        return np.concatenate(parts) if parts else np.zeros(0, dtype=np.float32)


class KokoroModel:
    """Kokoro-82M (Apache-2.0) through ONNX Runtime: phoneme tokens + a voice style vector -> 24 kHz audio."""

    SR = 24000
    MAX_TOKENS = 510
    _inst: "KokoroModel | None" = None
    _lock = threading.Lock()

    @classmethod
    def load(cls) -> "KokoroModel":
        with cls._lock:
            if cls._inst is None:
                model, voices = find_file(KOKORO, KOKORO_MODEL), find_file(KOKORO, KOKORO_VOICES)
                if not model or not voices:
                    raise VoiceError("The Kokoro voices are not downloaded yet.")
                cls._inst = KokoroModel(model, voices)
            return cls._inst

    def __init__(self, model: Path, voices: Path):
        from .kokoro_vocab import VOCAB
        self.vocab = VOCAB
        self.voices = np.load(voices)
        self.sess = _session(model)
        names = {i.name: i for i in self.sess.get_inputs()}
        self.tok_name = "input_ids" if "input_ids" in names else "tokens"
        self.speed_int = "int" in (names["speed"].type if "speed" in names else "")

    def _run(self, ph: str, style: np.ndarray, speed: float) -> np.ndarray:
        tokens = [self.vocab[c] for c in ph if c in self.vocab][: self.MAX_TOKENS]
        if not tokens:
            return np.zeros(0, dtype=np.float32)
        feeds = {self.tok_name: np.array([[0, *tokens, 0]], dtype=np.int64),
                 "style": np.asarray(style[min(len(tokens), len(style)) - 1], dtype=np.float32).reshape(1, -1),
                 "speed": np.array([max(1, round(speed)) if self.speed_int else speed],
                                   dtype=np.int32 if self.speed_int else np.float32)}
        return np.asarray(self.sess.run(None, feeds)[0], dtype=np.float32).reshape(-1)

    def synthesize(self, text: str, voice: str, lang: str, speed: float = 1.0, on_audio=None) -> np.ndarray:
        if voice not in self.voices:
            raise VoiceError(f"Kokoro has no voice '{voice}'.")
        style = self.voices[voice]
        esp = _KOKORO_ESPEAK.get(lang) or _KOKORO_ESPEAK.get(L.base(lang))
        if not esp:
            raise VoiceError(f"Kokoro does not speak {L.name(lang)}.")
        parts, gap = [], np.zeros(int(self.SR * 0.1), dtype=np.float32)
        for ph in phonemize(text, esp):
            audio = _trim(self._run(ph, style, max(0.5, min(2.0, speed))), self.SR)
            if not len(audio):
                continue
            if on_audio:
                on_audio(audio if not parts else np.concatenate([gap, audio]))
            parts += [gap, audio] if parts else [audio]
        return np.concatenate(parts) if parts else np.zeros(0, dtype=np.float32)


def _trim(audio: np.ndarray, sr: int, thresh: float = 0.01) -> np.ndarray:
    """Cut the silence a model puts before and after the speech (keeps 40 ms)."""
    idx = np.flatnonzero(np.abs(audio) > thresh)
    if not len(idx):
        return audio[:0]
    keep = int(sr * 0.04)
    return audio[max(0, idx[0] - keep): idx[-1] + keep]


# --------------------------------------------------------------------------------------------------- Windows
_win_cache: list[Voice] | None = None


def windows_voices() -> list[Voice]:
    """The voices installed in Windows (Settings -> Time & language -> Speech). Cached."""
    global _win_cache
    if _win_cache is None:
        out = []
        try:
            from winrt.windows.media.speechsynthesis import SpeechSynthesizer
            for v in SpeechSynthesizer.all_voices:
                name = v.display_name.replace("Microsoft ", "")
                out.append(Voice(f"{WINDOWS}:{v.display_name}", WINDOWS, L.normalize(v.language) or "en", name,
                                 "female" if int(v.gender) == 1 else "male", "Part of Windows", "Microsoft"))
        except Exception as e:  # noqa: BLE001
            log.info("Windows voices not available: %s", e)
        _win_cache = out
    return list(_win_cache)


def windows_synthesize(display_name: str, text: str, speed: float = 1.0) -> tuple[np.ndarray, int]:
    import asyncio

    from winrt.windows.media.speechsynthesis import SpeechSynthesizer
    from winrt.windows.storage.streams import DataReader

    from .audio.utils import decode_audio

    async def run():
        s = SpeechSynthesizer()
        for v in SpeechSynthesizer.all_voices:
            if v.display_name == display_name:
                s.voice = v
                break
        if abs(speed - 1.0) > 0.01:
            s.options.speaking_rate = max(0.5, min(6.0, float(speed)))
        stream = await s.synthesize_text_to_stream_async(text)
        reader = DataReader(stream.get_input_stream_at(0))
        await reader.load_async(stream.size)
        buf = bytearray(stream.size)
        reader.read_bytes(buf)
        return bytes(buf)
    return decode_audio(asyncio.run(run()))


# --------------------------------------------------------------------------------------------------- one entry point
def synthesize(voice_id: str, text: str, lang: str, speed: float = 1.0, on_audio=None) -> tuple[np.ndarray, int]:
    """Speak `text` with a voice of the catalogue / Windows. on_audio(chunk, sr) streams sentence by sentence."""
    v = get(voice_id)
    if v is None:
        raise VoiceError(f"Unknown voice '{voice_id}'.")
    if v.engine == WINDOWS:
        audio, sr = windows_synthesize(voice_id[len(WINDOWS) + 1:], text, speed)
        if on_audio:
            on_audio(audio, sr)
        return audio, sr
    if not installed(v):
        download(v)
    cb = (lambda a: on_audio(a, sr)) if on_audio else None
    if v.engine == PIPER:
        name, _, spk = v.id[len(PIPER) + 1:].partition("#")
        m = PiperModel.load(name)
        sr = m.sr
        return m.synthesize(text, int(spk) if spk else None, speed, cb), sr
    m = KokoroModel.load()
    sr = m.SR
    return m.synthesize(text, v.id[len(KOKORO) + 1:], v.lang if L.base(v.lang) != L.base(lang) else lang, speed,
                        cb), sr


def warm_up(voice_id: str) -> None:
    """Load the voice (and its eSpeak NG) now, so the first sentence starts quickly."""
    try:
        v = get(voice_id)
        if v is not None and installed(v):
            synthesize(voice_id, "Ok.", v.lang)
    except Exception as e:  # noqa: BLE001
        log.info("voice warm-up failed (%s): %s", voice_id, e)

