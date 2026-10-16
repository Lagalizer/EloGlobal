"""Translation on this PC: OPUS-MT models (University of Helsinki, CC-BY 4.0) run with CTranslate2.

A model is fetched once from the official OPUS-MT release server (object.pouta.csc.fi - the download links on the
models' pages), converted on this PC to CTranslate2's compact int8 format with CTranslate2's own OPUS-MT converter
(it only needs numpy and PyYAML) and kept in MODELS_DIR/opus-mt/<src>-<tgt>. The original download is deleted.
Text never leaves the PC: translating is a local CTranslate2 call.

Pairs are looked up by ISO 639-3 code (eng-por, rus-eng...). When there is no direct model, the text goes through
English (two models). Each converted model keeps the README and LICENSE of the original (attribution).
"""
from __future__ import annotations

import json
import logging
import os
import re
import shutil
import tempfile
import threading
import time
import urllib.request
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

from . import languages as L
from .config import MODELS_DIR

log = logging.getLogger("eloglobal.opusmt")

SERVER = "https://object.pouta.csc.fi/Tatoeba-MT-models"
DIR = MODELS_DIR / "opus-mt"
INDEX = DIR / "index.json"                       # pair -> chosen release (so a known pair needs no lookup)
_TOKENS = {"pt": ("pob", "por"), "pt-PT": ("por",), "zh": ("cmn_Hans", "zho_Hans", "cmn"),
           "zh-TW": ("cmn_Hant", "zho_Hant", "cmn"), "sr": ("srp_Cyrl", "srp_Latn"), "no": ("nob", "nno")}
_SENT = re.compile(r"(?<=[.!?。！？])\s+")


class OpusError(Exception):
    pass


# The live pipelines, the chat translations (4 at a time) and the "download now" button can all need the same
# missing pair at once: one lock per pair makes them wait for a single download instead of each fetching 280 MB.
_pair_locks: dict[tuple[str, str], threading.RLock] = {}
_locks_guard = threading.Lock()
_index_lock = threading.Lock()


def _pair_lock(src3: str, tgt3: str) -> threading.RLock:
    with _locks_guard:
        return _pair_locks.setdefault((src3, tgt3), threading.RLock())


def pair_dir(src3: str, tgt3: str) -> Path:
    return DIR / f"{src3}-{tgt3}"


def is_ready(src3: str, tgt3: str) -> bool:
    return (pair_dir(src3, tgt3) / "model.bin").is_file()


def _index() -> dict:
    try:
        return json.loads(INDEX.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def _save_index(data: dict) -> None:
    DIR.mkdir(parents=True, exist_ok=True)
    tmp = INDEX.with_name(INDEX.name + ".tmp")
    tmp.write_text(json.dumps(data, indent=1), encoding="utf-8")
    os.replace(tmp, INDEX)


def _list_releases(src3: str, tgt3: str) -> list[tuple[str, int]]:
    """[(object key, bytes)] of the model zips on the release server for this pair."""
    url = f"{SERVER}?prefix={src3}-{tgt3}/&max-keys=500"
    req = urllib.request.Request(url, headers={"User-Agent": "EloGlobal"})
    with urllib.request.urlopen(req, timeout=20) as r:
        root = ET.fromstring(r.read())
    out = []
    for el in root.iter():
        if el.tag.endswith("Contents"):
            key = next((c.text for c in el if c.tag.endswith("Key")), "") or ""
            size = int(next((c.text for c in el if c.tag.endswith("Size")), "0") or 0)
            if key.endswith(".zip") and not key.endswith(".eval.zip"):
                out.append((key, size))
    return out


def _rank(key: str, best: bool) -> tuple:
    """Prefer the base Transformer trained with back-translation (fast, ~75 MB once converted), newest first.
    best=True prefers the big models (better, ~3x slower and bigger)."""
    name = key.split("/", 1)[1]
    big = "transformer-big" in name
    tiny = "tiny" in name
    date = re.findall(r"\d{4}-\d{2}-\d{2}", name)
    kind = 0 if (big and best) else 1 if "+bt" in name and not big and not tiny else 2 if not big and not tiny \
        else 3 if big else 4
    return kind, -int(date[-1].replace("-", "")) if date else 0


def find_release(src3: str, tgt3: str, best: bool = False) -> tuple[str, int] | None:
    idx = _index()
    k = f"{src3}-{tgt3}{'+best' if best else ''}"
    if k in idx:
        return tuple(idx[k]) if idx[k] else None
    try:
        rel = _list_releases(src3, tgt3)
    except Exception as e:  # noqa: BLE001
        raise OpusError(f"Could not reach the OPUS-MT model server to download {src3}->{tgt3}: {e}") from e
    pick = sorted(rel, key=lambda r: _rank(r[0], best))[0] if rel else None
    with _index_lock:                       # several pairs can be looked up at once
        idx = _index()
        idx[k] = list(pick) if pick else None
        _save_index(idx)
    return pick


def route(src: str, tgt: str, best: bool = False) -> list[tuple[str, str]]:
    """The model pairs (iso3) that translate src -> tgt: direct, or through English."""
    s3, t3 = L.iso3(src), L.iso3(tgt)
    if s3 == t3:
        return []
    if is_ready(s3, t3) or find_release(s3, t3, best):
        return [(s3, t3)]
    if "eng" in (s3, t3):
        raise OpusError(f"There is no OPUS-MT model for {L.name(src)} -> {L.name(tgt)}.")
    hops = [(s3, "eng"), ("eng", t3)]
    for a, b in hops:
        if not is_ready(a, b) and not find_release(a, b, best):
            raise OpusError(f"There is no OPUS-MT model for {L.name(src)} -> {L.name(tgt)}.")
    return hops


def download(src3: str, tgt3: str, progress=None, cancelled=lambda: False, best: bool = False) -> Path:
    """Fetch + convert one pair (once). progress(done_bytes, total_bytes) while downloading."""
    out = pair_dir(src3, tgt3)
    with _pair_lock(src3, tgt3):
        if (out / "model.bin").is_file():           # (again) another thread may just have finished it
            return out
        return _download(src3, tgt3, out, progress, cancelled, best)


def _download(src3: str, tgt3: str, out: Path, progress, cancelled, best: bool) -> Path:
    rel = find_release(src3, tgt3, best)
    if not rel:
        raise OpusError(f"There is no OPUS-MT model for {src3} -> {tgt3}.")
    key, _size = rel
    from .downloads import fetch
    DIR.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="opus-", dir=DIR) as tmp:
        tmp = Path(tmp)
        zpath = tmp / "model.zip"
        fetch(f"{SERVER}/{key}", zpath, progress, cancelled)
        src = tmp / "src"
        with zipfile.ZipFile(zpath) as z:
            z.extractall(src)
        zpath.unlink()
        from ctranslate2.converters import OpusMTConverter
        conv = tmp / "ct2"
        OpusMTConverter(str(src)).convert(str(conv), quantization="int8", force=True)
        for name in ("source.spm", "target.spm", "README.md", "LICENSE"):
            if (src / name).is_file():
                shutil.copy2(src / name, conv / name)
        (conv / "info.json").write_text(json.dumps({"source": f"{SERVER}/{key}", "licence": "CC-BY-4.0",
                                                    "converted": time.strftime("%Y-%m-%d")}, indent=1),
                                        encoding="utf-8")
        if out.exists():
            shutil.rmtree(out, ignore_errors=True)
        shutil.move(str(conv), str(out))
    log.info("OPUS-MT model ready: %s-%s (%s)", src3, tgt3, key)
    return out


