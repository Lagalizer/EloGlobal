"""NVIDIA graphics card support for Whisper (and OPUS-MT): the CUDA libraries CTranslate2 needs (cuBLAS 12, cuDNN 9).

They are big (about 1 GB) and only useful with an NVIDIA card, so they are not shipped: "Set up the graphics card"
downloads NVIDIA's own Python packages from PyPI (nvidia-cublas-cu12, nvidia-cudnn-cu12 - NVIDIA's licence allows
redistributing these runtime libraries with applications) and keeps only their DLLs in MODELS_DIR/gpu. main.py adds
that folder to the DLL search path at start-up. No pip, so it works in the read-only store installation.
"""
from __future__ import annotations

import json
import shutil
import subprocess
import urllib.request
import zipfile
from pathlib import Path

from .config import MODELS_DIR

GPU_DIR = MODELS_DIR / "gpu"
PACKAGES = [("nvidia-cublas-cu12", "12."), ("nvidia-cudnn-cu12", "9.")]
NEEDED = ("cublas64_12.dll", "cublasLt64_12.dll", "cudnn_ops64_9.dll", "cudnn_cnn64_9.dll")


def nvidia_present() -> bool:
    """An NVIDIA card with its driver (nvidia-smi comes with the driver)."""
    try:
        r = subprocess.run(["nvidia-smi", "-L"], capture_output=True, text=True, timeout=5, creationflags=0x08000000)
        return r.returncode == 0 and "GPU" in r.stdout
    except (OSError, subprocess.SubprocessError):
        return False


def installed() -> bool:
    return all((GPU_DIR / n).is_file() for n in NEEDED)


def _wheel_url(name: str, major: str) -> tuple[str, int, str]:
    """(url, bytes, version) of the newest Windows x64 wheel of `name` whose version starts with `major`."""
    with urllib.request.urlopen(f"https://pypi.org/pypi/{name}/json", timeout=20) as r:
        data = json.loads(r.read())

    def key(v):
        return tuple(int(x) if x.isdigit() else 0 for x in v.split("."))
    for version in sorted((v for v in data["releases"] if v.startswith(major)), key=key, reverse=True):
        for f in data["releases"][version]:
            if f["filename"].endswith("win_amd64.whl") and not f.get("yanked"):
                return f["url"], int(f["size"]), version
    raise RuntimeError(f"No Windows package of {name} {major}x found on PyPI.")


def plan() -> list[tuple[str, int, str]]:
    return [_wheel_url(n, m) for n, m in PACKAGES]


def download(progress=None, cancelled=lambda: False) -> None:
    """Fetch the CUDA libraries into MODELS_DIR/gpu (once). progress(done_bytes, total_bytes)."""
    from .downloads import fetch
    items = plan()
    total, done = sum(s for _u, s, _v in items), 0
    tmp = GPU_DIR.with_name("gpu-download")
    tmp.mkdir(parents=True, exist_ok=True)
    GPU_DIR.mkdir(parents=True, exist_ok=True)
    try:
        for url, size, _version in items:
            whl = tmp / url.rsplit("/", 1)[1]
            fetch(url, whl, (lambda d, _t, base=done: progress and progress(base + d, total)), cancelled)
            done += size
            with zipfile.ZipFile(whl) as z:
                for m in z.namelist():
                    if m.lower().endswith(".dll") and "/bin/" in m.replace("\\", "/"):
                        with z.open(m) as src, open(GPU_DIR / Path(m).name, "wb") as dst:
                            shutil.copyfileobj(src, dst, 1 << 20)
                    elif Path(m).name.upper().startswith("LICENSE"):
                        (GPU_DIR / f"{whl.name.split('-')[0]}-{Path(m).name}").write_bytes(z.read(m))
            whl.unlink()
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    if not installed():
        raise RuntimeError("The NVIDIA libraries were downloaded but some files are missing.")
