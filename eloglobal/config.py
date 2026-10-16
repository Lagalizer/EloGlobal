r"""Paths, profiles (save/load) and the small store for the one secret the app keeps.

Where things live:
- ROOT           the app folder. Read-only when installed from a store (MSIX / Steam): only program files, the
                 bundled engines (engines\espeak-ng) and the bundled voice (models\) are there.
- DATA_DIR       %LOCALAPPDATA%\EloGlobal - profiles, logs, transcripts, app state, restore files, secrets.
- MODELS_DIR     %LOCALAPPDATA%\EloGlobal\models - speech, translation and voice models, downloaded once.
A file named portable.txt next to main.py keeps everything inside the app folder instead (development copies).
When the app runs from its MSIX package, Windows redirects writes to %LOCALAPPDATA% into the package's own folder;
that real path is used directly, so "Open data folder" shows the files in Explorer.
"""
import base64
import copy
import ctypes
import json
import os
import re
import sys
import threading
from pathlib import Path

from . import languages

if getattr(sys, "frozen", False):
    ROOT = Path(sys.executable).parent
else:
    ROOT = Path(__file__).resolve().parent.parent

APP_DIR_NAME = "EloGlobal"
PORTABLE = (ROOT / "portable.txt").exists()


def _package_family() -> str:
    """The MSIX package family name when the app runs from its Microsoft Store package, else ""."""
    if os.name != "nt":
        return ""
    try:
        n = ctypes.c_uint32(0)
        k32 = ctypes.windll.kernel32
        if k32.GetCurrentPackageFamilyName(ctypes.byref(n), None) != 122:     # ERROR_INSUFFICIENT_BUFFER
            return ""                                                        # 15700 = not in a package
        buf = ctypes.create_unicode_buffer(n.value)
        return buf.value if k32.GetCurrentPackageFamilyName(ctypes.byref(n), buf) == 0 else ""
    except Exception:  # noqa: BLE001
        return ""


PACKAGE_FAMILY = _package_family()


def _user_dir() -> Path:
    if PORTABLE:
        return ROOT / "data"
    local = Path(os.environ.get("LOCALAPPDATA") or Path.home() / "AppData" / "Local")
    if PACKAGE_FAMILY:                           # MSIX: where Windows would redirect our writes anyway
        return local / "Packages" / PACKAGE_FAMILY / "LocalCache" / "Local" / APP_DIR_NAME
    return local / APP_DIR_NAME


DATA_DIR = _user_dir()
PROFILES_DIR = DATA_DIR / "profiles"
TRANSCRIPTS_DIR = DATA_DIR / "transcripts"
LOGS_DIR = DATA_DIR / "logs"
MODELS_DIR = ROOT / "models" if PORTABLE else DATA_DIR / "models"
BUNDLED_MODELS_DIR = ROOT / "models"            # voices shipped with the app (read-only)
ENGINES_DIR = ROOT / "engines"                  # separate programs shipped with the app (espeak-ng)
SECRETS_FILE = DATA_DIR / "secrets.json"
APP_STATE_FILE = DATA_DIR / "app_state.json"

for _d in (DATA_DIR, PROFILES_DIR, TRANSCRIPTS_DIR, LOGS_DIR, MODELS_DIR):
    _d.mkdir(parents=True, exist_ok=True)

PROFILE_VERSION = 3       # 2: Discord-only listening, app voice settings; 3: only engines that run on this PC


