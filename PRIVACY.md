# EloGlobal - Privacy Policy

*Last updated: 15 October 2026 · applies to EloGlobal 1.0 for Windows (Microsoft Store, Steam, GitHub download)*

EloGlobal is a voice and chat translator for voice calls that runs **entirely on your own computer**. This policy
explains what the app does with your data and with the data of the people you talk to.

## The short version

- **Nothing you say, write or hear is sent to us or to anyone else.** Speech recognition, translation and the
  voices run on your PC.
- **We collect no personal data**: no account, no analytics, no telemetry, no advertising, no crash reports.
- The app **only connects to the internet to download model files** (once) - and, if you turn on the optional
  "Who is talking" feature, to log in to Discord with your own Discord application. The copy downloaded from
  GitHub also asks GitHub for the newest version number (can be turned off).
- Everything the app stores stays in `%LOCALAPPDATA%\EloGlobal` on your PC, and you can delete it at any time.

## What the app processes, and where

| Data | Why | Where it goes |
|---|---|---|
| Audio of the Discord app (what people in your call say) | To recognise the speech and translate it for you | Processed in memory on your PC, never stored, never sent |
| Your microphone | To translate what you say and speak it into the call | Processed in memory on your PC, never stored, never sent |
| Discord chat messages shown on your screen (when chat translation is on) | To translate them | Read from the Discord window through Windows accessibility on your PC, never sent |
| Text you highlight or areas you select for OCR | To translate them | Processed on your PC (Windows' built-in OCR), never sent |
| Transcripts of calls | Only if you turn on "Save transcripts" (off by default) | Saved on your PC in `%LOCALAPPDATA%\EloGlobal\transcripts` |
| Settings, profiles, logs | To remember your choices and to help you find problems | Saved on your PC in `%LOCALAPPDATA%\EloGlobal`. Logs contain technical messages, not what people say |
| Discord application secret (optional "Who is talking" feature) | To log in to Discord's local connection | Saved on your PC, encrypted for your Windows user (DPAPI) |

**Other people's voices and messages.** While the translator runs, EloGlobal processes what the people in your call
say and the chat messages you see, so that it can translate them for you. This happens only on your PC and nothing
is kept unless you turn on transcripts. Please **tell the people in your call** that you use a translator; in some
countries you need their consent to record or process a conversation. The app shows this reminder the first time
it starts.

## Internet connections

EloGlobal makes only these connections:

1. **Model downloads** (once per model): speech recognition models from Hugging Face (`huggingface.co`),
   translation models from the OPUS-MT release server of the University of Helsinki (`object.pouta.csc.fi`), and
   voices from Hugging Face and GitHub. Only the file is requested; like any download, the server sees your IP
   address. No information about you or your calls is sent.
2. **Optional - "Who is talking"**: if you enter your own Discord application ID and turn this on, the app asks
   Discord (`discord.com`) for a login token for *your* application, and then talks to the Discord app on your PC
   through its local connection to learn who is speaking. No audio or messages are sent.
3. **Optional - your own AI server**: if you choose the "AI model on this PC" translation engine, the app sends
   the text to translate to the AI server *you* run on your computer or local network (Ollama, LM Studio). The app
   refuses addresses that are not on your computer or local network.

4. **Updates - only the copy downloaded from GitHub**: when EloGlobal starts (*Settings → Updates → Check for
   updates when EloGlobal starts*, can be turned off) or when you click *Check for updates*, the app asks GitHub
   (`api.github.com`) for the newest release of EloGlobal, and downloads it from GitHub only when you click
   *Update*. Nothing about you is sent; GitHub sees your IP address, as with any download.

The copies from the Microsoft Store and Steam have no updater of their own - they are updated by that store, under
the store's privacy policy.

## Children

EloGlobal is not directed at children and collects no data from anyone.

## Your control

- Turn transcripts on or off in *Settings → Privacy & about*.
- Delete everything the app stored: uninstall the app and delete the folder `%LOCALAPPDATA%\EloGlobal`
  (*Settings → Open data folder*). When installed from the Microsoft Store, Windows removes the app's data when you
  uninstall it.

## Changes

If this policy changes, the new version will be published at this address with a new date.

## Contact

Questions about privacy: write to the support contact shown on EloGlobal's store page (Microsoft Store or
Steam), or open an issue at github.com/Lagalizer/EloGlobal.
