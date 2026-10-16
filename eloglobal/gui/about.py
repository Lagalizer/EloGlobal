"""About / licences window and the privacy notice (shown once, on the first start)."""
from __future__ import annotations

from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import (QDialog, QHBoxLayout, QLabel, QPlainTextEdit, QPushButton, QTabWidget, QTextBrowser,
                               QVBoxLayout)

from .. import APP_NAME, DONATE_URL, PRIVACY_URL, __version__, config, updater
from ..i18n import no_translate

PRIVACY_TEXT = (
    "<p><b>EloGlobal works only on this PC.</b> It listens to the Discord app and to your microphone, turns speech "
    "into text, translates it and speaks the translation - all on your computer. Nothing anyone says or writes is "
    "sent to the internet, to us or to anyone else.</p>"
    "<p><b>Other people's voices and messages are processed.</b> While the translator runs, the app hears what the "
    "people in your call say, and the chat translation reads the messages shown in Discord, to translate them for "
    "you.</p>"
    "<p><b>Tell the people in the call.</b> Let them know that you use a translator that listens to the call, for "
    "example: “I use a translator app - it runs only on my PC and saves nothing.” In some countries you need their "
    "consent.</p>"
    "<p><b>Nothing is kept unless you want.</b> Saving transcripts is off (Settings → Privacy &amp; about). The log "
    "files contain technical messages, not what people say.</p>"
    "<p><b>Downloads.</b> Speech, translation and voice models are downloaded once from their publishers "
    "(Hugging Face, the OPUS-MT server of the University of Helsinki, GitHub). Only the file is requested; nothing "
    "about you or your calls is sent.</p>")


def _read(name: str) -> str:
    for p in (config.ROOT / name, config.ROOT / "licenses" / name):
        if p.is_file():
            return p.read_text(encoding="utf-8", errors="replace")
    return ""


def _open_privacy_policy():
    if PRIVACY_URL:
        QDesktopServices.openUrl(QUrl(PRIVACY_URL))
    elif (config.ROOT / "PRIVACY.md").is_file():
        QDesktopServices.openUrl(QUrl.fromLocalFile(str(config.ROOT / "PRIVACY.md")))


class PrivacyDialog(QDialog):
    def __init__(self, parent=None, first_run: bool = True):
        super().__init__(parent)
        self.setWindowTitle(f"{APP_NAME} - Privacy")
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.setMinimumWidth(560)
        v = QVBoxLayout(self)
        head = QLabel("🔒  Before you start: your privacy and other people's")
        head.setObjectName("title")
        head.setWordWrap(True)
        v.addWidget(head)
        body = QLabel(PRIVACY_TEXT)
        body.setWordWrap(True)
        body.setTextFormat(Qt.RichText)
        v.addWidget(body)
        row = QHBoxLayout()
        pol = QPushButton("Full privacy policy")
        pol.clicked.connect(_open_privacy_policy)
        row.addWidget(pol)
        row.addStretch(1)
        ok = QPushButton("I understand  ▶" if first_run else "Close")
        ok.setObjectName("primary")
        ok.setDefault(True)
        ok.clicked.connect(self.accept)
        row.addWidget(ok)
        v.addLayout(row)


class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"About {APP_NAME}")
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.resize(820, 620)
        v = QVBoxLayout(self)
        head = no_translate(QLabel(f"{APP_NAME} {__version__}"))
        head.setObjectName("title")
        v.addWidget(head)
        info = QLabel("Real-time voice and chat translator for voice calls. Works with Discord - not affiliated with, "
                      "endorsed or sponsored by Discord Inc. “Discord” is a trademark of Discord Inc.<br>"
                      "© 2026 Lagalizer. EloGlobal is free to use, but it may not be sold, copied or changed - "
                      "see the Licence tab. It includes open source software and models made by others - "
                      "see the list below.")
        info.setWordWrap(True)
        info.setTextFormat(Qt.RichText)
        v.addWidget(info)
        tabs = QTabWidget()
        lic = no_translate(QPlainTextEdit(_read("LICENSE") or "LICENSE"))
        lic.setReadOnly(True)
        tabs.addTab(lic, "Licence")
        third = no_translate(QPlainTextEdit(_read("THIRD_PARTY_NOTICES.txt") or "THIRD_PARTY_NOTICES.txt"))
        third.setReadOnly(True)
        third.setLineWrapMode(QPlainTextEdit.NoWrap)
        tabs.addTab(third, "Third-party software && models")
        priv = QTextBrowser()
        priv.setHtml(PRIVACY_TEXT)
        tabs.addTab(priv, "Privacy")
        v.addWidget(tabs, 1)
        row = QHBoxLayout()
        b = QPushButton("Open licences folder")
        b.clicked.connect(lambda: QDesktopServices.openUrl(QUrl.fromLocalFile(str(config.ROOT / "licenses"))))
        row.addWidget(b)
        b = QPushButton("Full privacy policy")
        b.clicked.connect(_open_privacy_policy)
        row.addWidget(b)
        if DONATE_URL and updater.repo():
            b = QPushButton("♥ Donate")
            b.clicked.connect(lambda: QDesktopServices.openUrl(QUrl(DONATE_URL)))
            row.addWidget(b)
        row.addStretch(1)
        close = QPushButton("Close")
        close.clicked.connect(self.accept)
        row.addWidget(close)
        v.addLayout(row)
