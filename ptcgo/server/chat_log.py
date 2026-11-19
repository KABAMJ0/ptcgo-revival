"""Moderation record of chat: room messages and private messages.

Kept apart from the activity feed so chat volume never buries the Monitor view.
Same shape as activity.py: a bounded in-memory ring for recent lookups and a daily
JSONL file under logs/ (gitignored) so a report about yesterday is still answerable
after a restart. Files older than RETENTION_DAYS are deleted when a new day starts.
"""
import datetime
import glob
import json
import logging
import os
import threading

RING_SIZE = int(os.environ.get("PTCGO_CHAT_RING", "5000"))
RETENTION_DAYS = int(os.environ.get("PTCGO_CHAT_RETENTION_DAYS", "30"))
MAX_MESSAGE = 500

_lock = threading.Lock()
_ring = []
_pruned_day = None


def _log_dir():
    from ptcgo.server import activity
    return activity.LOG_DIR


def _prune(today):
    global _pruned_day
    if _pruned_day == today:
        return
    _pruned_day = today
    cutoff = (datetime.date.today() - datetime.timedelta(days=RETENTION_DAYS)).isoformat()
    for path in glob.glob(os.path.join(_log_dir(), "chat-*.jsonl")):
        if os.path.basename(path)[5:15] < cutoff:
            try:
                os.remove(path)
            except OSError:
                pass


def record(kind, sender_id, sender_name, message, room=None, to_id=None, to_name=None):
    """Appends one chat line. Never raises: moderation logging must not break chat."""
    try:
        now = datetime.datetime.now(datetime.timezone.utc)
        event = {"at": now.isoformat(timespec="seconds"), "kind": kind, "from_id": sender_id,
                 "from": sender_name, "room": room, "to_id": to_id, "to": to_name,
                 "message": str(message or "")[:MAX_MESSAGE]}
        with _lock:
            _ring.append(event)
            if len(_ring) > RING_SIZE:
                del _ring[: len(_ring) - RING_SIZE]
            day = now.date().isoformat()
            _prune(day)
            os.makedirs(_log_dir(), exist_ok=True)
            with open(os.path.join(_log_dir(), f"chat-{day}.jsonl"), "a", encoding="utf-8") as f:
                f.write(json.dumps(event, separators=(",", ":")) + "\n")
    except Exception as e:
        logging.debug(f"[ChatLog] could not record: {e}")


def recent(account_id=None, query=None, limit=200, days=14):
    """Newest-first chat lines, from the daily files plus anything still only in the ring."""
    events, seen = [], set()
    for path in sorted(glob.glob(os.path.join(_log_dir(), "chat-*.jsonl")))[-days:]:
        try:
            with open(path, encoding="utf-8") as f:
                for line in f:
                    try:
                        events.append(json.loads(line))
                    except ValueError:
                        continue
        except OSError:
            continue
    with _lock:
        events.extend(_ring)
    needle = (query or "").lower()
    out = []
    for e in reversed(events):
        key = (e.get("at"), e.get("from_id"), e.get("message"), e.get("room"), e.get("to_id"))
        if key in seen:
            continue
        seen.add(key)
        if account_id and account_id not in (e.get("from_id"), e.get("to_id")):
            continue
        if needle and needle not in " ".join(str(e.get(k) or "") for k in ("from", "to", "room", "message")).lower():
            continue
        out.append(e)
        if len(out) >= limit:
            break
    return out
