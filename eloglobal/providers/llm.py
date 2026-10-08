"""AI model (LLM) providers for the optional "AI model" translation engine - only servers on this PC.

Ollama and LM Studio speak the OpenAI chat-completions dialect on localhost. The user installs them and their
models; EloGlobal never contacts an online AI service (base.local_json refuses non-local addresses). The licence of
a model the user downloads in Ollama / LM Studio is between the user and the model's author.
"""
from __future__ import annotations

import json
import re

from .base import Field, Provider, ProviderError, register
from .models_info import ModelInfo

# Model ids that are not chat models (embeddings, speech, images…).
_NOT_CHAT = re.compile(r"embed|whisper|tts|image|moderation|transcribe|audio|rerank|speech|ocr|guard", re.I)


class LLMProvider(Provider):
    kind = "llm"
    limits_note = "Runs on your PC: free and unlimited (speed depends on your hardware)."

    def chat(self, system: str, messages: list[dict], max_tokens: int = 1024) -> str:
        raise NotImplementedError

    def list_models(self) -> list[ModelInfo]:
        raise ProviderError(f"{self.name}: listing models is not supported")


class LocalOpenAICompatLLM(LLMProvider):
    base_url = ""
    default_model = ""
    model_options: list[str] = []

    @classmethod
    def build_fields(cls):
        return [
            Field("base_url", "Server address", "str", cls.base_url,
                  help="The OpenAI-compatible address of the server on this PC (…/v1)"),
            Field("model", "Model", "model", cls.default_model, options=cls.model_options),
            Field("temperature", "Temperature", "float", 0.2, min=-1, max=2, step=0.1,
                  help="-1 = don't send"),
            Field("timeout", "Timeout (s)", "float", 30, min=3, max=300),
            Field("extra_body", "Extra JSON body", "text", "",
                  help='Merged into every request, e.g. {"keep_alive": "30m"}'),
        ]

    def chat(self, system, messages, max_tokens=1024):
        url = self.s("base_url").rstrip("/") + "/chat/completions"
        body = {"model": self.s("model"), "messages": [{"role": "system", "content": system}] + messages,
                "max_tokens": max_tokens, "stream": False}
        temp = float(self.s("temperature", 0.2))
        if temp >= 0:
            body["temperature"] = temp
        extra = (self.s("extra_body") or "").strip()
        if extra:
            try:
                body.update(json.loads(extra))
            except json.JSONDecodeError as e:
                raise ProviderError(f"{self.name}: 'Extra JSON body' is not valid JSON: {e}")
        data = self.local_json("POST", url, body, timeout=float(self.s("timeout", 30)))
        try:
            content = data["choices"][0]["message"]["content"]
        except (KeyError, IndexError, TypeError):
            raise ProviderError(f"{self.name}: unexpected response: {str(data)[:300]}")
        if isinstance(content, list):  # some servers return content parts
            content = "".join(p.get("text", "") for p in content if isinstance(p, dict))
        content = re.sub(r"<think>.*?</think>", "", content or "", flags=re.S)   # reasoning models
        return content.strip()

    def list_models(self) -> list[ModelInfo]:
        url = self.s("base_url").rstrip("/") + "/models"
        data = self.local_json("GET", url, timeout=10)
        rows = data.get("data", data.get("models", [])) if isinstance(data, dict) else data
        out = [ModelInfo(id=m["id"], free="local") for m in rows or []
               if isinstance(m, dict) and m.get("id") and not _NOT_CHAT.search(m["id"])]
        out.sort(key=lambda i: i.id.lower())
        return out


# (id, name, base_url, default_model, suggestions) - suggested models allow commercial use (Apache-2.0 / Gemma terms)
LLM_PRESETS = [
    ("ollama", "Ollama", "http://localhost:11434/v1", "qwen2.5:7b",
     ["qwen2.5:7b", "qwen2.5:14b", "gemma3:4b", "gemma3:12b", "mistral-nemo"]),
    ("lmstudio", "LM Studio", "http://localhost:1234/v1", "local-model", []),
    ("custom_local", "Other server on this PC (OpenAI-compatible)", "http://localhost:8000/v1", "", []),
]


for _pid, _pname, _url, _model, _models in LLM_PRESETS:
    _cls = type(f"LLM_{_pid}", (LocalOpenAICompatLLM,), {
        "id": _pid, "name": _pname, "base_url": _url, "default_model": _model, "model_options": _models,
        "description": f"{_pname}: an AI model running on your own PC (you install it and its models yourself). "
                       "Nothing is sent to the internet.",
    })
    _cls.fields = _cls.build_fields()
    register(_cls)
