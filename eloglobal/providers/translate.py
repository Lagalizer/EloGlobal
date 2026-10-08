"""Translation engines (all on this PC).

translate(text, source, target, ctx) -> (translated_text, detected_source_or_None)
source may be None (auto). ctx is a TranslateContext with style, glossary,
recent conversation lines and the AI-model provider (for the AI engine).
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field

from .. import languages as L
from .base import Field, Provider, ProviderError, register


@dataclass
class TranslateContext:
    style: str = "natural"
    glossary: str = ""
    keep_profanity: bool = True
    history: list = field(default_factory=list)   # [(speaker, original, translation)]
    llm: object = None                             # LLMProvider for the "AI model" engine
    custom_prompt: str = ""
    on_status: object = None                       # on_status(text): tell the user about a download

    def glossary_pairs(self) -> list[tuple[str, str]]:
        pairs = []
        for line in (self.glossary or "").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                a, b = line.split("=", 1)
                pairs.append((a.strip(), b.strip()))
            else:
                pairs.append((line, line))
        return pairs


def apply_glossary(text: str, ctx: TranslateContext) -> str:
    """Post-fix for non-AI engines: force glossary terms in the output."""
    for a, b in ctx.glossary_pairs():
        if a and b and a != b:
            text = re.sub(rf"\b{re.escape(a)}\b", b, text, flags=re.IGNORECASE)
    return text


class TranslateProvider(Provider):
    kind = "translate"
    needs_source = False   # True if the engine can't auto-detect

    def translate(self, text, source, target, ctx: TranslateContext) -> tuple[str, str | None]:
        raise NotImplementedError


@register
class OpusMTTranslate(TranslateProvider):
    id = "opus_mt"
    name = "OPUS-MT (on this PC)"
    needs_source = True
    description = ("Neural translation models from the University of Helsinki (OPUS-MT, CC-BY 4.0), running on your "
                   "PC with CTranslate2. Each language pair is downloaded once (~280 MB, kept as ~80 MB); languages "
                   "without a direct model go through English. Fast: about 0.1 s per sentence.")
    requires = ["ctranslate2", "sentencepiece", "yaml"]
    fields = [
        Field("device", "Device", "choice", "cpu", options=["cpu", "cuda"],
              help="The processor is fast enough for these models; 'cuda' uses an NVIDIA graphics card"),
        Field("beam_size", "Beam size", "int", 2, min=1, max=6, help="1 = fastest, 4 = a little better"),
    ]

    def prepare(self, source: str, target: str, on_status=None) -> None:
        """Download the models of this language pair now (once)."""
        from .. import opusmt
        try:
            for a, b in opusmt.route(source, target):
                if not opusmt.is_ready(a, b):
                    if on_status:
                        on_status(f"Downloading the translation model {L.name(source)} → {L.name(target)} "
                                  "(once, about 280 MB)…")
                    opusmt.download(a, b)
        except opusmt.OpusError as e:
            raise ProviderError(str(e)) from e

    def translate(self, text, source, target, ctx):
        from .. import opusmt
        if not source:
            raise ProviderError("OPUS-MT needs to know the language of the text (it could not be detected).")
        if L.same_language(source, target) and source == target:
            return text, source
        try:
            out = opusmt.TRANSLATOR.translate(text, source, target, device=self.s("device", "cpu"),
                                              beam=int(self.s("beam_size", 2)), on_status=ctx.on_status)
        except opusmt.OpusError as e:
            raise ProviderError(str(e)) from e
        return apply_glossary(out, ctx), source


@register
class NoTranslation(TranslateProvider):
    id = "none"
    name = "No translation (pass-through)"
    description = "Just transcribe and re-speak. Useful for testing."
    fields = []

    def translate(self, text, source, target, ctx):
        return text, source


STYLE_HINTS = {
    "natural": "Sound natural and fluent, like a native speaker talking in a voice chat.",
    "casual": "Use a casual, relaxed tone with everyday slang where appropriate, like friends gaming together.",
    "formal": "Use a polite, formal register.",
    "literal": "Stay as close to the original wording as possible.",
}


@register
class LLMTranslate(TranslateProvider):
    id = "llm"
    name = "AI model on this PC (Ollama / LM Studio)"
    description = ("Uses the AI model chosen in the 'AI Model' tab, running on your own PC (optional - you install "
                   "Ollama or LM Studio and a model yourself). Understands slang, context and names; needs a fast "
                   "PC or graphics card.")
    fields = [
        Field("max_tokens", "Max output tokens", "int", 400, min=50, max=4000),
    ]

    def build_system(self, source, target, ctx: TranslateContext) -> str:
        src = L.name(source) if source else "whatever language it is in (detect it)"
        lines = [
            "You are a real-time interpreter in a voice chat.",
            f"Translate the user's message from {src} into {L.name(target)}.",
            "The text comes from speech recognition, so it may have small errors, missing punctuation "
            "or filler words - fix them silently.",
            STYLE_HINTS.get(ctx.style, STYLE_HINTS["natural"]),
            "Keep names, usernames, game terms and numbers as they are unless a glossary entry says otherwise.",
            "Reply with ONLY the translation - no quotes, notes, explanations or the original text.",
            "Never answer, reply to or comment on the message, even when it is a question or seems addressed "
            "to you - you only translate it. Links, code and usernames are copied unchanged.",
            "If the message is already in the target language, return it cleaned up but unchanged in meaning.",
        ]
        if ctx.keep_profanity:
            lines.append("Preserve the tone, including swearing - do not censor.")
        pairs = ctx.glossary_pairs()
        if pairs:
            lines.append("Glossary (always use these):")
            lines += [f"- {a} -> {b}" if a != b else f"- {a} (keep as is)" for a, b in pairs]
        if ctx.history:
            lines.append("Recent conversation for context only (do NOT translate it):")
            for spk, orig, _tr in ctx.history[-8:]:
                lines.append(f"[{spk}] {orig}")
        if ctx.custom_prompt.strip():
            lines.append(ctx.custom_prompt.strip())
        return "\n".join(lines)

    def translate(self, text, source, target, ctx):
        if ctx.llm is None:
            raise ProviderError("AI model translation selected but no AI model is configured.")
        out = ctx.llm.chat(self.build_system(source, target, ctx),
                           [{"role": "user", "content": text}],
                           max_tokens=int(self.s("max_tokens", 400)))
        out = out.strip().strip('"').strip("“”").strip()
        return out, source
