"""EloGlobal - entry point.  Run:  EloGlobal.exe  (or runtime\\pythonw.exe -s main.py)

Options (for tests): --smoke [seconds]   open the window, wait, write "SMOKE OK" to the log and quit
                     --lang <code>       use this app language for this run (en, pt, ...)
"""
import logging
import logging.handlers
import os
import site
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

# Only the app's own runtime: never packages from the user's Python (AppData\Roaming\Python\...).
if not sys.flags.no_user_site:
    _user = site.getusersitepackages() if hasattr(site, "getusersitepackages") else ""
    sys.path[:] = [p for p in sys.path if not (_user and p.startswith(_user)) and "AppData\\Roaming\\Python" not in p]


def _setup_env():
    """Model downloads (Hugging Face cache...) go to the user's models folder, never into the app folder."""
    sys.path.insert(0, str(ROOT))
    from eloglobal.config import MODELS_DIR
    os.environ.setdefault("HF_HOME", str(MODELS_DIR / "huggingface"))
    os.environ.setdefault("HF_HUB_DISABLE_SYMLINKS_WARNING", "1")
    os.environ.setdefault("HF_HUB_DISABLE_TELEMETRY", "1")
    os.environ.setdefault("HF_HUB_DISABLE_IMPLICIT_TOKEN", "1")
    os.environ.setdefault("XDG_CACHE_HOME", str(MODELS_DIR / "cache"))


def _add_cuda_dlls():
    """Make NVIDIA libraries visible to CTranslate2: the optional GPU download (models\\gpu) or pip packages."""
    if os.name != "nt":
        return
    from eloglobal.config import MODELS_DIR
    dirs = [MODELS_DIR / "gpu"]
    for sp in sys.path:
        nv = Path(sp) / "nvidia"
        if nv.is_dir():
            dirs += list(nv.glob("*/bin"))
    for bin_dir in dirs:
        if bin_dir.is_dir():
            try:
                os.add_dll_directory(str(bin_dir))
            except OSError:
                pass
            os.environ["PATH"] = str(bin_dir) + os.pathsep + os.environ.get("PATH", "")


def _setup_logging():
    from eloglobal.config import LOGS_DIR
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    fh = logging.handlers.RotatingFileHandler(LOGS_DIR / "eloglobal.log", maxBytes=2_000_000, backupCount=3,
                                              encoding="utf-8")
    fh.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s"))
    root.addHandler(fh)
    if sys.stderr:
        sh = logging.StreamHandler()
        sh.setFormatter(logging.Formatter("%(levelname)s %(name)s: %(message)s"))
        root.addHandler(sh)
    for noisy in ("httpx", "httpcore", "urllib3", "faster_whisper", "huggingface_hub"):
        logging.getLogger(noisy).setLevel(logging.WARNING)


def _splash(app, icon: Path):
    """A small window shown while the app loads (no text to translate)."""
    from PySide6.QtCore import Qt
    from PySide6.QtGui import QColor, QFont, QIcon, QPainter, QPixmap
    from PySide6.QtWidgets import QSplashScreen
    pm = QPixmap(380, 150)
    pm.fill(QColor("#14202b"))
    p = QPainter(pm)
    if icon.exists():
        p.drawPixmap(24, 43, QIcon(str(icon)).pixmap(64, 64))
    p.setPen(QColor("#e8eef3"))
    f = QFont()
    f.setPointSize(22)
    f.setBold(True)
    p.setFont(f)
    p.drawText(pm.rect().adjusted(102, 0, 0, -12), Qt.AlignVCenter, "EloGlobal")
    p.setPen(QColor("#2ec4b6"))
    f.setPointSize(14)
    p.setFont(f)
    p.drawText(pm.rect().adjusted(104, 46, 0, 0), Qt.AlignVCenter, "• • •")
    p.end()
    s = QSplashScreen(pm)
    s.show()
    app.processEvents()
    return s


