"""Speech-to-text: Whisper (faster-whisper / CTranslate2) on this PC.

transcribe(audio, language) -> (text, detected_language_code_or_None)
audio is mono float32 at 16 kHz. language is one of our codes or None (= auto).
"""
from __future__ import annotations

import logging
import os
import sys
import types

from .. import languages as L
from ..config import MODELS_DIR
from .base import Field, Provider, ProviderError, register

log = logging.getLogger("eloglobal.stt")
SR = 16000


def _without_pyav():
    """faster-whisper imports PyAV only to decode audio *files*; the app always passes samples. PyAV's wheels carry
    an FFmpeg build with GPL encoders, so PyAV is not shipped: a stand-in module answers that import."""
    if "av" in sys.modules:
        return
    stub = types.ModuleType("av")

    def __getattr__(name):
        raise ImportError("PyAV is not included in EloGlobal: audio files can't be decoded")
    stub.__getattr__ = __getattr__
    sys.modules["av"] = stub


def gpu_count() -> int:
    try:
        import ctranslate2
        return ctranslate2.get_cuda_device_count()
    except Exception:  # noqa: BLE001
        return 0


def gpu_memory_gb() -> float:
    """Memory of the first NVIDIA card (nvidia-smi comes with the driver), 0 when unknown."""
    try:
        import subprocess
        out = subprocess.run(["nvidia-smi", "--query-gpu=memory.total", "--format=csv,noheader,nounits"],
                             capture_output=True, text=True, timeout=5, creationflags=0x08000000)
        return float(out.stdout.split()[0]) / 1024
    except Exception:  # noqa: BLE001
        return 0.0


def auto_model(device: str) -> str:
    """The Whisper size for this PC: a big model on a graphics card, a small one on the processor."""
    if device == "cuda":
        mem = gpu_memory_gb()
        return "large-v3-turbo" if mem == 0 or mem >= 5.5 else "medium" if mem >= 3.5 else "small"
    cores = os.cpu_count() or 4
    return "small" if cores >= 8 else "base"


class STTProvider(Provider):
    kind = "stt"
    supports_auto = True

    def transcribe(self, audio, language: str | None) -> tuple[str, str | None]:
        raise NotImplementedError


@register
class FasterWhisperSTT(STTProvider):
    id = "faster_whisper"
    name = "Whisper (on this PC)"
    description = ("OpenAI's Whisper speech recognition (MIT licence), running on your PC with faster-whisper. "
                   "Uses an NVIDIA graphics card when one is set up, otherwise the processor. 'auto' picks the "
                   "model size for your PC. Each model is downloaded once.")
    requires = ["faster_whisper", "ctranslate2"]
    fields = [
        Field("model", "Model", "combo", "auto",
              options=["auto", "tiny", "base", "small", "medium", "large-v3-turbo", "large-v3", "distil-large-v3"],
              help="auto = picked for this PC. Bigger = more accurate but slower. 'large-v3-turbo' is great on a "
                   "graphics card."),
        Field("device", "Device", "choice", "auto", options=["auto", "cuda", "cpu"]),
        Field("compute_type", "Precision", "choice", "auto",
              options=["auto", "int8", "int8_float16", "float16", "float32"]),
        Field("beam_size", "Beam size", "int", 1, min=1, max=10, help="1 = fastest"),
        Field("cpu_threads", "CPU threads", "int", min(8, max(2, (os.cpu_count() or 4) // 2)), min=1, max=64),
        Field("vad_filter", "Built-in VAD filter", "bool", False),
        Field("initial_prompt", "Hint / vocabulary", "str", "",
              help="Names, game terms etc. to help recognition"),
    ]

    _model = None
    _model_key = None

    def _device(self) -> str:
        device = self.s("device")
        if device == "auto":
            device = "cuda" if gpu_count() > 0 else "cpu"
        return device

    def model_name(self) -> str:
        m = self.s("model") or "auto"
        return auto_model(self._device()) if m == "auto" else m

    def _load(self):
        _without_pyav()
        from faster_whisper import WhisperModel
        device = self._device()
        name = self.model_name()
        key = (name, device, self.s("compute_type"))
        if self._model is not None and self._model_key == key:
            return self._model
        ctype = self.s("compute_type")
        if ctype == "auto":
            ctype = "float16" if device == "cuda" else "int8"
        kw = dict(cpu_threads=int(self.s("cpu_threads", 4)), download_root=str(MODELS_DIR / "whisper"))
        try:
            self._model = WhisperModel(name, device=device, compute_type=ctype, **kw)
        except Exception as e:
            if device == "cuda":  # graphics card libraries missing -> the processor instead of failing
                log.warning("Whisper on the graphics card failed (%s) - using the processor", e)
                if self.s("model") == "auto":
                    name = auto_model("cpu")
                self._model = WhisperModel(name, device="cpu", compute_type="int8", **kw)
            else:
                raise ProviderError(f"Whisper: could not load the model '{name}': {e}") from e
        log.info("Whisper %s on %s", name, device)
        self._model_key = key
        return self._model

    def warmup(self):
        with self.lock:
            self._load()

    def transcribe(self, audio, language):
        with self.lock:
            model = self._load()
            segments, info = model.transcribe(
                audio, language=L.whisper_code(language), beam_size=int(self.s("beam_size", 1)),
                vad_filter=bool(self.s("vad_filter")), condition_on_previous_text=False,
                initial_prompt=self.s("initial_prompt") or None, without_timestamps=True,
            )
            text = " ".join(seg.text.strip() for seg in segments
                            if getattr(seg, "no_speech_prob", 0) < 0.8).strip()
        detected = L.normalize(info.language) if info and info.language else None
        if detected and language is None and getattr(info, "language_probability", 1.0) < 0.4:
            detected = None  # too unsure to trust
        return text, detected or language
