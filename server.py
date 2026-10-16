from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse
import json, time

ROOT = Path(__file__).resolve().parent
STATE_FILE = ROOT / "state.json"
HOST, PORT = "127.0.0.1", 8766
START_TIME = time.time()

def load_state():
    try:
        d = json.loads(STATE_FILE.read_text(encoding="utf-8"))
        target = max(1, int(d.get("target", 200)))
        return {"kills": max(0, min(target, int(d.get("kills", 0)))), "target": target}
    except Exception:
        return {"kills": 0, "target": 200}

def save_state(state):
    STATE_FILE.write_text(json.dumps(state), encoding="utf-8")

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=str(ROOT), **kw)
    def log_message(self, fmt, *args):
        pass
    def send_json(self, payload, status=200):
        body = json.dumps(payload).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)
    def do_GET(self):
        path = urlparse(self.path).path
        if path == "/api/state":
            d = load_state()
            d["elapsed"] = int(time.time() - START_TIME)
            self.send_json(d)
            return
        if path == "/":
            self.path = "/index.html"
        return super().do_GET()
    def do_POST(self):
        path = urlparse(self.path).path
        if path not in ("/api/kill", "/api/undo", "/api/reset"):
            self.send_json({"error":"not found"}, 404); return
        d = load_state()
        if path == "/api/kill": d["kills"] = min(d["target"], d["kills"] + 1)
        elif path == "/api/undo": d["kills"] = max(0, d["kills"] - 1)
        else: d["kills"] = 0
        save_state(d)
        self.send_json(d)
    def do_OPTIONS(self):
        self.send_response(204); self.end_headers()

if __name__ == "__main__":
    print("\n=== ROTK KILL COUNTER V4 ===")
    try:
        raw = input("Objectif de kills pour ce challenge [200] : ").strip()
        target = int(raw) if raw else 200
        if target < 1: raise ValueError
    except ValueError:
        print("Objectif invalide : utilisation de 200."); target = 200
    save_state({"kills": 0, "target": target})
    print(f"Objectif : {target} kills")
    print(f"Overlay OBS : http://{HOST}:{PORT}/")
    print("Timer lancé. Laissez cette fenêtre ouverte. Ctrl+C pour arrêter.\n")
    ThreadingHTTPServer((HOST, PORT), Handler).serve_forever()