def default_profile() -> dict:
    me = languages.system_language()
    them = "en" if languages.base(me) != "en" else "es"
    return {
        "name": "Default",
        "version": PROFILE_VERSION,
        "incoming": {                      # what other people say -> me
            "enabled": True,
            "source_lang": "auto",
            "target_lang": me,
            "speak": True,                 # read the translation out loud to me
            "show_subtitles": True,
            "skip_same_language": True,    # don't re-speak lines already in my language
            "output_device": "",           # where I hear translations ("" = system default)
            "volume": 1.0,
            "voice_speed": 1.0,            # translated voice: speed (any voice engine)
            "voice_pitch": 0.0,            # ... and pitch in semitones
            "passthrough": False,          # forward the captured Discord audio to my output device
            "passthrough_volume": 1.0,
            "duck_passthrough": 0.25,      # their voices' volume while a translation is spoken (hear people: on)
            "hear_originals": False,       # hear the people in the call too (hotkey input.hear_key toggles it)
        },
        "outgoing": {                      # what I say -> other people
            "enabled": True,
            "source_lang": me,
            "target_lang": them,
            "follow_their_language": False,  # auto-switch target to the last language I heard
            "speak": True,
            "output_device": "CABLE Input",  # virtual cable that Discord uses as its microphone
            "volume": 1.0,
            "voice_speed": 1.0,
            "voice_pitch": 0.0,
            "monitor_device": "",            # optionally hear your own translated voice
            "monitor_volume": 0.5,
            "monitor": False,
        },
        "input": {
            "listen_mode": "app",          # app = only the Discord app (recommended) | loopback = an output device
                                           # | device = an input device
            "listen_app": "discord",       # app mode: which app ("discord" = Discord / PTB / Canary)
            "listen_device": "",           # loopback: output device name; device: input device name
            "mic_device": "",
            "mic_mode": "vad",             # vad | ptt | toggle
            "ptt_key": "f8",
            "hear_key": "f9",              # toggles hearing the people in the call (their original voices)
            "listen_vad": {"auto": True, "threshold_db": -45.0, "silence_ms": 550, "min_speech_ms": 350,
                           "max_utterance_s": 12.0, "pre_roll_ms": 300},
            "mic_vad": {"auto": True, "threshold_db": -42.0, "silence_ms": 500, "min_speech_ms": 300,
                        "max_utterance_s": 15.0, "pre_roll_ms": 300},
            "pause_listen_while_speaking": True,   # loopback mode: avoid translating our own translations (echo)
            "ignore_mic_while_playing": False,     # True only without headphones (the echo filter handles the rest)
            "mic_gain_db": 0.0,
            "listen_gain_db": 0.0,
        },
        "stt": {"provider": "faster_whisper", "settings": {}},
        "translation": {
            "provider": "opus_mt",
            "settings": {},
            "style": "natural",            # natural | casual | formal | literal
            "context_lines": 4,            # recent lines given to a local AI model
            "glossary": "",                # one per line: term = translation   (or just term to keep as-is)
            "keep_profanity": True,
        },
        "ai": {"provider": "ollama", "settings": {}, "custom_prompt": ""},
        "tts": {
            "provider": "local",
            "settings": {},
            "voices": {},                  # provider_id -> {"incoming": voice, "outgoing": voice}
            "gender": "female",
        },
        "speech": {                        # the app voice (call translations and chat messages read aloud)
            "names": "short",              # say who talked: short (first 2 letters) | first | full | off
            "repeat_names": False,         # say the name again when the same person goes on talking
            "catchup": True,               # speak a little faster when lines pile up
        },
        "speakers": {                      # who is talking in the voice call (Discord RPC, optional)
            "enabled": False,
            "client_id": "",               # your Discord application's id (secret: secrets.json)
        },
        "chat": {
            "auto_translate": False,       # read Discord messages from the window and translate them
            "target_lang": me,
            "skip_same_language": True,
            "include_embeds": True,
            "my_name": "",                 # your Discord display name - your own messages are skipped
            "history": 5,                  # translate the last N messages when you open a channel
            "poll_ms": 700,
            "overlay_attach": True,        # keep the chat overlay docked to the Discord window
            "overlay_lines": 6,
            "engine": "",                  # translation engine for text ("" = same as the Translation tab)
            "display": "inline",           # where translations show: inline (on the messages in Discord) | window | both
            "hotkey_inline": "ctrl+alt+i", # show the originals / the translations
            "speak": False,                # read translated chat messages out loud
            "speak_mode": "queue",         # queue = one after the other | interrupt = a new one cuts the old one
            "select_translate": True,      # translate text you highlight with the mouse
            "select_scope": "discord",     # discord | everywhere
            "popup_seconds": 10,
            "hotkey_selection": "ctrl+alt+t",
            "hotkey_draft": "ctrl+alt+y",  # translate what you typed in Discord's message box, in place
            "hotkey_ocr": "ctrl+alt+o",    # select a screen area and translate the text in it
            "compose_lang": "auto",        # auto = the language people use in the chat
            "draft_send": False,           # press Enter after translating the draft
            "ocr_lang": "auto",
            "clipboard_watch": False,      # translate everything you copy
        },
        "ui": {
            "subtitle_font_size": 22,
            "subtitle_opacity": 0.85,
            "subtitle_show_original": True,
            "subtitle_lines": 3,
            "subtitle_show_mine": True,
            "autosave_transcript": False,   # off: other people's words are kept only if you want
            "autosave_settings": True,       # save the profile by itself ~1 s after every change
        },
    }


