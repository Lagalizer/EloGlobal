"""Builds the ready-to-ship EloGlobal: one folder with the app, its own Python and every package - nothing to install.

    runtime\\python.exe -s tools\\build_store.py [--out dist] [--no-msix] [--version 1.0.0.0]

Results (in dist\\):
  EloGlobal\                the app folder: EloGlobal.exe, main.py, eloglobal\, runtime\ (Python 3.13 + packages),
                            engines\espeak-ng, models\piper (English voice), licenses\, LICENSE, PRIVACY.md...
  steam\content\            the same folder, laid out as a Steam depot, + steam\scripts\*.vdf for SteamPipe
  github\EloGlobal-<version>-windows-x64.zip   the same folder + update.json, for GitHub releases (--github)
  msix\layout\              the same folder + AppxManifest.xml + Images\ (MSIX package logos)
  msix\EloGlobal.msix       the package for Partner Center (unsigned: the Microsoft Store signs it)

Uses the development runtime (runtime\) only to download and unpack wheels; the shipped runtime is a fresh copy of
the official embeddable Python. Every package is pinned in requirements-lock.txt and installed without its
dependencies (so PyAV, whose FFmpeg build has GPL parts, never gets in). Downloads are cached in dist\_cache.
"""
from __future__ import annotations

import argparse
import hashlib
import os
import re
import shutil
import subprocess
import sys
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PY_VERSION = "3.13.16"
PY_URL = f"https://www.python.org/ftp/python/{PY_VERSION}/python-{PY_VERSION}-embed-amd64.zip"
ESPEAK_MSI = "https://github.com/espeak-ng/espeak-ng/releases/download/1.52.0/espeak-ng.msi"
ESPEAK_MSI_SHA256 = "7f673c709ea5dd579d3b5ebb98688cc575328a6ab7438d2bc405b88cedaeafb9"
ESPEAK_SRC = "https://github.com/espeak-ng/espeak-ng/archive/refs/tags/1.52.0.tar.gz"
ESPEAK_SRC_SHA256 = "bb4338102ff3b49a81423da8a1a158b420124b055b60fa76cfb4b18677130a23"
SDK_TOOLS = "https://www.nuget.org/api/v2/package/Microsoft.Windows.SDK.BuildTools/10.0.26100.1742"
BUNDLED_VOICE = "en/en_US/kristin/medium/en_US-kristin-medium"
PIPER_URL = "https://huggingface.co/rhasspy/piper-voices/resolve/main"

APP_FILES = ["main.py", "LICENSE", "THIRD_PARTY_NOTICES.txt", "PRIVACY.md", "EloGlobal-debug.bat"]
APP_DIRS = ["eloglobal"]
TOOLS = ["tools/selftest.py", "tools/calltest.py"]
ASSETS = ["assets/icon.ico", "assets/icon.png", "assets/logo/eloglobal-icon.svg", "assets/logo/eloglobal-mark.svg"]

# Parts of packages the app never uses (Qt tools and QML, tests, headers, ASIO / non-x64 PortAudio builds)
STRIP_GLOBS = [
    "PySide6/*.exe", "PySide6/qml", "PySide6/include", "PySide6/typesystems", "PySide6/glue", "PySide6/doc",
    "PySide6/metatypes", "PySide6/scripts", "PySide6/translations",
    "PySide6/*.lib", "PySide6/Qt6Qml*.dll", "PySide6/Qt6Quick*.dll", "PySide6/Qt6Designer*.dll",
    "PySide6/Qt6Help.dll", "PySide6/Qt6Labs*.dll", "PySide6/Qt6Lottie*.dll", "PySide6/Qt6ShaderTools.dll",
    "PySide6/QtQml*", "PySide6/QtQuick*", "PySide6/QtDesigner*", "PySide6/QtHelp*", "PySide6/plugins/qmltooling",
    "PySide6/plugins/designer", "PySide6/plugins/qmllint", "PySide6/plugins/assetimporters",
    "_sounddevice_data/portaudio-binaries/*asio*", "_sounddevice_data/portaudio-binaries/*32bit*",
    "_sounddevice_data/portaudio-binaries/*arm64*", "_sounddevice_data/portaudio-binaries/*.dylib",
    "numpy/*/tests", "numpy/tests", "scipy/*/tests", "scipy/*/*/tests", "scipy/*/*/*/tests", "*/__pycache__",
    "bin",
]