DEMO = [  # (direction, who, original, translation in the app language, source, target) - English <-> app language
    ("incoming", "Alex", "Hey, can you hear me? We should push B together.",
     {"pt": "Ei, dá pra me ouvir? A gente devia avançar no B juntos.", "es": "Oye, ¿me oyes? Deberíamos ir al B juntos.",
      "de": "Hey, hörst du mich? Wir sollten zusammen auf B gehen.", "fr": "Hé, tu m'entends ? On devrait pousser B ensemble.",
      "it": "Ehi, mi senti? Dovremmo spingere su B insieme.", "ru": "Эй, слышишь меня? Давай вместе пойдём на B.",
      "uk": "Гей, чуєш мене? Давай разом підемо на B.", "pl": "Hej, słyszysz mnie? Powinniśmy razem wejść na B.",
      "tr": "Hey, beni duyuyor musun? B'ye birlikte gitmeliyiz.", "en": "Hey, can you hear me? We should push B together."}),
    ("outgoing", "", "", {}),
    ("incoming", "Sam", "Nice shot! One enemy left behind the wall.",
     {"pt": "Belo tiro! Sobrou um inimigo atrás do muro.", "es": "¡Buen tiro! Queda un enemigo detrás del muro.",
      "de": "Schöner Schuss! Ein Gegner ist noch hinter der Mauer.", "fr": "Joli tir ! Il reste un ennemi derrière le mur.",
      "it": "Bel colpo! È rimasto un nemico dietro il muro.", "ru": "Отличный выстрел! За стеной остался один враг.",
      "uk": "Чудовий постріл! За стіною лишився один ворог.", "pl": "Ładny strzał! Za ścianą został jeden przeciwnik.",
      "tr": "Güzel atış! Duvarın arkasında bir düşman kaldı.", "en": "Nice shot! One enemy left behind the wall."}),
]
DEMO_MINE = {"pt": ("Tô indo pela esquerda, me cobre!", "I'm going left, cover me!"),
             "es": ("¡Voy por la izquierda, cúbreme!", "I'm going left, cover me!"),
             "de": ("Ich gehe links rum, gib mir Deckung!", "I'm going left, cover me!"),
             "fr": ("Je passe par la gauche, couvre-moi !", "I'm going left, cover me!"),
             "it": ("Vado a sinistra, coprimi!", "I'm going left, cover me!"),
             "ru": ("Я иду слева, прикрой меня!", "I'm going left, cover me!"),
             "uk": ("Я йду ліворуч, прикрий мене!", "I'm going left, cover me!"),
             "pl": ("Idę lewą stroną, osłaniaj mnie!", "I'm going left, cover me!"),
             "tr": ("Soldan gidiyorum, beni koru!", "I'm going left, cover me!"),
             "en": ("I'm going left, cover me!", "Voy por la izquierda, ¡cúbreme!")}


DEMO_ES = [("¿Me oyes? Deberíamos ir al B juntos.", "Can you hear me? We should push B together."),
           ("¡Buen tiro! Queda un enemigo detrás del muro.", "Nice shot! One enemy left behind the wall.")]


def _demo(win, code: str):
    """Show a short sample conversation in the transcript, the subtitles and the dashboard. The people in the call
    speak English (Spanish when the app itself is in English); you speak the app language."""
    other = "es" if code == "en" else "en"
    for combo, value in ((win.in_src, other), (win.in_tgt, code), (win.out_src, code), (win.out_tgt, other)):
        combo.setValue(value)
    incoming = iter(DEMO_ES if code == "en" else [(d[2], d[3].get(code, d[2])) for d in DEMO if d[0] == "incoming"])
    mine, theirs = DEMO_MINE.get(code, DEMO_MINE["en"])
    n = 0
    for direction, who, _o, _t in DEMO:
        n += 1
        if direction == "outgoing":
            ev = {"type": "line", "dir": "outgoing", "id": n, "original": mine, "translated": theirs,
                  "src": code, "tgt": other, "timings": {"stt": 0.9, "mt": 0.1}, "skipped": False, "typed": False,
                  "who": "", "latency": 1.3}
        else:
            original, translated = next(incoming)
            ev = {"type": "line", "dir": "incoming", "id": n, "original": original, "translated": translated,
                  "src": other, "tgt": code, "timings": {"stt": 0.8, "mt": 0.1}, "skipped": False, "typed": False,
                  "who": who, "latency": 1.4}
        win.on_event(ev)
    win.on_event({"type": "spoken", "dir": "incoming", "id": n, "timings": {"stt": 0.8, "mt": 0.1, "tts": 0.1},
                  "latency": 1.6})
    win.overlay.show()


