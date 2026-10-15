# EloGlobal

**Real-time voice and chat translator for voice calls - works with Discord.** Hear everyone in your language, speak
in theirs. Everything runs on your own Windows PC: speech recognition, translation and voices. Nothing anyone says or
writes is sent to the internet.

## Download

**[Latest release](https://github.com/Lagalizer/EloGlobal/releases/latest)** → `EloGlobal-<version>-windows-x64.zip`.
Unzip it anywhere (e.g. `C:\Games\EloGlobal`) and run `EloGlobal.exe` - nothing to install, Python is included.
Windows 10 2004 or newer, 64-bit. New versions: *Settings → Updates* downloads and installs them (your settings and
models are kept).

## About

This is the **store edition** (Microsoft Store, Steam and the zip above). It grew out of Dizcord, the GitHub edition, and differs from
it in four ways: it uses only engines that run on the PC, it ships as a ready folder with its own Python (nothing to
install), it keeps user data in `%LOCALAPPDATA%\EloGlobal`, and it uses only components whose licences allow
commercial distribution.

## Features

- **You hear them in your language** - listens to the Discord app only (never its own voice, your game or music),
  recognises speech with Whisper, translates with OPUS-MT and reads it to you; **F9** lets you hear the people too.
- **They hear you in theirs** - your microphone is translated and spoken into Discord through a virtual cable
  ([VB-Audio Virtual Cable](https://vb-audio.com/Cable/), installed by the user - not included).
- **One app voice** - call translations and chat messages share one queue, never overlap, catch up when they pile up;
  optional "who is talking" names through Discord's local RPC.
- **Text** - Discord chat translated inside Discord (Windows UI Automation), select-to-translate, screen OCR, write
  in their language.
- **10 UI languages**, guided tour and a manual read aloud by a voice of the PC.

## Engines (all local)

| Step | Engine | Licence |
|---|---|---|
| Speech recognition | Whisper via faster-whisper / CTranslate2, CPU or NVIDIA GPU (size picked for the PC) | MIT |
| Translation | OPUS-MT (University of Helsinki), converted to CTranslate2 int8 on the PC; optional local LLM (Ollama / LM Studio) | CC-BY 4.0 |
| Voices | Piper voices trained from scratch (PD / CC0 / CC-BY), Kokoro-82M, Windows voices | see THIRD_PARTY_NOTICES.txt |
| Phonemes | eSpeak NG 1.52 as a separate program (GPL-3, source included) | GPL-3.0 (separate) |

EloGlobal itself is **MIT** (see [LICENSE](LICENSE)); every component is listed in
[THIRD_PARTY_NOTICES.txt](THIRD_PARTY_NOTICES.txt). Privacy policy: [PRIVACY.md](PRIVACY.md).

## Development

```
setup.bat                                   builds runtime\ (dev Python + packages from requirements*.txt)
EloGlobal.bat / EloGlobal-debug.bat         start the app from source
runtime\python.exe -s tools\selftest.py     both directions: cable -> Whisper -> OPUS-MT -> voice  (PASS/FAIL)
runtime\python.exe -s tools\calltest.py     a pretend call: order, no echo, one voice, latency per sentence
runtime\python.exe -s tools\i18n_check.py   texts without a translation in each of the 9 other languages
runtime\python.exe -s tools\make_assets.py  logo, icons and every store graphic -> assets\
runtime\python.exe -s tools\build_store.py  ready app folder + Steam depot + MSIX -> dist\
```

`main.py --lang pt --smoke 5 --shots <folder>` opens the window, saves a picture of every tab and quits (tests,
store screenshots). A `portable.txt` next to `main.py` keeps data and models in the app folder.

Store submission: see [STORE_LISTING.md](STORE_LISTING.md).