def log(msg):
    print(f"==> {msg}", flush=True)


def fetch(url: str, dst: Path, sha256: str | None = None) -> Path:
    if not dst.exists():
        dst.parent.mkdir(parents=True, exist_ok=True)
        log(f"download {url}")
        req = urllib.request.Request(url, headers={"User-Agent": "EloGlobal-build"})
        with urllib.request.urlopen(req, timeout=60) as r, open(dst.with_suffix(dst.suffix + ".part"), "wb") as f:
            shutil.copyfileobj(r, f, 1 << 20)
        dst.with_suffix(dst.suffix + ".part").replace(dst)
    if sha256:
        h = hashlib.sha256(dst.read_bytes()).hexdigest()
        if h != sha256:
            raise SystemExit(f"checksum mismatch for {dst.name}: {h}")
    return dst


def run(cmd, **kw):
    print("   $", " ".join(str(c) for c in cmd), flush=True)
    subprocess.run([str(c) for c in cmd], check=True, **kw)


def rmtree(p: Path):
    if p.exists():
        shutil.rmtree(p, ignore_errors=False, onerror=lambda f, path, _e: (os.chmod(path, 0o666), f(path)))


# ------------------------------------------------------------------------------------------------ steps
def make_runtime(app: Path, cache: Path):
    rt = app / "runtime"
    log(f"Python {PY_VERSION} (embeddable)")
    with zipfile.ZipFile(fetch(PY_URL, cache / f"python-{PY_VERSION}-embed-amd64.zip")) as z:
        z.extractall(rt)
    pth = next(rt.glob("python*._pth"))
    zipname = next(rt.glob("python*.zip")).name
    pth.write_text("\n".join([zipname, ".", "Lib\\site-packages", "..", "import site"]) + "\n", encoding="ascii")
    sp = rt / "Lib" / "site-packages"
    sp.mkdir(parents=True, exist_ok=True)

    log("wheels (pinned in requirements-lock.txt, no dependencies resolved)")
    wheels = cache / "wheels"
    wheels.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ, PIP_DISABLE_PIP_VERSION_CHECK="1", PYTHONNOUSERSITE="1")
    lock = ROOT / "requirements-lock.txt"
    run([sys.executable, "-s", "-m", "pip", "wheel", "--no-deps", "--no-build-isolation", "-w", wheels, "-r", lock],
        env=env)
    run([sys.executable, "-s", "-m", "pip", "install", "--no-deps", "--no-index", "--find-links", wheels,
         "--target", sp, "--no-compile", "-r", lock], env=env)
    if (sp / "av").exists() or list(sp.glob("av-*.dist-info")):
        raise SystemExit("PyAV must not be in the build")

    log("strip unused parts")
    removed = 0
    for pattern in STRIP_GLOBS:
        for p in sp.glob(pattern):
            removed += 1
            rmtree(p) if p.is_dir() else p.unlink()
    print(f"   removed {removed} items")

    log("pre-compile Python files (the MSIX folder is read-only)")
    run([rt / "python.exe", "-s", "-m", "compileall", "-q", "-j", "0", sp, app / "eloglobal", app / "main.py"])


def copy_app(app: Path):
    log("app files")
    for f in APP_FILES + TOOLS + ASSETS:
        dst = app / f
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / f, dst)
    for d in APP_DIRS:
        shutil.copytree(ROOT / d, app / d, ignore=shutil.ignore_patterns("__pycache__", "*.pyc", "src"))
    # .bat files need CRLF
    for bat in app.glob("*.bat"):
        bat.write_bytes(bat.read_bytes().replace(b"\r\n", b"\n").replace(b"\n", b"\r\n"))


