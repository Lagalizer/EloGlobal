"""Updates of the GitHub (zip) edition from the releases of its GitHub repository: Settings -> Updates.

Only the zip from GitHub has an update.json next to main.py ({"repo": "owner/name"}); the Microsoft Store and Steam
builds don't, and are updated by their store. Nothing about the user is sent: the app asks GitHub for the newest
release and downloads its zip, like a browser would.

download() saves the release zip in the data folder and unpacks it there; install_on_exit() starts a small script
that waits until EloGlobal has closed, copies the new app folder over this one (user data, downloaded models and
portable.txt are never touched), and starts EloGlobal again.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import urllib.request
import zipfile
from dataclasses import dataclass
from pathlib import Path

from . import __version__
from .config import DATA_DIR, PACKAGE_FAMILY, ROOT
from .downloads import UA, fetch

UPDATE_FILE = ROOT / "update.json"
ASSET = re.compile(r"EloGlobal-.*-windows-x64\.zip$", re.I)
STAGE = DATA_DIR / "update"
TIMEOUT = 30


@dataclass
class Release:
    tag: str
    version: tuple
    notes: str
    asset_url: str
    asset_name: str
    size: int
    newer: bool
    sha256: str = ""         # from GitHub's asset digest ("sha256:…"); empty for releases made before GitHub had it


def repo() -> str:
    """owner/name of the GitHub repository this copy updates from ("" = updates come from a store)."""
    if PACKAGE_FAMILY:
        return ""
    try:
        r = json.loads(UPDATE_FILE.read_text(encoding="utf-8")).get("repo", "")
    except (OSError, ValueError):
        return ""
    return r if re.fullmatch(r"[\w.-]+/[\w.-]+", r or "") else ""


def parse_version(text: str) -> tuple:
    m = re.search(r"(\d+)\.(\d+)(?:\.(\d+))?", text or "")
    return tuple(int(x or 0) for x in m.groups()) if m else ()


def check() -> Release:
    name = repo()
    if not name:
        raise RuntimeError("This copy is updated by its store.")
    req = urllib.request.Request(f"https://api.github.com/repos/{name}/releases/latest",
                                 headers={"User-Agent": UA, "Accept": "application/vnd.github+json"})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        data = json.loads(r.read().decode("utf-8"))
    tag = data.get("tag_name") or ""
    asset = next((a for a in data.get("assets") or [] if ASSET.search(a.get("name", ""))), None)
    if asset is None:
        raise RuntimeError(f"The release {tag} has no Windows zip yet - try again later.")
    version = parse_version(tag)
    digest = asset.get("digest") or ""
    sha256 = digest[7:].lower() if digest.lower().startswith("sha256:") else ""
    return Release(tag, version, data.get("body") or "", asset["browser_download_url"], asset["name"],
                   int(asset.get("size") or 0), bool(version) and version > parse_version(__version__), sha256)


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def download(rel: Release, progress=None, cancelled=lambda: False) -> Path:
    """Download and unpack the release; returns the new app folder (with EloGlobal.exe) in the data folder."""
    STAGE.mkdir(parents=True, exist_ok=True)
    keep = {rel.asset_name, rel.asset_name + ".part"}      # a .part of this release resumes; older ones go
    for old in [*STAGE.glob("*.zip"), *STAGE.glob("*.zip.part")]:
        if old.name not in keep:
            old.unlink(missing_ok=True)
    zpath = fetch(rel.asset_url, STAGE / rel.asset_name, progress, cancelled)
    if rel.size and zpath.stat().st_size != rel.size:
        zpath.unlink(missing_ok=True)
        raise OSError("the download is incomplete - try again")
    if rel.sha256 and _sha256(zpath) != rel.sha256:
        zpath.unlink(missing_ok=True)
        raise OSError("the download doesn't match the release (checksum differs) - try again")
    new = STAGE / "new"
    shutil.rmtree(new, ignore_errors=True)
    with zipfile.ZipFile(zpath) as z:
        bad = z.testzip()
        if bad:
            raise OSError(f"the downloaded zip is damaged ({bad})")
        z.extractall(new)
    app = next((p.parent for p in new.rglob("EloGlobal.exe") if (p.parent / "main.py").is_file()), None)
    if app is None:
        raise OSError("the downloaded zip has no EloGlobal app folder")
    zpath.unlink(missing_ok=True)
    return app


SCRIPT = r"""@echo off
chcp 65001 >nul
rem EloGlobal update: waits until EloGlobal has closed, copies the new version over the app folder, starts it again.
setlocal
set "SRC={src}"
set "DST={dst}"
set "LOG={log}"
echo EloGlobal update %date% %time% > "%LOG%"
:wait
tasklist /FI "PID eq {pid}" /NH 2>nul | find /I "{exe}" >nul && (ping -n 2 127.0.0.1 >nul & goto wait)
ping -n 2 127.0.0.1 >nul
rem program files: mirror (removes files of the old version) but never the user's data, models or portable.txt
robocopy "%SRC%" "%DST%" /MIR /R:20 /W:1 /NFL /NDL /NP /XD "%DST%\data" "%DST%\models" /XF portable.txt >> "%LOG%"
if errorlevel 8 goto failed
rem voices that ship with the app: added or updated, downloaded ones are kept
if exist "%SRC%\models" robocopy "%SRC%\models" "%DST%\models" /E /R:20 /W:1 /NFL /NDL /NP >> "%LOG%"
if errorlevel 8 goto failed
echo OK >> "%LOG%"
start "" "%DST%\EloGlobal.exe"
rd /s /q "{stage}" 2>nul
exit /b 0
:failed
echo FAILED >> "%LOG%"
start "" "%DST%\EloGlobal.exe"
exit /b 1
"""


def install_on_exit(app_dir: Path) -> None:
    """Start the script that installs `app_dir` once this process has ended. The caller then quits the app."""
    script = DATA_DIR / "update.cmd"
    script.write_text(SCRIPT.format(src=app_dir, dst=ROOT, log=DATA_DIR / "logs" / "update.log", pid=os.getpid(),
                                    exe=Path(sys.executable).name, stage=STAGE / "new").replace("\n", "\r\n"),
                      encoding="utf-8")
    subprocess.Popen(["cmd.exe", "/c", str(script)], cwd=str(DATA_DIR), close_fds=True,
                     creationflags=subprocess.CREATE_NO_WINDOW | subprocess.CREATE_NEW_PROCESS_GROUP)
