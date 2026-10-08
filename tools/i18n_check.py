"""Which English texts of the app have no translation yet - in each of the 9 other languages.

    runtime\\python.exe -s tools\\i18n_check.py [--prune] [--write <missing.json>]

Opens the main window off screen in English, visits every tab and engine form and records every text that reaches
the screen (i18n.start_collecting), plus the texts in the source that only appear while the app runs (status
messages, dialogs: f-strings become "{0}" patterns). Then each eloglobal/locale/<code>.json is checked with the real
lookup (i18n.tr): a text counts as translated when tr() changes it or the dictionary maps it to itself.
--prune removes dictionary entries whose English text the app no longer shows.
"""
import ast
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEXT_CALLS = {"setStatus", "setText", "showMessage", "setToolTip", "setPlaceholderText", "setTitle", "setWindowTitle",
              "information", "warning", "critical", "question", "getText", "addRow", "addTab", "addAction",
              "QLabel", "QPushButton", "QCheckBox", "QGroupBox", "hint", "_muted", "_card", "emit_status", "set", "tr",
              "emit_error", "setHtml", "Step"}
SKIP_FILES = {"manual.py", "languages.py", "models_info.py", "kokoro_vocab.py"}


def static_texts() -> list[str]:
    out = []
    for f in sorted((ROOT / "eloglobal").rglob("*.py")):
        if f.name in SKIP_FILES or "locale" in f.parts:
            continue
        tree = ast.parse(f.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            fn = node.func
            name = fn.attr if isinstance(fn, ast.Attribute) else getattr(fn, "id", "")
            if name == "Step":
                out += [n.value for n in ast.walk(node) if isinstance(n, ast.Constant) and isinstance(n.value, str)]
                continue
            if name not in TEXT_CALLS:
                continue
            for arg in node.args:
                if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                    out.append(arg.value)
                elif isinstance(arg, ast.JoinedStr):
                    parts, n = [], 0
                    for v in arg.values:
                        if isinstance(v, ast.Constant):
                            parts.append(v.value)
                        else:
                            parts.append(f"{{{n}}}")
                            n += 1
                    text = "".join(parts)
                    if n and any(c.isalpha() for c in text.replace("{", "").replace("}", "")):
                        out.append(text)
    return out


def runtime_texts() -> list[str]:
    os.environ["QT_QPA_PLATFORM"] = "offscreen"
    sys.path.insert(0, str(ROOT))
    from eloglobal import i18n
    i18n.set_language("en")
    i18n.start_collecting(str(ROOT / "dist" / "_collect.json"))
    i18n.install()
    from PySide6.QtWidgets import QApplication
    app = QApplication([])
    from eloglobal.gui.about import AboutDialog, PrivacyDialog
    from eloglobal.gui.main_window import MainWindow
    from eloglobal.providers import REGISTRY
    w = MainWindow(app)
    w.show()
    for i in range(w.tabs.count()):
        w.tabs.setCurrentIndex(i)
        app.processEvents()
    for kind, panel in (("stt", w.stt_panel), ("translate", w.tr_panel), ("llm", w.ai_panel), ("tts", w.tts_panel)):
        for pid in list(REGISTRY[kind]):
            panel.set_state(pid, {})
            app.processEvents()
    AboutDialog(w)
    PrivacyDialog(w)
    from eloglobal.gui import tour
    for s in tour.steps(w):
        i18n.tr(s.title)
        i18n.tr(s.text)
        if s.action:
            i18n.tr(s.action[0])
    w._manual_stop()
    w.engine.shutdown()
    return list(i18n._collect)


def main():
    texts: dict[str, None] = {}
    for t in runtime_texts() + static_texts():
        t = t.strip("\n")
        if t and any(c.isalpha() for c in t):
            texts.setdefault(t, None)
    from eloglobal import i18n
    report = {}
    for lang in i18n.LANGUAGES[1:]:
        i18n.set_language(lang.code)
        missing = [t for t in texts if i18n.tr(t) == t and t not in i18n._table]
        report[lang.code] = missing
        print(f"{lang.code}: {len(missing)} of {len(texts)} texts not translated")
        if "--prune" in sys.argv:
            f = i18n.LOCALE_DIR / f"{lang.code}.json"
            data = json.loads(f.read_text(encoding="utf-8"))
            keep = {k: v for k, v in data.items() if k.startswith("_") or k in texts or "{0}" in k}
            print(f"   pruned {len(data) - len(keep)} unused entries")
            f.write_text(json.dumps(keep, ensure_ascii=False, indent=1), encoding="utf-8")
    if "--write" in sys.argv:
        out = Path(sys.argv[sys.argv.index("--write") + 1])
        out.write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"missing texts per language -> {out}")
    sys.stdout.flush()
    os._exit(0)


if __name__ == "__main__":
    main()