def build_launcher(app: Path):
    log("EloGlobal.exe (launcher)")
    csc = Path(os.environ["WINDIR"]) / "Microsoft.NET" / "Framework64" / "v4.0.30319" / "csc.exe"
    run([csc, "/nologo", "/target:winexe", "/optimize+", "/platform:anycpu", f"/win32icon:{ROOT / 'assets/icon.ico'}",
         "/r:System.Windows.Forms.dll", f"/out:{app / 'EloGlobal.exe'}", ROOT / "tools/launcher/EloGlobal.cs"])


def add_espeak(app: Path, cache: Path):
    log("eSpeak NG 1.52.0 (GPL-3, separate program) + its source code")
    msi = fetch(ESPEAK_MSI, cache / "espeak-ng-1.52.0.msi", ESPEAK_MSI_SHA256)
    src = fetch(ESPEAK_SRC, cache / "espeak-ng-1.52.0.tar.gz", ESPEAK_SRC_SHA256)
    x = cache / "espeak-x"
    if not (x / "eSpeak NG" / "espeak-ng.exe").exists():
        rmtree(x)
        run(["msiexec", "/a", msi, "/qn", f"TARGETDIR={x}"])
    shutil.copytree(x / "eSpeak NG", app / "engines" / "espeak-ng")
    lic = app / "licenses" / "espeak-ng"
    lic.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, lic / "espeak-ng-1.52.0.tar.gz")
    import tarfile
    with tarfile.open(src) as t:
        for m in t.getmembers():
            if m.name.endswith(("/COPYING", "/README.md", "/COPYING.APACHE", "/COPYING.BSD2", "/COPYING.UCD")) \
                    and m.name.count("/") == 1:
                f = t.extractfile(m)
                if f:
                    (lic / m.name.split("/")[-1]).write_bytes(f.read())
    (lic / "SOURCE.txt").write_text(
        "eSpeak NG 1.52.0 - https://github.com/espeak-ng/espeak-ng\n"
        "Binary: espeak-ng.msi of the official release, unmodified (engines\\espeak-ng).\n"
        "Complete corresponding source: espeak-ng-1.52.0.tar.gz in this folder (the release tag's source archive).\n"
        "Licence: GNU General Public License v3 or later (COPYING).\n", encoding="utf-8")


def add_voice(app: Path, cache: Path):
    log("bundled English voice (Piper Kristin, public domain)")
    d = app / "models" / "piper"
    d.mkdir(parents=True, exist_ok=True)
    name = BUNDLED_VOICE.split("/")[-1]
    for ext in (".onnx", ".onnx.json"):
        shutil.copy2(fetch(f"{PIPER_URL}/{BUNDLED_VOICE}{ext}", cache / "voices" / f"{name}{ext}"), d / f"{name}{ext}")
    card = fetch(f"{PIPER_URL}/{BUNDLED_VOICE.rsplit('/', 1)[0]}/MODEL_CARD", cache / "voices" / f"{name}.MODEL_CARD")
    shutil.copy2(card, d / f"{name}.MODEL_CARD.txt")


def collect_licences(app: Path):
    log("licence texts of every package -> licenses\\")
    sp = app / "runtime" / "Lib" / "site-packages"
    out = app / "licenses"
    names = re.compile(r"(LICEN[CS]E|COPYING|NOTICE|AUTHORS|ThirdParty)", re.I)
    for dist in sorted(sp.glob("*.dist-info")):
        pkg = re.sub(r"-[^-]+\.dist-info$", "", dist.name)
        files = [f for f in dist.rglob("*") if f.is_file() and names.search(f.name)]
        meta = dist / "METADATA"
        dst = out / pkg
        dst.mkdir(parents=True, exist_ok=True)
        for f in files:
            shutil.copy2(f, dst / f.name)
        if meta.exists():
            lines = [ln for ln in meta.read_text(encoding="utf-8", errors="replace").splitlines()
                     if ln.startswith(("Name:", "Version:", "License", "Home-page:", "Project-URL:", "Author"))]
            (dst / "METADATA.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    extra = {"onnxruntime": ["onnxruntime/ThirdPartyNotices.txt", "onnxruntime/LICENSE"],
             "PySide6": ["PySide6/LICENSES"], "_sounddevice_data": ["_sounddevice_data/portaudio-binaries/README.md"],
             "soundfile": ["_soundfile_data/COPYING"]}
    for pkg, rels in extra.items():
        for rel in rels:
            src = sp / rel
            if src.is_dir():
                shutil.copytree(src, out / pkg / src.name, dirs_exist_ok=True)
            elif src.exists():
                (out / pkg).mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, out / pkg / src.name)
    py = out / "python"
    py.mkdir(exist_ok=True)
    for f in (app / "runtime").glob("LICENSE*"):
        shutil.copy2(f, py / f.name)


