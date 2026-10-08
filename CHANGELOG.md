# EloGlobal - changelog

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
