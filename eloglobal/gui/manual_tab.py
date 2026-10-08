"""'Manual' tab: the user manual in the app language, chapter by chapter, read aloud by a voice of this PC in that
language (a Piper / Kokoro voice, or a voice built into Windows).

Moving to another chapter - with Next / Previous or by clicking the list - cuts the voice that was reading the
old chapter, shows the new chapter and starts reading it. The narrator is silent whenever the tab is not visible."""
from __future__ import annotations

from PySide6.QtCore import QObject, Qt, Signal
from PySide6.QtWidgets import (QCheckBox, QHBoxLayout, QLabel, QListWidget, QPushButton, QSlider, QTextBrowser,
                               QVBoxLayout, QWidget)

from .. import config, i18n, localvoice
from ..manual import chapters, speakable
from ..natural import NaturalNarrator
from .widgets import DataCombo, run_async


class _Bridge(QObject):
    """Lets the voice threads report a problem to the window thread: (voice, message)."""
    failed = Signal(str, str)


class ManualTabMixin:
    """Mixed into MainWindow. Needs: tabs, state, setStatus."""

    # ------------------------------------------------------------------ build
    def _build_manual_tab(self) -> QWidget:
        saved = self.state.get("manual") or {}
        self._bridge = _Bridge()
        self._bridge.failed.connect(self._manual_voice_failed)
        self._natural = NaturalNarrator(on_error=self._bridge.failed.emit)
        self._manual_index = 0
        self._chapters = chapters(i18n.current().code)
        w = QWidget()
        root = QHBoxLayout(w)

        self.manual_list = QListWidget()
        self.manual_list.setFixedWidth(250)
        for ch in self._chapters:
            self.manual_list.addItem(i18n.tr(ch.title))
        left = QVBoxLayout()
        left.addWidget(self.manual_list, 1)
        replay = QPushButton("▶ Replay the guided tour")
        replay.setToolTip("Show the first steps again, one at a time")
        replay.clicked.connect(self._manual_replay_tour)
        left.addWidget(replay)
        root.addLayout(left)

        right = QVBoxLayout()
        self.manual_view = QTextBrowser()
        self.manual_view.setOpenExternalLinks(True)
        right.addWidget(self.manual_view, 1)

        nav = QHBoxLayout()
        self.manual_prev = QPushButton("◀ Previous")
        self.manual_prev.setToolTip("Previous chapter - the voice stops the current one and reads that one")
        self.manual_next = QPushButton("Next ▶")
        self.manual_next.setObjectName("primary")
        self.manual_next.setToolTip("Next chapter - the voice stops the current one and reads that one")
        self.manual_pos = QLabel()
        nav.addWidget(self.manual_prev)
        nav.addWidget(self.manual_next)
        nav.addWidget(self.manual_pos)
        nav.addStretch(1)
        right.addLayout(nav)

        voice = QHBoxLayout()
        self.manual_speak = QCheckBox("🔊 Read aloud")
        self.manual_speak.setChecked(bool(saved.get("speak", True)))
        again = QPushButton("🔁 Read again")
        stop = QPushButton("⏹ Stop")
        self.manual_voice = DataCombo(self._natural.voices())
        self.manual_voice.setMinimumWidth(300)
        self.manual_speed = QSlider(Qt.Horizontal)
        self.manual_speed.setRange(-6, 6)
        self.manual_speed.setValue(int(saved.get("rate", 0)))
        self.manual_speed.setFixedWidth(110)
        self.manual_speed.setToolTip("Speed of the voice")
        voice.addWidget(self.manual_speak)
        voice.addWidget(again)
        voice.addWidget(stop)
        voice.addSpacing(12)
        voice.addWidget(QLabel("Voice"))
        voice.addWidget(self.manual_voice, 1)
        voice.addWidget(QLabel("Speed"))
        voice.addWidget(self.manual_speed)
        right.addLayout(voice)
        self.manual_note = QLabel("")
        self.manual_note.setWordWrap(True)
        self.manual_note.setObjectName("muted")
        right.addWidget(self.manual_note)
        root.addLayout(right, 1)

        self.manual_list.currentRowChanged.connect(lambda i: i >= 0 and self._manual_goto(i))
        self.manual_prev.clicked.connect(lambda: self._manual_goto(self._manual_index - 1))
        self.manual_next.clicked.connect(lambda: self._manual_goto(self._manual_index + 1))
        again.clicked.connect(lambda: self._manual_read())
        stop.clicked.connect(self._manual_stop)
        self.manual_speak.toggled.connect(self._manual_speak_toggled)
        self.manual_voice.changed.connect(self._manual_voice_changed)
        self.manual_speed.valueChanged.connect(lambda _v: self._manual_save())
        pick = (saved.get("voices") or {}).get(i18n.current().code) or ""
        if not localvoice.get(pick or "-"):
            pick = self._natural.default_voice()
        self.manual_voice.blockSignals(True)
        self.manual_voice.setValue(pick)
        self.manual_voice.blockSignals(False)
        if not self._natural.available:
            self.manual_note.setText("No voice for this language is on this PC yet - the manual is shown as text. "
                                     "Add a Windows voice: Windows Settings → Time & language → Speech.")
        self._natural.warm_up(self._manual_current_voice())      # load the voice now, while the app starts
        self.manual_tab_widget = w
        self._manual_show(0)
        return w

    # ------------------------------------------------------------------ narrator
    def _manual_current_voice(self) -> str:
        return self.manual_voice.value() or ""

    def _manual_read(self):
        """Read the chapter on screen from its beginning (the previous reading is cut first)."""
        voice = self._manual_current_voice()
        v = localvoice.get(voice) if voice else None
        self._manual_stop()
        if v is None:
            return
        if not localvoice.installed(v):
            self._manual_download(v)
            return
        self.manual_note.setText("")
        self._natural.speak(speakable(self._chapters[self._manual_index].body), voice, self.manual_speed.value())

    def _manual_download(self, v):
        """A voice from the list that is not on this PC yet: download it once, then read."""
        self.manual_note.setText(f"Downloading the voice {v.name} (about {v.size_mb} MB, only once)…")

        def done(_r, err):
            if err:
                self.manual_note.setText(f"⚠ The voice could not be downloaded: {err}")
                return
            self.manual_voice.set_items(self._natural.voices())
            self.manual_voice.blockSignals(True)
            self.manual_voice.setValue(v.id)
            self.manual_voice.blockSignals(False)
            self.manual_note.setText("")
            if self.manual_speak.isChecked() and self._manual_tab_visible():
                self._manual_read()
        run_async(lambda: localvoice.download(v), done)

    def _manual_voice_failed(self, voice: str, _msg: str):
        """The voice failed: read with a Windows voice of the language instead, if there is one."""
        if not self.manual_speak.isChecked() or not self._manual_tab_visible():
            return
        code = i18n.current().code
        wins = [v for v in localvoice.windows_voices() if v.lang.split("-")[0] == code and v.id != voice]
        if wins:
            self.manual_note.setText("That voice is not working - reading with a Windows voice instead.")
            self._natural.speak(speakable(self._chapters[self._manual_index].body), wins[0].id,
                                self.manual_speed.value())
        else:
            self.manual_note.setText("That voice is not working right now - the manual is shown as text.")

    def _manual_stop(self):
        self._natural.stop()

    # ------------------------------------------------------------------ navigation
    def _manual_show(self, i: int):
        self._manual_index = i
        self.manual_view.setMarkdown(self._chapters[i].body.strip())
        self.manual_view.verticalScrollBar().setValue(0)
        self.manual_pos.setText(f"   Chapter {i + 1} of {len(self._chapters)}")
        self.manual_prev.setEnabled(i > 0)
        self.manual_next.setEnabled(i < len(self._chapters) - 1)
        self.manual_list.blockSignals(True)
        self.manual_list.setCurrentRow(i)
        self.manual_list.blockSignals(False)

    def _manual_goto(self, i: int):
        i = max(0, min(len(self._chapters) - 1, i))
        changed = i != self._manual_index
        self._manual_stop()                      # the old chapter is cut at once
        self._manual_show(i)                     # the new chapter is shown...
        if changed and self.manual_speak.isChecked() and self._manual_tab_visible():
            self._manual_read()                  # ...and read

    def _manual_tab_visible(self) -> bool:
        return self.tabs.currentWidget() is getattr(self, "manual_tab_widget", None)

    # ------------------------------------------------------------------ settings, hooks
    def _manual_speak_toggled(self, on: bool):
        if on and self._manual_tab_visible():
            self._manual_read()
        elif not on:
            self._manual_stop()
        self._manual_save()

    def _manual_voice_changed(self):
        voice = self._manual_current_voice()
        self._natural.warm_up(voice)
        if voice and self.manual_speak.isChecked() and self._manual_tab_visible():
            self._manual_read()
        self._manual_save()

    def _manual_save(self):
        voices = dict((self.state.get("manual") or {}).get("voices") or {})
        voices[i18n.current().code] = self._manual_current_voice()       # one voice per language
        self.state["manual"] = {"speak": self.manual_speak.isChecked(), "rate": self.manual_speed.value(),
                                "voices": voices}
        try:
            config.save_app_state(self.state)
        except Exception:  # noqa: BLE001
            pass

    def _manual_tab_changed(self):
        """Called by MainWindow when the user changes tab: read when the Manual opens, be silent when it closes."""
        if getattr(self, "manual_tab_widget", None) is None:
            return
        if self._manual_tab_visible():
            if self.manual_speak.isChecked():
                self._manual_read()
        else:
            self._manual_stop()

    def _manual_replay_tour(self):
        self._manual_stop()
        if hasattr(self, "start_tour"):
            self.start_tour()

    def _manual_close(self):
        if hasattr(self, "_natural"):
            self._manual_stop()