def steam_layout(app: Path, dist: Path):
    log("Steam depot layout")
    steam = dist / "steam"
    rmtree(steam)
    shutil.copytree(app, steam / "content" / "EloGlobal")
    scripts = steam / "scripts"
    scripts.mkdir(parents=True)
    (scripts / "app_build_APPID.vdf").write_text('''"AppBuild"
{
	"AppID" "APPID"
	"Desc" "EloGlobal build"
	"ContentRoot" "..\\\\content\\\\"
	"BuildOutput" "..\\\\output\\\\"
	"Depots"
	{
		"DEPOTID" "depot_build_DEPOTID.vdf"
	}
}
''', encoding="utf-8")
    (scripts / "depot_build_DEPOTID.vdf").write_text('''"DepotBuild"
{
	"DepotID" "DEPOTID"
	"FileMapping"
	{
		"LocalPath" "EloGlobal\\\\*"
		"DepotPath" "."
		"Recursive" "1"
	}
	"FileExclusion" "*.pdb"
}
''', encoding="utf-8")
    (steam / "README.txt").write_text(
        "Replace APPID / DEPOTID in scripts\\ with your Steamworks ids (file names too), then run\n"
        "  steamcmd +login <builder account> +run_app_build ..\\scripts\\app_build_<APPID>.vdf +quit\n"
        "Launch option in Steamworks (Installation > General): Executable = EloGlobal.exe, OS = Windows, 64-bit.\n",
        encoding="utf-8")


MANIFEST = '''<?xml version="1.0" encoding="utf-8"?>
<Package xmlns="http://schemas.microsoft.com/appx/manifest/foundation/windows10"
         xmlns:uap="http://schemas.microsoft.com/appx/manifest/uap/windows10"
         xmlns:rescap="http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities"
         IgnorableNamespaces="uap rescap">
  <!-- Identity Name / Publisher / PublisherDisplayName: replace with the values Partner Center shows under
       Product management > Product identity before uploading. -->
  <Identity Name="Lagalizer.EloGlobal" Publisher="CN=Lagalizer" Version="{version}" ProcessorArchitecture="x64"/>
  <Properties>
    <DisplayName>EloGlobal</DisplayName>
    <PublisherDisplayName>Lagalizer</PublisherDisplayName>
    <Logo>Images\\StoreLogo.png</Logo>
    <Description>Real-time voice and chat translator for voice calls. Runs on your PC only.</Description>
  </Properties>
  <Dependencies>
    <TargetDeviceFamily Name="Windows.Desktop" MinVersion="10.0.19041.0" MaxVersionTested="10.0.26100.0"/>
  </Dependencies>
  <Resources>
    <Resource Language="en-us"/><Resource Language="pt-br"/><Resource Language="es-es"/><Resource Language="fr-fr"/>
    <Resource Language="de-de"/><Resource Language="it-it"/><Resource Language="ru-ru"/><Resource Language="uk-ua"/>
    <Resource Language="pl-pl"/><Resource Language="tr-tr"/>
  </Resources>
  <Applications>
    <Application Id="EloGlobal" Executable="EloGlobal.exe" EntryPoint="Windows.FullTrustApplication">
      <uap:VisualElements DisplayName="EloGlobal" Description="Real-time voice and chat translator for voice calls"
                          BackgroundColor="#0B5F58" Square150x150Logo="Images\\Square150x150Logo.png"
                          Square44x44Logo="Images\\Square44x44Logo.png">
        <uap:DefaultTile Wide310x150Logo="Images\\Wide310x150Logo.png" Square71x71Logo="Images\\Square71x71Logo.png"
                         Square310x310Logo="Images\\Square310x310Logo.png" ShortName="EloGlobal">
          <uap:ShowNameOnTiles><uap:ShowOn Tile="square150x150Logo"/></uap:ShowNameOnTiles>
        </uap:DefaultTile>
        <uap:SplashScreen Image="Images\\SplashScreen.png" BackgroundColor="#0B5F58"/>
      </uap:VisualElements>
    </Application>
  </Applications>
  <Capabilities>
    <rescap:Capability Name="runFullTrust"/>
    <DeviceCapability Name="microphone"/>
  </Capabilities>
</Package>
'''


