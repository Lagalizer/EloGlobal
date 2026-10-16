# EloGlobal - changelog

## Unreleased

- **Licence**: EloGlobal is no longer MIT. The new LICENSE (EloGlobal Licence) keeps all rights with Lagalizer: free
  to download and use, but no selling, copying, redistributing or modifying without written permission. Third-party
  components keep their own licences. 1.0.0 and 1.0.1 remain MIT. About window text updated in all 10 languages.
- **Fixes**: Stop + Start while the engines load no longer starts the audio twice; chat translation Stop + Start
  works while the old reader is still busy; no duplicate clipboard watchers and no popups for the app's own
  clipboard use; echo check can't crash during Stop.
- **Safer**: updates are checked against GitHub's SHA-256 checksum; local AI requests refuse redirects and proxies;
  settings, secrets and the Discord-volume file are written atomically.

## 1.0.1 - 2026-10-15 - text-only voice translation, GitHub download with updates

- **Text only in voice calls**: Dashboard → *Speak the translations* (same as Live → *Speak translation*) off = the
  translations of the others are only shown as text (the subtitles window opens; with names when *Who is talking*
  is set up) and you hear the people with their own voices - Discord is no longer turned down and *Hear people* is
  greyed out. Turning it off while a translation is being said stops it. Your own translated voice is unchanged.
  Translated into the 9 other app languages.
- **GitHub download**: `tools/build_store.py` also makes `dist/github/EloGlobal-<version>-windows-x64.zip` (the app
  folder + `update.json`). Only that copy has *Settings → Updates* (`eloglobal/updater.py`): it asks GitHub for the
  newest release (at start-up, can be turned off, and on request), downloads its zip into the data folder, and a
  small script copies it over the app folder after EloGlobal closes, then starts it again (user data, downloaded
  models and `portable.txt` are kept; log in `logs/update.log`). Microsoft Store and Steam builds have no
  `update.json` and stay updated by their store. PRIVACY.md lists the new connection.

## 1.0.0 - 2026-10-08 - first store edition (from Dizcord 0.6.0, GitHub edition)

**New name and look.** Dizcord becomes EloGlobal ("elo" = link): new logo, icon and teal/amber theme (no Discord
name, logo or colours); package `dizcord` -> `eloglobal`; EloGlobal.exe launcher; all 10 languages, the tour and the
manual updated.

**Everything on the PC.** Removed every online engine and its code: OpenAI-compatible, Groq, Deepgram, ElevenLabs,
Azure, Google Cloud, DeepL, LibreTranslate, MyMemory, Anthropic, the free Google translator and Edge voices; the API
keys tab and key store; the GitHub updater; `requests`, `edge-tts`, `anthropic`, `argostranslate`, `piper-tts`.
- Speech: Whisper (faster-whisper), model size `auto` picked from the hardware (GPU memory / CPU cores); optional
  in-app download of NVIDIA's cuBLAS/cuDNN for the graphics card (`eloglobal/gpu.py`).
- Translation: OPUS-MT (CC-BY 4.0) - the official Marian models are downloaded once and converted on the PC to
  CTranslate2 int8 (`eloglobal/opusmt.py`); pairs without a model go through English. ~0.12 s per sentence on CPU.
- Voices (`eloglobal/localvoice.py`): own MIT runners for Piper and Kokoro on ONNX Runtime; eSpeak NG runs as a
  separate program (persistent pipe, sentinel-delimited); Windows OneCore voices through WinRT (native speaking
  rate). Only voices trained from scratch with commercial-use licences; the best German/French MLS speakers were
  picked by Whisper word error rate and pitch.
- Manual / tour narrator uses the same local voices; SAPI module removed.
- Optional AI translation only through servers on this PC / LAN (Ollama, LM Studio); other addresses are refused.

**Store readiness.**
- User data in `%LOCALAPPDATA%\EloGlobal` (MSIX: the package's LocalCache folder, shown in Explorer);
  `portable.txt` keeps the old in-folder layout for development.
- First-run privacy notice; transcripts off by default; no conversation text in the log files; the Discord RPC
  secret is encrypted with DPAPI; PRIVACY.md.
- LICENSE (MIT), THIRD_PARTY_NOTICES.txt, About & licences window, licence texts of every package in `licenses\`,
  eSpeak NG source included.
- `tools/build_store.py`: ready folder with its own Python 3.13 (pinned `requirements-lock.txt`, installed without
  dependency resolution - no PyAV/FFmpeg GPL), stripped Qt tools/QML and ASIO PortAudio builds, pre-compiled .pyc,
  Steam depot layout + SteamPipe scripts, MSIX (runFullTrust + microphone) built with makeappx/makepri from
  Microsoft.Windows.SDK.BuildTools.
- `tools/make_assets.py`: SVG logo + every Steam / Microsoft Store graphic and MSIX logo in all scales.
- `main.py --smoke/--shots/--size/--demo/--lang` for automated GUI checks and screenshots; `tools/i18n_check.py`.
- Echo filter also matches letter by letter (plainer voices are recognised with spelling mistakes).