def deep_merge(base: dict, override: dict) -> dict:
    out = copy.deepcopy(base)
    for k, v in (override or {}).items():
        if isinstance(v, dict) and isinstance(out.get(k), dict) and k not in ("settings", "voices"):
            out[k] = deep_merge(out[k], v)
        else:
            out[k] = copy.deepcopy(v)
    return out


def _safe_filename(name: str) -> str:
    s = re.sub(r"[^\w\- ]+", "_", name, flags=re.UNICODE).strip()
    return s or "profile"


def list_profiles() -> list[str]:
    names = []
    for p in sorted(PROFILES_DIR.glob("*.json")):
        try:
            names.append(json.loads(p.read_text(encoding="utf-8")).get("name") or p.stem)
        except Exception:
            names.append(p.stem)
    return names


def profile_path(name: str) -> Path:
    return PROFILES_DIR / f"{_safe_filename(name)}.json"


def migrate(data: dict) -> dict:
    """Bring a profile saved by an older version up to date (only settings that were left at their old default)."""
    if not data or data.get("version", 1) >= PROFILE_VERSION:
        return data
    inp = data.setdefault("input", {})
    if inp.get("listen_mode", "loopback") == "loopback" and not inp.get("listen_device"):
        inp["listen_mode"] = "app"            # was: everything on the default speakers (the app's own voice too)
    if inp.get("ignore_mic_while_playing", True):
        inp["ignore_mic_while_playing"] = False   # keep listening to you while the app talks (echo filter instead)
    for key, old, new in (("listen_vad", 700, 550), ("mic_vad", 600, 500)):
        vad = inp.get(key) or {}
        if vad.get("silence_ms") == old:
            vad["silence_ms"] = new
    # v3: only engines that run on this PC exist; an online engine falls back to the local default
    from .providers import REGISTRY
    for section, kind in (("stt", "stt"), ("translation", "translate"), ("ai", "llm"), ("tts", "tts")):
        sec = data.get(section) or {}
        if sec.get("provider") and sec["provider"] not in REGISTRY[kind]:
            sec.pop("provider", None)
            sec.pop("settings", None)
    chat = data.get("chat") or {}
    if chat.get("engine") and chat["engine"] not in REGISTRY["translate"]:
        chat["engine"] = ""
    data["version"] = PROFILE_VERSION
    return data


def load_profile(name: str) -> dict:
    p = profile_path(name)
    data = json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}
    prof = deep_merge(default_profile(), migrate(data))
    prof["name"] = name
    return prof


def write_atomic(path: Path, text: str) -> None:
    """Write a file so that a crash or power cut leaves either the old or the new content, never half of it."""
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(text, encoding="utf-8")
    os.replace(tmp, path)


def save_profile(profile: dict, name: str | None = None) -> Path:
    if name:
        profile["name"] = name
    p = profile_path(profile["name"])
    write_atomic(p, json.dumps(profile, indent=2, ensure_ascii=False))
    return p


def delete_profile(name: str) -> None:
    p = profile_path(name)
    if p.exists():
        p.unlink()


def import_profile(path: str) -> dict:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    prof = deep_merge(default_profile(), migrate(data))
    prof["name"] = data.get("name") or Path(path).stem
    return prof