def _arg(name: str, default=None):
    if name in sys.argv:
        i = sys.argv.index(name)
        return sys.argv[i + 1] if i + 1 < len(sys.argv) and not sys.argv[i + 1].startswith("--") else default
    return None


def main():
    _setup_env()
    _add_cuda_dlls()
    _setup_logging()
    log = logging.getLogger("eloglobal")

    def excepthook(et, ev, tb):
        log.error("Unhandled error", exc_info=(et, ev, tb))
    sys.excepthook = excepthook

    from PySide6.QtCore import QTimer
    from PySide6.QtGui import QIcon
    from PySide6.QtWidgets import QApplication

    from eloglobal import APP_NAME, __version__, config, i18n
    from eloglobal.gui import theme
    from eloglobal.gui.about import PrivacyDialog
    from eloglobal.gui.language_dialog import choose_language

    if os.name == "nt":  # own taskbar icon/group instead of python's
        try:
            import ctypes
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("Lagalizer.EloGlobal")
        except Exception:
            pass
    app = QApplication(sys.argv)
    app.setApplicationName(APP_NAME)
    icon = ROOT / "assets" / "icon.ico"
    if icon.exists():
        app.setWindowIcon(QIcon(str(icon)))
    log.info("%s %s starting (Python %s), data in %s", APP_NAME, __version__, sys.version.split()[0], config.DATA_DIR)

    # the language of the app: chosen before the main window opens (first start), then everything is in it
    state = config.load_app_state()
    theme.apply(app, state.get("theme", "dark"))
    i18n.install()
    forced = _arg("--lang")
    if forced in i18n.BY_CODE:
        code, asked = forced, False
    else:
        code, asked = choose_language(state)
    i18n.set_language(code)
    if not forced:
        state["ui_language"] = code
    if asked and not state.get("seen_setup"):
        state["tour_pending"] = True             # a fresh install: the guided tour opens with the main window
    smoke = "--smoke" in sys.argv
    if not state.get("privacy_seen") and not smoke:
        PrivacyDialog(first_run=True).exec()     # other people's voices and chat are processed (on this PC)
        state["privacy_seen"] = 1
    config.save_app_state(state)
    log.info("app language: %s", code)

    splash = _splash(app, icon)
    from eloglobal import natural                # the Manual / the guide read aloud: load their voice before the
    natural.preload()                            # window exists (loading it freezes Python for a moment)
    if state.get("tour_pending") and not smoke:
        from eloglobal.gui.tour import prepare_voice
        prepare_voice()                          # the guide's first steps are synthesised while the window is built

    from eloglobal.gui.main_window import MainWindow
    win = MainWindow(app)
    win.show()
    splash.finish(win)
    if smoke:
        secs = float(_arg("--smoke", "4") or 4)
        size = _arg("--size")                   # e.g. 1920x1080 for store screenshots
        if size:
            w, h = (int(x) for x in size.lower().split("x"))
            dpr = win.devicePixelRatioF() or 1.0
            win.resize(int(w / dpr), int(h / dpr))
        if "--demo" in sys.argv:                # a sample conversation (store screenshots)
            _demo(win, code)

        def done():
            tabs = [win.tabs.tabText(i) for i in range(win.tabs.count())]
            shots = _arg("--shots")
            if shots:                            # a picture of every tab (store screenshots, UI checks)
                Path(shots).mkdir(parents=True, exist_ok=True)
                for i in range(win.tabs.count()):
                    win.tabs.setCurrentIndex(i)
                    for _ in range(5):
                        app.processEvents()
                    win.grab().save(str(Path(shots) / f"{code}-{i:02d}.png"))
            log.info("SMOKE OK - %s tabs: %s", len(tabs), ", ".join(tabs))
            app.quit()
        QTimer.singleShot(int(secs * 1000), done)
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
