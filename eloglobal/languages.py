"""Language table + per-provider code mapping.

Codes are ISO-639-1 with a few regional variants (pt-PT, en-GB, zh-TW, es-MX).
"auto" means "detect automatically".
"""

AUTO = "auto"

# code: (english name, native name, locale tag (Windows voices), ISO 639-3 code (translation models))
LANGUAGES = {
    "en":    ("English (US)",          "English",          "en-US", "eng"),
    "en-GB": ("English (UK)",          "English (UK)",     "en-GB", "eng"),
    "pt":    ("Portuguese (Brazil)",   "Português (BR)",   "pt-BR", "por"),
    "pt-PT": ("Portuguese (Portugal)", "Português (PT)",   "pt-PT", "por"),
    "es":    ("Spanish (Spain)",       "Español",          "es-ES", "spa"),
    "es-MX": ("Spanish (Mexico)",      "Español (MX)",     "es-MX", "spa"),
    "fr":    ("French",                "Français",         "fr-FR", "fra"),
    "de":    ("German",                "Deutsch",          "de-DE", "deu"),
    "it":    ("Italian",               "Italiano",         "it-IT", "ita"),
    "nl":    ("Dutch",                 "Nederlands",       "nl-NL", "nld"),
    "ru":    ("Russian",               "Русский",          "ru-RU", "rus"),
    "uk":    ("Ukrainian",             "Українська",       "uk-UA", "ukr"),
    "pl":    ("Polish",                "Polski",           "pl-PL", "pol"),
    "tr":    ("Turkish",               "Türkçe",           "tr-TR", "tur"),
    "ja":    ("Japanese",              "日本語",            "ja-JP", "jpn"),
    "ko":    ("Korean",                "한국어",            "ko-KR", "kor"),
    "zh":    ("Chinese (Simplified)",  "中文 (简体)",       "zh-CN", "zho"),
    "zh-TW": ("Chinese (Traditional)", "中文 (繁體)",       "zh-TW", "zho"),
    "ar":    ("Arabic",                "العربية",          "ar-SA", "ara"),
    "hi":    ("Hindi",                 "हिन्दी",            "hi-IN", "hin"),
    "bn":    ("Bengali",               "বাংলা",            "bn-IN", "ben"),
    "ur":    ("Urdu",                  "اردو",             "ur-PK", "urd"),
    "ta":    ("Tamil",                 "தமிழ்",            "ta-IN", "tam"),
    "fa":    ("Persian",               "فارسی",            "fa-IR", "fas"),
    "he":    ("Hebrew",                "עברית",            "he-IL", "heb"),
    "id":    ("Indonesian",            "Bahasa Indonesia", "id-ID", "ind"),
    "ms":    ("Malay",                 "Bahasa Melayu",    "ms-MY", "msa"),
    "fil":   ("Filipino",              "Filipino",         "fil-PH", "tgl"),
    "vi":    ("Vietnamese",            "Tiếng Việt",       "vi-VN", "vie"),
    "th":    ("Thai",                  "ไทย",              "th-TH", "tha"),
    "el":    ("Greek",                 "Ελληνικά",         "el-GR", "ell"),
    "cs":    ("Czech",                 "Čeština",          "cs-CZ", "ces"),
    "sk":    ("Slovak",                "Slovenčina",       "sk-SK", "slk"),
    "hu":    ("Hungarian",             "Magyar",           "hu-HU", "hun"),
    "ro":    ("Romanian",              "Română",           "ro-RO", "ron"),
    "bg":    ("Bulgarian",             "Български",        "bg-BG", "bul"),
    "hr":    ("Croatian",              "Hrvatski",         "hr-HR", "hrv"),
    "sr":    ("Serbian",               "Српски",           "sr-RS", "srp"),
    "sl":    ("Slovenian",             "Slovenščina",      "sl-SI", "slv"),
    "sv":    ("Swedish",               "Svenska",          "sv-SE", "swe"),
    "da":    ("Danish",                "Dansk",            "da-DK", "dan"),
    "no":    ("Norwegian",             "Norsk",            "nb-NO", "nor"),
    "fi":    ("Finnish",               "Suomi",            "fi-FI", "fin"),
    "et":    ("Estonian",              "Eesti",            "et-EE", "est"),
    "lv":    ("Latvian",               "Latviešu",         "lv-LV", "lav"),
    "lt":    ("Lithuanian",            "Lietuvių",         "lt-LT", "lit"),
    "ca":    ("Catalan",               "Català",           "ca-ES", "cat"),
    "sw":    ("Swahili",               "Kiswahili",        "sw-KE", "swa"),
    "af":    ("Afrikaans",             "Afrikaans",        "af-ZA", "afr"),
}

