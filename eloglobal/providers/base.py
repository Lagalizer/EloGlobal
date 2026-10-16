"""Provider framework.

Every engine (speech-to-text, translation, AI model, text-to-speech) is a Provider subclass that declares its
settings as a list of Field objects. The GUI builds the settings form from those fields automatically.

Every engine runs on this PC. The only network helper, local_json(), refuses any address that is not this PC or
the local network (an AI model server such as Ollama or LM Studio), so audio and text can't leave by mistake.
"""
from __future__ import annotations

import importlib.util
import ipaddress
import json
import socket
import threading
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from typing import Any

REGISTRY: dict[str, dict[str, type["Provider"]]] = {"stt": {}, "translate": {}, "llm": {}, "tts": {}}


class ProviderError(Exception):
    pass


@dataclass
class Field:
    key: str
    label: str
    kind: str = "str"        # str | secret | int | float | bool | choice | combo (editable) | model | path | text
    default: Any = ""
    options: list = field(default_factory=list)
    help: str = ""
    min: float = 0
    max: float = 100000
    step: float = 1
    key_ref: str = ""        # for kind == "secret": id in the KeyStore


def register(cls):
    REGISTRY[cls.kind][cls.id] = cls
    return cls


def providers(kind: str) -> dict[str, type["Provider"]]:
    return REGISTRY[kind]


def is_local_address(url: str) -> bool:
    """True for this PC (localhost) and private network addresses (192.168.x.x, 10.x.x.x...)."""
    host = urllib.parse.urlparse(url).hostname or ""
    if not host:
        return False
    if host == "localhost":
        return True
    try:
        addrs = {i[4][0].split("%")[0] for i in socket.getaddrinfo(host, None)}
        return bool(addrs) and all(ipaddress.ip_address(a).is_private or ipaddress.ip_address(a).is_loopback
                                   for a in addrs)
    except (OSError, ValueError):
        return False


class _RefuseRedirects(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise urllib.error.HTTPError(req.full_url, code, f"redirect to {newurl} refused (only local servers)",
                                     headers, fp)


# Local AI servers: no redirects (a server on the network could send the request somewhere else) and no system
# proxy (the request must go straight to the local address, not through a proxy on the internet).
_NO_REDIRECTS = urllib.request.build_opener(_RefuseRedirects(), urllib.request.ProxyHandler({}))


class Provider:
    id = ""
    name = ""
    kind = ""
    local = True                  # every engine of this edition runs on this PC
    description = ""
    requires: list[str] = []      # importable module names
    pip_hint = ""
    fields: list[Field] = []

    def __init__(self, settings: dict | None, keys):
        self.keys = keys
        self.settings = {f.key: f.default for f in self.fields}
        for k, v in (settings or {}).items():
            self.settings[k] = v
        self.lock = threading.Lock()

    # ---------------------------------------------------------------- helpers
    @classmethod
    def missing_requirements(cls) -> list[str]:
        return [m for m in cls.requires if importlib.util.find_spec(m) is None]

    @classmethod
    def label(cls) -> str:
        return cls.name

    def s(self, key, default=None):
        v = self.settings.get(key, default)
        return default if v is None else v

    def key(self, field_key: str = "api_key") -> str:
        for f in self.fields:
            if f.key == field_key and f.kind == "secret":
                return self.keys.get(f.key_ref or f"{self.id}")
        return ""

    def local_json(self, method: str, url: str, body: dict | None = None, headers: dict | None = None,
                   timeout: float = 30):
        """A JSON request to a server on this PC / the local network. Anything else is refused."""
        if not is_local_address(url):
            raise ProviderError(f"{self.name}: {url} is not on this PC or your local network. EloGlobal only "
                                "talks to AI servers running on your own computer (Ollama, LM Studio…).")
        data = json.dumps(body).encode("utf-8") if body is not None else None
        h = {"Content-Type": "application/json", **(headers or {})}
        try:
            with _NO_REDIRECTS.open(urllib.request.Request(url, data=data, headers=h, method=method),
                                    timeout=timeout) as r:
                return json.loads(r.read().decode("utf-8") or "null")
        except urllib.error.HTTPError as e:
            text = e.read().decode("utf-8", "replace")[:300].replace("\n", " ")
            raise ProviderError(f"{self.name}: HTTP {e.code}: {text}") from e
        except (urllib.error.URLError, OSError) as e:
            raise ProviderError(f"{self.name}: server not reachable at {url} - is it running? ({e})") from e

    def warmup(self) -> None:
        """Load models ahead of time (optional)."""

    def close(self) -> None:
        pass
