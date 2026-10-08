"""The user manual shown (and read aloud) in the Manual tab. Plain Markdown chapters - no tables, so the text
reads well when it is spoken - plus `speakable()`, which turns a chapter into text a voice can say.

The English chapters are below. Every other app language has eloglobal/locale/<code>.manual.md: the same chapters,
each one starting with a line "=== <chapter title>". chapters(code) returns them (English if a file is missing)."""
from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path

LOCALE_DIR = Path(__file__).resolve().parent / "locale"


@dataclass(frozen=True)
class Chapter:
    title: str
    body: str            # Markdown


CHAPTERS: list[Chapter] = [
    Chapter("1. Welcome", """
# Welcome to EloGlobal

EloGlobal is a real-time translator for Discord and any other voice chat. Everything runs on your own PC: speech
recognition, translation and the voices. Nothing anyone says or writes is sent to the internet.

- **You hear them in your language.** The app listens to what people say in Discord, writes it down,
  translates it, shows subtitles, and can read the translation to you with a natural voice.
- **They hear you in their language.** You speak into your microphone. The app translates what you said and
  speaks it into Discord through a virtual audio cable.
- **Text too.** It translates Discord messages in servers, direct messages and threads, any text you highlight
  with the mouse, and text on your screen using OCR. You can also write in their language.
- **Free and private.** No account, no subscription and no online service. The models are downloaded once and
  then work without internet.

This manual has twelve chapters. Use the Next and Previous buttons, or click a chapter in the list.
Every time you change chapter, the narrator stops the old one and reads the new one. The narrator is a voice that
runs on your PC.
"""),
    Chapter("2. First start", """
# First start

**Step 1. Open the app.** Start EloGlobal from the Start menu or from Steam. The first time, you choose the language
of the app. Everything is shown in that language, and the guide and this manual are read aloud in it. Then the
app explains what it does with other people's voices and messages: everything stays on your PC. After that, a
short guided tour shows you the first steps. It only opens this first time; you can replay it from this tab.

**Step 2. Install a virtual audio cable.** Install VB-Audio Virtual Cable from its own website, and restart the
PC. It is made by VB-Audio, not by EloGlobal, and it is free for personal use. Windows needs it to create a
virtual microphone.

**Step 3. Set up Discord.** Open Discord, then User Settings, then Voice and Video.

- Input Device: CABLE Output, from VB-Audio Virtual Cable.
- Output Device: your headphones.
- Turn off Noise Suppression, Echo Cancellation and Automatic Gain Control.

**Step 4. Set up the app.** Keep the profile Standard, everything on this PC. On the Output tab, send your
translated voice to CABLE Input. On the Input tab, keep the method Only the Discord app, and choose your real
microphone. On the Live tab, choose the languages. Then press Start, or the F5 key.

**The first time you press Start**, the app downloads what it needs, once: the speech recognition model, between 75
and 1600 megabytes depending on your PC, a translation model of about 280 megabytes for each pair of languages,
and the voices of your languages. After that, it works without internet.

**Tell the people in your call** that you use a translator, for example: I use a translator app, it runs only on my
PC and saves nothing.
"""),
    Chapter("3. The main window", """
# The main window

At the top you find the profile box. A profile stores all your settings for engines, languages and devices.
You can save, save as, delete, import and export profiles. The starter profiles are: Standard, everything on this
PC. Fastest, for slower PCs. Best quality, for a PC with an NVIDIA graphics card. And AI translation with Ollama.

Your changes are saved automatically about one second after you make them. You can switch this off in the
Settings tab.

Next to the profile box are three buttons:

- **Subtitles** shows a floating subtitle window that you can drag, resize with the mouse wheel, and
  configure with a right-click.
- **Chat** turns on the translation of Discord text messages.
- **Start** begins the voice translator. The F5 key does the same.

The tabs are: Dashboard, Live, Text, Input, Output, Speech, Translation, AI Model, Voice, Setup, Settings, Manual
and Log. The next chapters explain the ones you will use most.
"""),
    Chapter("4. Dashboard", """
# Dashboard

The Dashboard is your control panel. It is the first tab, and it shows everything at a glance.

- The **voice translator card** starts and stops live voice translation, and shows what it is doing:
  recognizing, translating or speaking.
- The **chat translation card** starts and stops the translation of Discord messages. It also has the option
  to read translated messages out loud, either one after the other, or letting a new message interrupt the
  one being read.
- The **You card** is where you set your Discord name and the language you write in.
- The **tools card** has shortcuts for highlight to translate, OCR and the subtitle window.
- The **hotkeys card** reminds you of your keyboard shortcuts.
- At the bottom, Latest translations shows the last lines that were translated.

Settings that appear in two places, for example in the Dashboard and in the Text tab, always stay in sync.
"""),
    Chapter("5. Live voice translation", """
# Live voice translation

This is the main feature. It works in two directions, and each one can be switched on separately.

**Incoming: they speak, you hear.** The app listens only to the Discord app, so it never hears its own voice, your
game or your music, and it keeps listening while it talks. It recognizes the speech, translates it, shows
subtitles, and, if you want, speaks the translation. You choose the language they speak, or Auto-detect. Choosing
the language makes recognition on your PC about twice as fast.

**Outgoing: you speak, they hear.** The app listens to your microphone, translates what you say, and speaks it into
Discord through the virtual cable. Your own voice is not sent to Discord, only the translation. The app warns you
if Discord uses your real microphone instead of the cable.

**Hear people, the F9 key.** By default you hear only the translations. While the translator runs, the app turns
Discord down in the Windows volume mixer, and gives it its volume back when you press Stop. Press F9, or the Hear
people button, to also hear their own voices. You can change the key on the Input tab.

**One voice, in order.** The translations of the call and the chat messages read aloud share one voice, so they
never talk over each other. Everything is said in the order it was spoken, and nothing is skipped: the next line is
prepared while the current one plays, and when lines pile up, the voice speaks a little faster.

**Who is talking.** The app voice can say who talked, for example the first two letters of the name, or the full
name. Choose it on the Output tab, under The app voice. In calls the names come from the Discord app itself: on the
Output tab, under Who is talking, add your own Discord application once. Chat messages always have the author's
name.

On the **Live** tab you set the languages for both directions, watch the level meters and read the transcript.
You can use a push to talk button, and the Type to speak box, where you type a line, it is translated and spoken
into Discord. The option Reply in the language they speak makes your output language follow the last language
detected from the other person.

On the **Input** tab you choose what to listen to and how your microphone starts: voice activity, push to talk, or
toggle. There is also a sensitivity control. The app recognizes its own voice when your microphone hears it, and
ignores it.

On the **Output** tab you choose where translations play, the virtual cable for your voice, the app voice, and who
is talking.

All the sound devices are also together in one place, in the Settings tab, under Sound devices.
"""),
    Chapter("6. Engines: speech, translation, AI and voice", """
# Engines

Every step of the translation runs on your PC, and you can change the settings at any time. They are saved in
your profile.

- **Speech tab.** Turns speech into text with Whisper. The model size auto is chosen for your PC: a small model on
  the processor, a big and accurate one on an NVIDIA graphics card. A bigger model is more accurate but slower.
  There is a microphone test on this tab.
- **Translation tab.** The engine OPUS-MT, from the University of Helsinki, translates in about a tenth of a
  second per sentence. Each pair of languages is downloaded once; languages without a direct model go through
  English. The button Download the models for my languages now gets them before your call. You can set the tone,
  and a glossary lets you fix how names and game terms are translated.
- **AI Model tab.** Optional. If you install Ollama or LM Studio and a model on your PC, the engine AI model on this
  PC translates with it. It understands slang and context better, but needs a fast PC or a graphics card. The app
  only talks to AI servers on your own computer or local network.
- **Voice tab.** The voices on this PC: natural Piper and Kokoro voices, and the voices built into Windows. Auto
  picks a voice for each language. A voice is downloaded once, the first time it is used. Kokoro voices sound very
  natural but need a fast PC. For more Windows voices, open Windows Settings, Time and language, Speech, Add voices.
  For each direction you can set the speed, the pitch and the volume.

Every tab has a Test button, so you can check an engine before using it.
"""),
    Chapter("7. Privacy and your data", """
# Privacy and your data

EloGlobal works only on your PC. What people say in the call, your microphone, the chat messages and the text you
translate never leave your computer. The app has no account, no analytics and no advertising.

**Other people's voices.** While the translator runs, the app hears what the people in your call say, to translate
it for you. Tell them that you use a translator. In some countries you need their consent.

**What is saved.** Your settings and profiles, and log files with technical messages, not with what people say.
Transcripts of calls are saved only if you switch them on, in the Settings tab, under Privacy and about.

**Where.** Everything the app saves is in your user folder, in App Data, Local, EloGlobal: profiles, logs,
transcripts and the downloaded models. The Settings tab has buttons to open the data folder and the models folder.

**Internet.** The app only downloads model files, once. The optional Who is talking feature logs in to Discord with
your own Discord application. Updates come from the store.

The Settings tab also shows the privacy notice again, and the About and licences window lists all the software and
models EloGlobal is built on.
"""),
    Chapter("8. Translating Discord text", """
# Translating Discord text

Press the **Chat** button, or use the chat card in the Dashboard. The app then reads the messages you see in the
Discord app, using the Windows accessibility features, like a screen reader. It needs no token, no bot, and
sends nothing anywhere.

New messages are translated and drawn on top of the original text, right inside Discord, or in a small window
next to it. You choose which in the Text tab, under Show translations. It works in servers, direct messages,
group chats, threads and forum posts, even with Discord in the background. Messages already in your language,
and your own messages, are skipped. The translations only show while Discord is the active window, so they never
cover your game.

**Reading aloud.** Only new messages are read aloud. Messages you scroll back to, edited messages, and old messages
are translated on screen but never read out. Chat messages share the app voice with the call translations, so the
two never talk at the same time.

The Text tab has more tools:

- **Highlight to translate.** Select text, or double-click a word, and a popup with the translation appears
  next to the mouse.
- **Control Alt T** translates the current selection in any app.
- **Control Alt Y** replaces what you typed in Discord's message box with its translation into the language used
  in that chat.
- **Write in their language.** Type in the Text tab, then copy, paste into Discord, or send.
- **Control Alt O** lets you drag a box over any part of the screen. The app reads the text with OCR and shows
  the translation on top of it. It can repeat every few seconds.
- **Copied text.** Optionally translate everything you copy.

You can change every hotkey in the Text tab. For OCR in other alphabets, such as Russian or Japanese, add that
language in Windows Settings.
"""),
    Chapter("9. Subtitles and transcripts", """
# Subtitles and transcripts

The **subtitle window** floats above your game or Discord. Drag it to move it. Use the mouse wheel to resize it.
Right-click for options, such as how many lines to show, whether to show the original text, and the background.
In Settings you can change its text size and font.

A conversation can be saved as a **transcript**. This is off by default, because transcripts contain other
people's words. Switch it on in the Output tab or in Settings. Transcripts are saved in the data folder, under
transcripts.

The Log tab shows what the app is doing in real time. It also has buttons to open the logs, the transcripts and
the data folder. If something goes wrong, the log is the first place to look.

The status bar at the bottom shows the delay of each stage: speech recognition, translation and voice, so you
can see which step is slow.
"""),
    Chapter("10. Settings and about", """
# Settings and about

The **Settings** tab sets the language of the app. After you change it, the app restarts in the new language.
It also has all the sound devices in one place: what the app listens to, your microphone, where translations
play and where your translated voice goes.

It controls how the app looks: the theme, dark or light, the font, and the text size of the app
and of the translations shown inside Discord, in the small chat window and in the popups. It also has all the
hotkeys in one place, a switch to keep the window above other windows, and buttons to reset the window positions
and open the data, models and log folders.

The switch Save changes automatically keeps your profile saved about one second after every change. It is on by
default.

**Privacy and about.** The switch for transcripts, the privacy notice, and the About and licences window, with the
licence of EloGlobal and the list of every component it uses.

**Updates** come from the store you installed EloGlobal from, the Microsoft Store or Steam. Your settings,
profiles and downloaded models are kept.
"""),
    Chapter("11. Troubleshooting", """
# Troubleshooting

**Nobody hears my translation.** In Discord, the input device must be CABLE Output. In the app, the Output tab
must send to CABLE Input. Check that Noise Suppression is off in Discord.

**The app hears nothing.** On the Input tab, check the method. With Only the Discord app, Discord must be open.
With loopback, the device must be the one Discord plays to. Look at the level meters on the Live tab. If they do
not move, the setting is wrong.

**My own translation is heard twice, or the app translates itself.** Use the method Only the Discord app on the
Input tab, and wear headphones.

**Discord is silent.** This is on purpose while the translator runs: press F9 to hear the people too. If EloGlobal
was closed abruptly, open it once and it gives Discord its volume back, or raise Discord in the Windows volume
mixer.

**People hear my real voice.** In Discord, the input device must be CABLE Output, not your microphone. The app
shows a warning when Discord uses your real microphone.

**It is slow.** On the Live tab, choose the language they speak instead of Auto-detect. On the Speech tab, choose a
smaller model, or use an NVIDIA graphics card. Kokoro voices are slow on many processors: pick a Piper or Windows
voice on the Voice tab.

**No voice for my language.** Add a Windows voice: Windows Settings, Time and language, Speech, Add voices. Then
press Reload voice list on the Voice tab.

**A download fails.** Check your internet connection and press Start again; the download continues where it
stopped.

**Still stuck.** Open the Log tab and the logs folder. The log helps when you report a problem through the store
page.
"""),
    Chapter("12. About this manual", """
# About this manual

You are reading the manual built into EloGlobal. The narrator is a voice that runs on your PC, in the language of
the app. It works offline and does not send anything anywhere.

- **Next and Previous** move between chapters. The narrator stops reading the old chapter and starts the new
  one, and the new text is shown at the same time.
- **Read aloud** turns the narrator on or off. When it is off, the manual is just text.
- **Read again** starts the current chapter from the beginning.
- **Stop** silences the narrator.
- **Voice** and **Speed** let you change how it sounds. You can pick any voice of your language on this PC, or one
  to download.
- **Replay the guided tour** shows the first steps again.

The narrator is silent when you leave this tab, and it never starts by itself while you are using the
translator.

That is the end of the manual. Enjoy EloGlobal!
"""),
]