def export_profile(profile: dict, path: str) -> None:
    Path(path).write_text(json.dumps(profile, indent=2, ensure_ascii=False), encoding="utf-8")


# Starter profiles written on first run: (name, overrides). Every engine runs on this PC.
TEMPLATES = [
    ("Standard - everything on this PC", {}),
    ("Fastest - for slower PCs", {
        "stt": {"provider": "faster_whisper", "settings": {"faster_whisper": {"model": "base"}}},
    }),
    ("Best quality - NVIDIA graphics card", {
        "stt": {"provider": "faster_whisper", "settings": {"faster_whisper": {"model": "large-v3-turbo",
                                                                             "device": "cuda"}}},
    }),
    ("AI translation - Ollama on this PC", {
        "translation": {"provider": "llm", "settings": {}},
        "ai": {"provider": "ollama", "settings": {}},
    }),
]


def ensure_starter_profiles() -> None:
    if any(PROFILES_DIR.glob("*.json")):
        return
    for name, overrides in TEMPLATES:
        prof = deep_merge(default_profile(), overrides)
        prof["name"] = name
        save_profile(prof)


def load_app_state() -> dict:
    try:
        return json.loads(APP_STATE_FILE.read_text(encoding="utf-8"))
    except Exception:
        return {}


def save_app_state(state: dict) -> None:
    write_atomic(APP_STATE_FILE, json.dumps(state, indent=2))


# --------------------------------------------------------------------------- secrets

# The only secret the app keeps: the client secret (and login token) of the user's own Discord application, used by
# "Who is talking". Encrypted for the Windows user (DPAPI); never put in profiles or exports.
KNOWN_KEYS = {
    "discord_rpc_secret": ("Discord application client secret (who is talking)", "ELOGLOBAL_DISCORD_SECRET"),
}


class _Blob(ctypes.Structure):
    _fields_ = [("cbData", ctypes.c_uint32), ("pbData", ctypes.POINTER(ctypes.c_char))]


def _dpapi(data: bytes, protect: bool) -> bytes:
    """Encrypt / decrypt for the current Windows user (CryptProtectData). Elsewhere the data is kept as it is."""
    if os.name != "nt":
        return data
    buf = ctypes.create_string_buffer(data, len(data))
    src, out = _Blob(len(data), ctypes.cast(buf, ctypes.POINTER(ctypes.c_char))), _Blob()
    fn = ctypes.windll.crypt32.CryptProtectData if protect else ctypes.windll.crypt32.CryptUnprotectData
    if not fn(ctypes.byref(src), None, None, None, None, 0x1, ctypes.byref(out)):    # CRYPTPROTECT_UI_FORBIDDEN
        raise OSError("DPAPI failed")
    try:
        return ctypes.string_at(out.pbData, out.cbData)
    finally:
        ctypes.windll.kernel32.LocalFree(out.pbData)


class KeyStore:
    """Secrets in DATA_DIR/secrets.json (encrypted with DPAPI), falling back to environment variables."""

    def __init__(self, path: Path = SECRETS_FILE):
        self.path = path
        self._lock = threading.Lock()
        try:
            raw = json.loads(path.read_text(encoding="utf-8"))
            self._keys = json.loads(_dpapi(base64.b64decode(raw["dpapi"]), False).decode("utf-8"))
        except Exception:  # noqa: BLE001 - missing or unreadable: start empty
            self._keys = {}

    def get(self, key_id: str) -> str:
        v = (self._keys.get(key_id) or "").strip()
        if v:
            return v
        env = KNOWN_KEYS.get(key_id, (None, ""))[1]
        return os.environ.get(env, "").strip() if env else ""

    def stored(self, key_id: str) -> str:
        return self._keys.get(key_id, "")

    def set(self, key_id: str, value: str) -> None:
        with self._lock:
            if value:
                self._keys[key_id] = value.strip()
            else:
                self._keys.pop(key_id, None)

    def save(self) -> None:
        with self._lock:
            blob = _dpapi(json.dumps(self._keys).encode("utf-8"), True)
            write_atomic(self.path, json.dumps({"dpapi": base64.b64encode(blob).decode("ascii")}))
