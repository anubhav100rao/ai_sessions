"""
Session 8 - Workflow Lab server. Standard library only, no installs.

Serves workflow_lab.html at http://localhost:8808 and forwards the lab's AI
steps to OpenRouter, so the API key stays on this computer and never reaches
the browser page.

    python3 workflow_server.py                 # then open http://localhost:8808
    python3 workflow_server.py --port 9000
    python3 workflow_server.py --env /path/to/.env

The key is read from OPENROUTER_API_KEY in (first match wins):
  1. the real environment
  2. --env PATH
  3. ~/development/accio-ai/xray-demo/.env

Only the two light models below can be used, whatever the .env MODEL says.
If the key is missing or a call fails, the lab switches to its offline
(scripted) answers on its own.
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

HERE = Path(__file__).resolve().parent
LAB = HERE / "workflow_lab.html"
DEFAULT_ENV = Path.home() / "development" / "accio-ai" / "xray-demo" / ".env"
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

# Light models only. The browser can pick a key, never a raw model id.
MODELS = {
    "luna": "openai/gpt-6-luna",      # lightest, default
    "terra": "openai/gpt-5.6-terra",  # mid tier
}
MAX_TOKENS = 900  # covers a little reasoning plus a short JSON answer


def load_env(path):
    if not path or not Path(path).exists():
        return False
    for line in Path(path).read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))
    return True


def call_openrouter(model_key, messages, want_json):
    key = os.environ.get("OPENROUTER_API_KEY")
    if not key:
        raise RuntimeError("OPENROUTER_API_KEY is not set")
    body = {
        "model": MODELS[model_key],
        "messages": messages,
        "max_tokens": MAX_TOKENS,
        "temperature": 0.2,
        "reasoning": {"effort": "low"},
    }
    if want_json:
        body["response_format"] = {"type": "json_object"}
    req = urllib.request.Request(
        OPENROUTER_URL,
        data=json.dumps(body).encode(),
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost",
            "X-Title": "Lakeview Workflow Lab",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.load(resp)
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"OpenRouter HTTP {e.code}: {e.read().decode()[:300]}") from None
    msg = data["choices"][0]["message"]
    return {
        "text": msg.get("content") or "",
        "model": data.get("model", MODELS[model_key]),
        "usage": data.get("usage", {}),
    }


class Handler(BaseHTTPRequestHandler):
    def _send(self, code, payload, ctype="application/json"):
        raw = payload if isinstance(payload, bytes) else json.dumps(payload).encode()
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(raw)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(raw)

    def do_GET(self):
        if self.path in ("/", "/index.html", "/workflow_lab.html"):
            return self._send(200, LAB.read_bytes(), "text/html; charset=utf-8")
        if self.path == "/api/status":
            return self._send(200, {
                "live": bool(os.environ.get("OPENROUTER_API_KEY")),
                "models": MODELS,
            })
        self._send(404, {"error": "not found"})

    def do_POST(self):
        if self.path != "/api/chat":
            return self._send(404, {"error": "not found"})
        try:
            n = int(self.headers.get("Content-Length", 0))
            req = json.loads(self.rfile.read(n) or b"{}")
            model_key = req.get("model", "luna")
            if model_key not in MODELS:
                return self._send(400, {"error": f"model must be one of {list(MODELS)}"})
            messages = req.get("messages")
            if not isinstance(messages, list) or not messages:
                return self._send(400, {"error": "messages missing"})
            out = call_openrouter(model_key, messages, bool(req.get("json")))
            self._send(200, out)
        except Exception as e:  # the lab falls back to offline answers
            self._send(502, {"error": str(e)})

    def log_message(self, fmt, *args):
        sys.stderr.write("  " + (fmt % args) + "\n")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--port", type=int, default=8808)
    ap.add_argument("--env", default=None, help="path to a .env with OPENROUTER_API_KEY")
    a = ap.parse_args()

    if not os.environ.get("OPENROUTER_API_KEY"):
        for p in (a.env, DEFAULT_ENV):
            if p and load_env(p) and os.environ.get("OPENROUTER_API_KEY"):
                print(f"Key loaded from {p}")
                break
    if not os.environ.get("OPENROUTER_API_KEY"):
        print("No OPENROUTER_API_KEY found: the lab will run in offline (scripted) mode.")
    print(f"Models: luna -> {MODELS['luna']}, terra -> {MODELS['terra']}")
    print(f"Open http://localhost:{a.port}   (Ctrl+C to stop)")
    ThreadingHTTPServer(("127.0.0.1", a.port), Handler).serve_forever()


if __name__ == "__main__":
    main()
