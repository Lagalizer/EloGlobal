"""Downloads of model and voice files (once). Only files are fetched - nothing about the user is sent.

fetch() writes to <file>.part and renames it at the end, so a broken download never leaves a half file behind;
it resumes a .part file left by an interrupted download when the server supports it."""
from __future__ import annotations

import urllib.error
import urllib.request
from pathlib import Path

from . import __version__

TIMEOUT = 30
UA = f"EloGlobal/{__version__}"


def fetch(url: str, dst: Path, progress=None, cancelled=lambda: False) -> Path:
    """Download `url` to `dst`. progress(done_bytes, total_bytes). Raises on failure or when cancelled()."""
    dst = Path(dst)
    dst.parent.mkdir(parents=True, exist_ok=True)
    part = dst.with_name(dst.name + ".part")
    have = part.stat().st_size if part.exists() else 0
    headers = {"User-Agent": UA}
    if have:
        headers["Range"] = f"bytes={have}-"
    try:
        resp = urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=TIMEOUT)
    except urllib.error.HTTPError as e:
        if e.code == 416 and have:                         # the .part file is already complete
            part.replace(dst)
            return dst
        raise
    with resp:
        if have and resp.status != 206:                    # no resume: start again
            have = 0
        total = int(resp.headers.get("Content-Length") or 0) + have
        done = have
        with open(part, "ab" if have else "wb") as f:
            while True:
                if cancelled():
                    raise RuntimeError("cancelled")
                block = resp.read(1 << 16)
                if not block:
                    break
                f.write(block)
                done += len(block)
                if progress:
                    progress(done, total)
    if total and done < total:
        raise OSError(f"download incomplete ({done} of {total} bytes): {url}")
    part.replace(dst)
    return dst