_cache: dict[str, list[Chapter]] = {}


def chapters(code: str) -> list[Chapter]:
    """The manual in the language `code` (English when there is no translation)."""
    if code in _cache:
        return _cache[code]
    out = CHAPTERS
    f = LOCALE_DIR / f"{code}.manual.md"
    if code != "en" and f.is_file():
        parts = re.split(r"^=== (.+)$", f.read_text(encoding="utf-8"), flags=re.M)
        found = [Chapter(parts[k].strip(), parts[k + 1]) for k in range(1, len(parts) - 1, 2)]
        if found:
            out = found
    _cache[code] = out
    return out


# --------------------------------------------------------------------------- text for the voice
_LINK = re.compile(r"\[([^\]]+)\]\([^)]*\)")
_MARKS = re.compile(r"[*_`#>]+")
_COMBO = re.compile(r"(?<=\w)\+(?=\w)")


def speakable(md: str) -> str:
    """Markdown -> plain sentences for a speech engine: no symbols, 'Ctrl+Alt+T' -> 'Control Alt T'.
    Lines that are only wrapped for the editor are joined, so the voice does not pause in the middle of a sentence."""
    items: list[str] = []            # one entry per heading / bullet / paragraph
    cur = ""
    for raw in md.strip().splitlines():
        line = raw.strip()
        starts_new = line.startswith("#") or bool(re.match(r"^[-*]\s", line))
        if not line or starts_new:
            if cur:
                items.append(cur)
            cur = ""
        if not line:
            continue
        line = _LINK.sub(r"\1", line)
        line = re.sub(r"^[-*]\s+", "", line)
        cur = f"{cur} {line}".strip() if cur and not starts_new else line
    if cur:
        items.append(cur)
    out = []
    for it in items:
        it = _MARKS.sub("", it).strip()
        if it:
            out.append(it if it[-1] in ".!?:;" else it + ".")
    text = " ".join(out)
    text = text.replace("Ctrl", "Control").replace("Strg", "Steuerung").replace("\\", " ")
    text = _COMBO.sub(" ", text)
    text = "".join(" " if unicodedata.category(ch)[0] in "SC" else ch for ch in text)   # emojis, arrows (any alphabet stays)
    return re.sub(r"\s+", " ", text).strip()
