# EloGlobal - store listing kit

Everything to paste into Steamworks and Microsoft Partner Center, plus the release checklists.
Graphics are in `assets\` (made by `tools\make_assets.py`); the packages come from `tools\build_store.py`.

---

## 1. Texts

**Name:** EloGlobal
**Developer / publisher:** Lagalizer *(use your legal or registered name if the store asks for it)*
**Category:** Steam - Software › Utilities (secondary: Audio Production) · Microsoft Store - Productivity
(alternative: Utilities & tools)
**Price:** Free · no in-app purchases · no ads
**Supported languages (interface, voices, manual):** English, Portuguese (Brazil), Spanish, French, German, Italian,
Russian, Ukrainian, Polish, Turkish. Translation itself covers many more languages.

**Short description** (Steam ≤ 300 characters; MS Store "short description"):
> Talk to anyone in their language. EloGlobal translates your Discord voice calls and chats in real time - you hear
> them in your language and they hear you in theirs. Speech recognition, translation and voices all run on your PC:
> nothing is sent to the internet.

**Long description:**
> **Your voice calls, in every language - privately, on your own PC.**
>
> EloGlobal listens to the Discord app, turns what people say into text, translates it and reads it to you with a
> natural voice. When you speak, it translates you and speaks into the call in their language through a virtual audio
> cable. Subtitles show both sides of the conversation.
>
> **Everything runs on your computer.** Speech recognition (Whisper), translation (OPUS-MT) and the voices (Piper,
> Kokoro and the voices of Windows) work offline after a one-time download. No account, no subscription, no cloud
> service, no data collection. Nothing anyone says or writes leaves your PC.
>
> **Made for gaming and voice chat**
> - Hears only the Discord app - never its own voice, your game or your music - so it keeps listening while it talks.
> - One app voice that never talks over itself, speeds up a little when lines pile up, and can say who is talking.
> - Press F9 to hear the people's own voices too; push-to-talk, hotkeys and a floating subtitle window.
> - Translates Discord text chat right inside Discord, any text you highlight, and text on screen (OCR).
> - Choose the voice, speed and pitch for what you hear and for what they hear.
> - Uses an NVIDIA graphics card when you have one; runs on the processor otherwise.
> - Interface, guided tour and a read-aloud manual in 10 languages.
>
> Works with Discord. Requires the free VB-Audio Virtual Cable (third-party, installed separately) for others to hear
> your translated voice. EloGlobal is not affiliated with Discord Inc.

**Feature list** (MS Store, up to 20):
1. Real-time two-way voice translation for Discord calls
2. Everything runs on your PC - nothing is sent to the internet
3. Listens to the Discord app only - never to your game, music or its own voice
4. Natural voices for what you hear and for what they hear, with speed and pitch
5. Subtitles window that floats over your game
6. Discord chat translated inside Discord
7. Translate any highlighted text and text on screen (OCR)
8. Write in their language with one hotkey
9. Says who is talking (optional, through Discord's local connection)
10. Push-to-talk and global hotkeys
11. NVIDIA graphics card acceleration (optional)
12. Optional AI translation with your own local model (Ollama / LM Studio)
13. 10 interface languages, guided tour and read-aloud manual
14. No account, no subscription, no ads, no tracking

**Search terms / tags:** translator, voice translator, discord, real-time translation, subtitles, speech to text,
offline translator *(MS Store allows 7 terms; Steam tags: Utilities, Software, Audio, Multiplayer-friendly)*

**Screenshot captions** (1920×1080 PNGs in `assets\screenshots\`):
1. The dashboard: voice translator, chat translation and tools in one place
2. Live: both sides of the call, translated and subtitled
3. Text: Discord chat translated inside Discord, select-to-translate and OCR
4. Voices on your PC - pick the voice, speed and pitch for each direction
5. Settings: languages, sound devices, hotkeys, privacy
6. The built-in manual, read aloud in your language

**Copyright and trademark line:** © 2026 Lagalizer. "Discord" is a trademark of Discord Inc.; EloGlobal is not
affiliated with or endorsed by Discord Inc.

**Privacy policy URL:** host `PRIVACY.md` (for example GitHub Pages) and put the address in both stores and in
`eloglobal\__init__.py` (`PRIVACY_URL`).
**Support contact:** an e-mail address or support page (required by both stores).

---

## 2. System requirements

| | Minimum | Recommended |
|---|---|---|
| OS | Windows 10 version 2004 (build 19041), 64-bit | Windows 11 64-bit |
| CPU | 4 cores, x64 with AVX2 (e.g. Intel Core i5 8th gen / AMD Ryzen 3) | 6+ cores (Core i5-10400 / Ryzen 5 3600 or better) |
| RAM | 8 GB | 16 GB |
| GPU | not needed | NVIDIA GeForce GTX 1060 6 GB or newer (CUDA) for the large speech model |
| Storage | 2 GB (app 550 MB + models for one language pair) | 5 GB |
| Other | microphone, headphones, Discord desktop app, VB-Audio Virtual Cable (free, separate), internet once to download models | |

Measured on an Intel Core i5-10400F (6 cores, no NVIDIA card): see the latency notes in the release report.

---

## 3. Age rating answers

**Microsoft Store (IARC questionnaire)** - category "App" (not a game):
- Violence, blood, fear, sexual content, nudity, drugs, alcohol, tobacco, gambling, crude humour: **No**.
- Does the app let users interact or exchange content with each other? **No** - EloGlobal does not provide any
  communication service; it translates what the user already hears and sees in Discord, on the user's PC.
- Does the app share the user's location or personal information with others? **No**.
- Does the app allow purchases of digital goods? **No**.
- Unrestricted internet access (web browser / search)? **No** (only model downloads from fixed addresses).
- Expected result: **Everyone / PEGI 3 / USK 0**. If the questionnaire asks about displaying user-generated content,
  answer truthfully that translated text from the user's own Discord conversations is shown; this may raise the
  rating to "Users Interact" style descriptors, which is fine.

**Steam (content survey):** no mature content; select none of the content descriptors. "Software" product type.

---

## 4. Release checklist - Steamworks

1. Create a Steamworks account (partner.steamgames.com), complete the tax and bank forms and identity check.
2. Pay the **Steam Direct fee: USD 100** per product (not refundable; recouped only after USD 1,000 revenue - for a
   free product it is not recouped).
3. Create the app (type: Software). Note the **App ID** and the **Depot ID**.
4. Store page: name, descriptions, tags, system requirements, languages (interface + full audio for the 10
   languages), content survey, the graphics from `assets\steam\store` (header 920×430, small 462×174, main
   1232×706, vertical 748×896, page background 1438×810) and at least **5 screenshots 1920×1080** from
   `assets\screenshots`. Library assets from `assets\steam\library` (capsule 600×900, header 920×430, hero
   3840×1240, logo 1280×720) and icons from `assets\steam\icons` (shortcut icon .ico, app icon 184×184 jpg).
5. Legal: add the privacy policy URL; EULA = the text of LICENSE (EloGlobal Licence, all rights reserved) plus a note about
   THIRD_PARTY_NOTICES.txt.
6. Installation › General: launch option `EloGlobal.exe`, OS Windows, 64-bit only.
7. Build: `runtime\python.exe -s tools\build_store.py`, then in `dist\steam\scripts` replace APPID/DEPOTID (file
   names too) and upload with SteamCMD: `steamcmd +login <builder> +run_app_build ..\scripts\app_build_<APPID>.vdf +quit`.
8. Set the build live on a beta branch, install it through Steam on a clean PC and test (first start, downloads,
   a call with VB-Cable).
9. Submit the store page for review, then the build for review.
10. Publish the **Coming Soon** page - it must be visible for **at least two weeks** before release.
11. After approval, press Release yourself on the release date.

## 5. Release checklist - Microsoft Partner Center

1. Register at storedeveloper.microsoft.com - **free for individual developers** (identity check with ID and
   selfie; companies are free since May 2026 too).
2. Create the app and **reserve the name "EloGlobal"**.
3. Product identity: copy *Package/Identity/Name*, *Publisher* (CN=...) and *PublisherDisplayName* into the
   `MANIFEST` text in `tools\build_store.py`, then build: `runtime\python.exe -s tools\build_store.py`
   → `dist\msix\EloGlobal.msix` (unsigned - the Store signs it).
4. Optional local test: sign a copy with a self-signed certificate whose subject equals the Publisher, trust it,
   install, and run the Windows App Certification Kit.
5. Submission › Pricing: Free, all markets you want. Properties: category Productivity; **privacy policy URL
   required** (the app uses the microphone); system requirements as above (no special hardware; microphone).
6. Age ratings: IARC questionnaire (answers above).
7. Packages: upload the .msix. In "Submission options" explain the **runFullTrust** restricted capability: *"EloGlobal
   is a desktop app (Python + Qt) that records the Discord app's audio with Windows process loopback, plays
   translated speech into a virtual audio device chosen by the user, reads the Discord window with UI Automation and
   registers global hotkeys - these need full trust. It sends no user data anywhere."*
8. Store listing (one per language you want): descriptions, features, search terms, screenshots
   (`assets\screenshots`, at least 1, ≥1366×768), logos: 1:1 app tile icon 300×300
   (`assets\msstore\listing`), optional box art 1080×1080, poster 720×1080, super hero art 1920×1080.
9. Submit for certification (usually a few days). Watch for feedback about the restricted capability and the privacy
   policy.

## 6. Before every release

- `tools\selftest.py` and `tools\calltest.py` PASS on the dev PC.
- `tools\i18n_check.py` - no new untranslated texts.
- Build, then start `dist\EloGlobal\EloGlobal.exe` from a copy in a new folder with an empty
  `%LOCALAPPDATA%\EloGlobal` (first start, language picker, privacy notice, tour, model downloads).
- Bump `__version__` in `eloglobal\__init__.py` (the MSIX version is derived from it).