# Some engines return language *names*; map them back to codes.
_NAME_TO_CODE = {
    "english": "en", "portuguese": "pt", "spanish": "es", "french": "fr", "german": "de",
    "italian": "it", "dutch": "nl", "russian": "ru", "ukrainian": "uk", "polish": "pl",
    "turkish": "tr", "japanese": "ja", "korean": "ko", "chinese": "zh", "mandarin": "zh",
    "cantonese": "zh-TW", "arabic": "ar", "hindi": "hi", "bengali": "bn", "urdu": "ur",
    "tamil": "ta", "persian": "fa", "hebrew": "he", "indonesian": "id", "malay": "ms",
    "tagalog": "fil", "filipino": "fil", "vietnamese": "vi", "thai": "th", "greek": "el",
    "czech": "cs", "slovak": "sk", "hungarian": "hu", "romanian": "ro", "bulgarian": "bg",
    "croatian": "hr", "serbian": "sr", "slovenian": "sl", "swedish": "sv", "danish": "da",
    "norwegian": "no", "nynorsk": "no", "finnish": "fi", "estonian": "et", "latvian": "lv",
    "lithuanian": "lt", "catalan": "ca", "swahili": "sw", "afrikaans": "af",
}

# ISO-639-3 / misc codes some APIs return.
_ALIASES = {
    "eng": "en", "por": "pt", "spa": "es", "fra": "fr", "fre": "fr", "deu": "de", "ger": "de",
    "ita": "it", "nld": "nl", "rus": "ru", "ukr": "uk", "pol": "pl", "tur": "tr", "jpn": "ja",
    "kor": "ko", "zho": "zh", "cmn": "zh", "yue": "zh-TW", "ara": "ar", "hin": "hi", "ben": "bn",
    "urd": "ur", "tam": "ta", "fas": "fa", "per": "fa", "heb": "he", "ind": "id", "msa": "ms",
    "fil": "fil", "tgl": "fil", "tl": "fil", "vie": "vi", "tha": "th", "ell": "el", "ces": "cs",
    "slk": "sk", "hun": "hu", "ron": "ro", "bul": "bg", "hrv": "hr", "srp": "sr", "slv": "sl",
    "swe": "sv", "dan": "da", "nor": "no", "nob": "no", "nb": "no", "nn": "no", "fin": "fi",
    "est": "et", "lav": "lv", "lit": "lt", "cat": "ca", "swa": "sw", "afr": "af", "iw": "he",
    "zh-cn": "zh", "zh-hans": "zh", "zh-hant": "zh-TW", "zh-tw": "zh-TW", "pt-br": "pt",
    "pt-pt": "pt-PT", "en-us": "en", "en-gb": "en-GB", "es-mx": "es-MX", "es-419": "es-MX",
}


def name(code: str) -> str:
    if not code or code == AUTO:
        return "Auto-detect"
    return LANGUAGES.get(code, (code,))[0]


def base(code: str) -> str:
    """'pt-PT' -> 'pt', 'zh-TW' -> 'zh'."""
    if not code or code == AUTO:
        return code
    return code.split("-")[0].lower()


def normalize(raw) -> str | None:
    """Turn whatever an API reports ('english', 'EN', 'pt-BR', 'por') into one of our codes."""
    if not raw:
        return None
    s = str(raw).strip()
    low = s.lower()
    for code in LANGUAGES:
        if code.lower() == low:
            return code
    if low in _ALIASES:
        return _ALIASES[low]
    if low in _NAME_TO_CODE:
        return _NAME_TO_CODE[low]
    b = low.split("-")[0].split("_")[0]
    if b in LANGUAGES:
        return b
    if b in _ALIASES:
        return _ALIASES[b]
    return b or None


def same_language(a: str | None, b: str | None) -> bool:
    if not a or not b or a == AUTO or b == AUTO:
        return False
    return base(a) == base(b)


def locale_tag(code: str) -> str:
    """BCP-47 locale ('pt' -> 'pt-BR'), used to pick Windows voices."""
    entry = LANGUAGES.get(code) or LANGUAGES.get(base(code))
    return entry[2] if entry else "en-US"


def iso3(code: str) -> str:
    """ISO 639-3 code ('pt' -> 'por'), used by the OPUS-MT translation models."""
    entry = LANGUAGES.get(code) or LANGUAGES.get(base(code))
    return entry[3] if entry else base(code)


def whisper_code(code: str) -> str | None:
    if not code or code == AUTO:
        return None
    b = base(code)
    return {"fil": "tl", "no": "no"}.get(b, b)


def system_language() -> str:
    """Best guess of the user's language from the OS locale."""
    import locale
    try:
        loc = locale.getlocale()[0] or ""
    except Exception:
        loc = ""
    if not loc:
        try:
            import ctypes
            lcid = ctypes.windll.kernel32.GetUserDefaultUILanguage()
            loc = locale.windows_locale.get(lcid, "")
        except Exception:
            loc = ""
    low = loc.lower()
    if low.startswith("portuguese_brazil") or low.startswith("pt_br"):
        return "pt"
    if low.startswith("portuguese") or low.startswith("pt_pt"):
        return "pt-PT"
    code = normalize(low.split("_")[0]) if low else None
    return code if code in LANGUAGES else "en"


def choices(include_auto: bool):
    """[(code, label)] for combo boxes."""
    items = [(AUTO, "Auto-detect")] if include_auto else []
    items += sorted(((c, f"{v[0]} — {v[1]}") for c, v in LANGUAGES.items()), key=lambda x: x[1])
    return items