class _Model:
    def __init__(self, path: Path, device: str):
        import ctranslate2
        import sentencepiece as spm
        threads = max(1, min(4, (os.cpu_count() or 4) // 2))
        self.tr = ctranslate2.Translator(str(path), device=device, compute_type="int8" if device == "cpu" else
                                         "int8_float16", inter_threads=1, intra_threads=threads)
        self.sp_src = spm.SentencePieceProcessor(model_file=str(path / "source.spm"))
        self.sp_tgt = spm.SentencePieceProcessor(model_file=str(path / "target.spm"))
        self.tokens = self._target_tokens(path)
        self.lock = threading.Lock()

    @staticmethod
    def _target_tokens(path: Path) -> set[str]:
        readme = path / "README.md"
        text = readme.read_text(encoding="utf-8", errors="replace") if readme.is_file() else ""
        if "language token is required" not in text:
            return set()
        return set(re.findall(r">>(\w+)<<", text))

    def translate(self, sentences: list[str], tgt: str, beam: int) -> list[str]:
        prefix = []
        if self.tokens:
            want = _TOKENS.get(tgt, ()) + (L.iso3(tgt),)
            tok = next((t for t in want if t in self.tokens), sorted(self.tokens)[0])
            prefix = [f">>{tok}<<"]
        batch = [prefix + self.sp_src.encode(s, out_type=str) for s in sentences]
        with self.lock:
            res = self.tr.translate_batch(batch, beam_size=beam, max_decoding_length=256,
                                          repetition_penalty=1.1)
        return [self.sp_tgt.decode(r.hypotheses[0]) for r in res]


class Translator:
    """Keeps the loaded pair models; translate() downloads what is missing on first use."""

    def __init__(self):
        self._models: dict[tuple[str, str, str], _Model] = {}
        self._lock = threading.Lock()

    def model(self, src3: str, tgt3: str, device: str = "cpu", on_status=None) -> _Model:
        key = (src3, tgt3, device)
        with self._lock:
            m = self._models.get(key)
        if m is not None:
            return m
        with _pair_lock(src3, tgt3):                 # load each model once, even when asked for at the same time
            with self._lock:
                m = self._models.get(key)
            if m is not None:
                return m
            if not is_ready(src3, tgt3):
                if on_status:
                    on_status(f"Downloading the translation model {src3} -> {tgt3} (once, about 280 MB)…")
                download(src3, tgt3)
            try:
                m = _Model(pair_dir(src3, tgt3), device)
            except Exception:  # noqa: BLE001 - e.g. no CUDA libraries: the CPU always works
                if device == "cpu":
                    raise
                m = _Model(pair_dir(src3, tgt3), "cpu")
            with self._lock:
                self._models[key] = m
            return m

    def translate(self, text: str, src: str, tgt: str, device: str = "cpu", beam: int = 2, on_status=None) -> str:
        hops = route(src, tgt)
        if not hops:
            return text
        sentences = [s for s in _SENT.split(" ".join(text.split())) if s]
        if not sentences:
            return text
        for i, (a, b) in enumerate(hops):
            target = tgt if i == len(hops) - 1 else "en"
            sentences = self.model(a, b, device, on_status).translate(sentences, target, beam)
        return " ".join(s.strip() for s in sentences if s.strip())


TRANSLATOR = Translator()
