"""
Shared LLM helper for this workspace. Standard library only, no installs.

Reads LLM_API_KEY / LLM_BASE_URL / LLM_MODEL from the repo's .env
(OpenAI-compatible endpoint), so any script can do:

    import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
    from llm import chat
    print(chat("Reply with hello"))

Run directly for a smoke test:  python3 llm.py
"""
import json
import os
import re
import urllib.error
import urllib.request
from pathlib import Path

ENV_FILE = Path(__file__).resolve().parent / ".env"


def load_env(path=ENV_FILE):
    """Minimal .env loader: KEY=VALUE lines, ${VAR} expansion, real env wins."""
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        value = value.strip().strip('"').strip("'")
        value = re.sub(r"\$\{(\w+)\}", lambda m: os.environ.get(m.group(1), ""), value)
        os.environ.setdefault(key.strip(), value)


load_env()


def chat(prompt=None, messages=None, model=None, temperature=None, max_tokens=None, timeout=120):
    """Send a chat completion and return the reply text."""
    api_key = os.environ.get("LLM_API_KEY") or os.environ.get("OPENAI_API_KEY")
    base_url = (os.environ.get("LLM_BASE_URL") or os.environ.get("OPENAI_BASE_URL", "")).rstrip("/")
    if not api_key or not base_url:
        raise RuntimeError(f"LLM_API_KEY / LLM_BASE_URL not set (expected in {ENV_FILE})")

    if messages is None:
        messages = [{"role": "user", "content": prompt}]
    body = {"model": model or os.environ.get("LLM_MODEL"), "messages": messages, "stream": False}
    if temperature is not None:
        body["temperature"] = temperature
    if max_tokens is not None:
        body["max_tokens"] = max_tokens

    req = urllib.request.Request(
        f"{base_url}/chat/completions",
        data=json.dumps(body).encode(),
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.load(resp)
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"LLM call failed: HTTP {e.code}: {e.read().decode()[:500]}") from None
    return data["choices"][0]["message"]["content"]


if __name__ == "__main__":
    print(chat("Reply with hello"))