def msix(app: Path, dist: Path, cache: Path, version: str):
    log("MSIX layout + package")
    out = dist / "msix"
    rmtree(out)
    layout = out / "layout"
    shutil.copytree(app, layout)
    assets = layout / "Images"          # not "Assets": the app folder already has assets (same name for Windows)
    assets.mkdir()
    for f in (ROOT / "assets" / "msstore" / "package").glob("*.png"):
        shutil.copy2(f, assets / f.name)
    (layout / "AppxManifest.xml").write_text(MANIFEST.replace("{version}", version), encoding="utf-8")
    nupkg = fetch(SDK_TOOLS, cache / "Microsoft.Windows.SDK.BuildTools.nupkg")
    tools = cache / "sdk-buildtools"
    if not tools.exists():
        with zipfile.ZipFile(nupkg) as z:
            z.extractall(tools)
    makeappx = next(p for p in tools.rglob("makeappx.exe") if "x64" in p.parts)
    makepri = next((p for p in tools.rglob("makepri.exe") if "x64" in p.parts), None)
    if makepri:                                  # resources.pri: the scale-100/125/... logos for every DPI
        run([makepri, "createconfig", "/cf", out / "priconfig.xml", "/dq", "en-US", "/o"])
        cfg = (out / "priconfig.xml").read_text(encoding="utf-8")         # one package: no split resource packs
        (out / "priconfig.xml").write_text(re.sub(r"<packaging>.*?</packaging>", "", cfg, flags=re.S),
                                           encoding="utf-8")
        run([makepri, "new", "/pr", layout, "/cf", out / "priconfig.xml", "/of", layout / "resources.pri", "/o"])
    run([makeappx, "pack", "/d", layout, "/p", out / "EloGlobal.msix", "/o"])


def github_zip(app: Path, dist: Path, repo: str, version: str) -> Path:
    """The download for GitHub releases: the app folder + update.json (Settings -> Updates updates from `repo`).
    The store builds have no update.json: their store updates them."""
    log("GitHub release zip")
    out = dist / "github"
    rmtree(out)
    out.mkdir(parents=True)
    zpath = out / f"EloGlobal-{version}-windows-x64.zip"
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for f in sorted(app.rglob("*")):
            if f.is_file():
                z.write(f, Path("EloGlobal") / f.relative_to(app))
        z.writestr("EloGlobal/update.json", '{"repo": "%s"}\n' % repo)
    print(f"   {zpath} ({zpath.stat().st_size / 1e6:.0f} MB)")
    return zpath


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "dist"))
    ap.add_argument("--no-msix", action="store_true")
    ap.add_argument("--version", default="")
    ap.add_argument("--github", default="Lagalizer/EloGlobal", metavar="OWNER/REPO",
                    help="repository the GitHub zip updates from ('' = no GitHub zip)")
    a = ap.parse_args()
    sys.path.insert(0, str(ROOT))
    from eloglobal import __version__
    version = a.version or (__version__ + ".0")
    dist = Path(a.out)
    cache = dist / "_cache"
    app = dist / "EloGlobal"
    rmtree(app)
    app.mkdir(parents=True)
    copy_app(app)
    make_runtime(app, cache)
    build_launcher(app)
    add_espeak(app, cache)
    add_voice(app, cache)
    collect_licences(app)
    size = sum(f.stat().st_size for f in app.rglob("*") if f.is_file())
    log(f"app folder ready: {app}  ({size / 1e6:.0f} MB)")
    steam_layout(app, dist)
    if a.github:
        github_zip(app, dist, a.github, __version__)
    if not a.no_msix:
        msix(app, dist, cache, version)
    log("done")


if __name__ == "__main__":
    main()
