"""Downloads the narrator voice of an app language (the guide and the Manual) - once.

English ships with the app; German, French, Italian and Ukrainian get a Piper voice (60-80 MB); languages that
have a Windows voice on this PC need no download; Portuguese and Spanish without a Windows voice get Kokoro
(about 350 MB)."""
from __future__ import annotations

from . import localvoice
from .i18n import Language


def size_mb(lang: Language) -> int:
    v = lang.narrator()
    return 0 if v is None or localvoice.installed(v) else v.size_mb


def download(lang: Language, progress=None, cancelled=lambda: False) -> None:
    """Fetch the narrator voice of `lang`. progress(done_bytes, total_bytes). Raises on failure; a half-downloaded
    file never replaces a good one."""
    v = lang.narrator()
    if v is not None and not localvoice.installed(v):
        localvoice.download(v, progress, cancelled)
