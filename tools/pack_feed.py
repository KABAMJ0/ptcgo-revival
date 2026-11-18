#!/usr/bin/env python3
"""Live progress page for the first bundling pass.

The server packs card bundles before it opens its ports, which means there is no
dashboard to watch during the one long wait in this project. This serves a small
page instead: counters, a progress bar, and the tail of the server log.

    ./venv/bin/python tools/pack_feed.py /tmp/ptcgo-service.log
    # then open http://127.0.0.1:8999/

Point it at the file the server writes: if you started it with
`... -m ptcgo.main > /tmp/ptcgo-service.log 2>&1`, that is the path to pass.
The systemd unit in the README uses the same file.

Environment: PACK_FEED_PORT (default 8999), PACK_FEED_TOTAL (default 2064, the
number of artwork variants a full catalogue produces).
"""

import json
import os
import subprocess
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse

LOG = sys.argv[1] if len(sys.argv) > 1 else "/tmp/ptcgo-service.log"
PORT = int(os.environ.get("PACK_FEED_PORT", "8999"))
TOTAL = int(os.environ.get("PACK_FEED_TOTAL", "2064"))

PAGE = """<!doctype html>
<html><head><meta charset="utf-8"><title>PTCGO packing</title><style>
 :root{color-scheme:dark light}
 body{background:#0f1218;color:#e6ebf5;font:13px/1.5 system-ui,sans-serif;margin:0;padding:18px}
 h1{font-size:15px;margin:0 0 12px;color:#ffcb05}
 .row{display:flex;gap:22px;flex-wrap:wrap;margin-bottom:14px}
 .stat{background:#1a2130;border:1px solid #2d3950;border-radius:8px;padding:10px 14px;min-width:120px}
 .stat b{display:block;font-size:20px}
 .stat span{color:#8fa0bd;font-size:11px;text-transform:uppercase;letter-spacing:.6px}
 .bar{height:10px;background:#1a2130;border-radius:6px;overflow:hidden;margin-bottom:14px}
 .bar i{display:block;height:100%;background:#3d7dca;width:0;transition:width .4s}
 pre{background:#0b0e14;border:1px solid #2d3950;border-radius:8px;padding:12px;height:60vh;overflow:auto;
     font:12px/1.5 ui-monospace,monospace;white-space:pre-wrap;margin:0}
 .ok{color:#4caf7d}.err{color:#e05c5c}
</style></head><body>
<h1>PTCGO &middot; packing progress</h1>
<div class="row">
  <div class="stat"><span>built</span><b id="v">0</b></div>
  <div class="stat"><span>of</span><b id="t">TOTAL</b></div>
  <div class="stat"><span>sets packed</span><b id="s">0</b></div>
  <div class="stat"><span>errors</span><b id="e" class="ok">0</b></div>
  <div class="stat"><span>ports</span><b id="p">closed</b></div>
</div>
<div class="bar"><i id="bar"></i></div>
<pre id="log">waiting for the log&hellip;</pre>
<script>
let first = true;
async function tick(){
  try{
    const d = await (await fetch('/state')).json();
    document.getElementById('v').textContent = d.index;
    document.getElementById('t').textContent = d.total;
    document.getElementById('s').textContent = d.sets;
    const e = document.getElementById('e');
    e.textContent = d.errors; e.className = d.errors ? 'err' : 'ok';
    document.getElementById('p').textContent = d.listening ? 'LISTENING' : 'closed';
    document.getElementById('bar').style.width = Math.min(100, 100*d.index/d.total) + '%';
    const box = document.getElementById('log');
    const stick = first || box.scrollTop + box.clientHeight >= box.scrollHeight - 40;
    box.textContent = d.tail;
    if (stick) box.scrollTop = box.scrollHeight;
    first = false;
  }catch(err){ document.getElementById('p').textContent = 'feed lost'; }
}
tick(); setInterval(tick, 2000);
</script></body></html>
"""


def read_log():
    try:
        with open(LOG, "r", encoding="utf-8", errors="replace") as f:
            return f.readlines()
    except OSError:
        return []


def listening():
    try:
        out = subprocess.run(["ss", "-ltn"], capture_output=True, text=True, timeout=5).stdout
    except Exception:
        return False
    return ":8000" in out and ":39389" in out


class Handler(BaseHTTPRequestHandler):
    def _send(self, body, ctype="application/json"):
        payload = body.encode() if isinstance(body, str) else body
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self):
        if urlparse(self.path).path != "/state":
            self._send(PAGE.replace("TOTAL", str(TOTAL)), "text/html; charset=utf-8")
            return
        lines = read_log()
        index = 0
        sets = 0
        errors = 0
        for line in lines:
            if "Preparing bundle" in line:
                # the server prints "Preparing bundle 1422/2064", so trust its index
                try:
                    index = max(index, int(line.split("Preparing bundle")[1].split("/")[0].strip()))
                except (IndexError, ValueError):
                    index += 1
            if "Generating bundle" in line:
                sets += 1
            if "ERROR" in line or "Traceback" in line:
                errors += 1
        self._send(json.dumps({
            "index": index,
            "total": TOTAL,
            "sets": sets,
            "errors": errors,
            "listening": listening(),
            "tail": "".join(lines[-120:]),
        }))

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    print(f"packing feed on http://127.0.0.1:{PORT}/  (reading {LOG})")
    ThreadingHTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
