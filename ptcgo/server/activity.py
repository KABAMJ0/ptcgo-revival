"""Rolling activity log for the admin dashboard's Monitor view.

Two things eat each other if you get this wrong: an operator wants to see what
just happened, and nobody wants a database write per login. So events go into a
bounded in-memory ring (cheap, instant, feeds the live feed) and are appended to
a daily JSONL file (cheap, sequential, survives a restart).

    record("login", account="brandon", detail="from 127.0.0.1")
    events_since(cursor)   -> {"events": [...], "cursor": 42}
"""

import datetime
import json
import logging
import os
import threading
import time

RING_SIZE = int(os.environ.get("PTCGO_ACTIVITY_RING", "1000"))
LOG_DIR = os.environ.get(
    "PTCGO_ACTIVITY_LOG_DIR",
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "logs")),
)

_lock = threading.Lock()
_ring = []          # list of event dicts, oldest first
_next_id = 1        # monotonic cursor
_sessions = {}      # account_id -> {"account", "since", "scene", "state", "addr"}


def _log_path():
    day = datetime.date.today().isoformat()
    return os.path.join(LOG_DIR, f"activity-{day}.jsonl")


def _append_file(event):
    try:
        os.makedirs(LOG_DIR, exist_ok=True)
        with open(_log_path(), "a", encoding="utf-8") as f:
            f.write(json.dumps(event, separators=(",", ":")) + "\n")
    except OSError as e:
        logging.debug(f"[Activity] could not append to log: {e}")


def record(kind, account=None, detail="", **extra):
    """Appends one event. Never raises: monitoring must not break gameplay."""
    global _next_id
    with _lock:
        event = {
            "id": _next_id,
            "at": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
            "kind": kind,
            "account": account,
            "detail": detail,
        }
        if extra:
            event.update(extra)
        _next_id += 1
        _ring.append(event)
        if len(_ring) > RING_SIZE:
            del _ring[: len(_ring) - RING_SIZE]
    _append_file(event)
    return event


def events_since(cursor=None, limit=200, kind=None, account=None):
    """Newest-first slice of the ring, optionally filtered."""
    with _lock:
        rows = list(_ring)
    if cursor:
        try:
            rows = [e for e in rows if e["id"] > int(cursor)]
        except (TypeError, ValueError):
            pass
    if kind:
        rows = [e for e in rows if e["kind"] == kind]
    if account:
        needle = str(account).lower()
        rows = [e for e in rows if (e.get("account") or "").lower() == needle]
    newest = list(reversed(rows))[:limit]
    return {"events": newest, "cursor": _next_id - 1, "total": len(rows)}


def counts(window_seconds=3600):
    """How many of each kind in the recent window, for the overview tiles."""
    cutoff = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(seconds=window_seconds)
    out = {}
    with _lock:
        rows = list(_ring)
    for e in rows:
        try:
            when = datetime.datetime.fromisoformat(e["at"])
        except ValueError:
            continue
        if when < cutoff:
            continue
        out[e["kind"]] = out.get(e["kind"], 0) + 1
    return out


# --- live session registry -------------------------------------------------

def session_open(account_id, username, addr=None):
    with _lock:
        _sessions[account_id] = {
            "account_id": account_id,
            "account": username,
            "addr": addr,
            "since": time.time(),
            "scene": None,
            "state": "connected",
        }
    record("connect", account=username, detail=addr or "")


def session_update(account_id, **fields):
    with _lock:
        sess = _sessions.get(account_id)
        if sess is not None:
            sess.update({k: v for k, v in fields.items() if v is not None})
            sess["_touched"] = time.time()


def session_close(account_id, reason=""):
    with _lock:
        sess = _sessions.pop(account_id, None)
    if sess:
        record("disconnect", account=sess.get("account"), detail=reason)


def sessions():
    now = time.time()
    with _lock:
        rows = list(_sessions.values())
    out = []
    for s in rows:
        item = dict(s)
        item.pop("_touched", None)
        item["idle_seconds"] = int(now - item.get("_touched", item.get("since", now)))
        item["connected_seconds"] = int(now - item.get("since", now))
        out.append(item)
    out.sort(key=lambda s: s.get("since", 0))
    return out
