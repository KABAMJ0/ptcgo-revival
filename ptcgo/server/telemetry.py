"""Operational telemetry for the dashboard's Monitor view: HTTP traffic shape,
captured warnings/errors, asset cache size, disk and process health.

Everything here is read-only and cheap enough to poll every couple of seconds:
counters are locked dicts, the log handler keeps a bounded list, and the asset
cache walk is memoised for a minute because a bundle cache can hold tens of
thousands of files.
"""
import collections
import logging
import os
import re
import threading
import time

STARTED_AT = time.time()
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

ACTIVITY_WINDOW_SECONDS = 120

_lock = threading.Lock()
_totals = collections.Counter()
_by_second = collections.defaultdict(collections.Counter)

_LOG_LIMIT = 250
_error_counts = collections.Counter()
_errors = collections.deque(maxlen=_LOG_LIMIT)
_error_states = collections.Counter()
_capture_installed = False

_NUMBERS = re.compile(r"\b\d+(?:\.\d+)?\b")


def http_kind(path):
    """Coarse request class: the split an operator actually reasons about."""
    path = path or ""
    if path.startswith("/admin"):
        return "admin"
    if path.endswith((".unity3d", ".obb", ".png", ".jpg", ".jpeg", ".webp", ".crc")):
        return "asset"
    if path.endswith((".json", ".manifest")) or ".manifest" in path:
        return "manifest"
    return "api"


def record_http(path):
    kind = http_kind(path)
    second = int(time.time())
    with _lock:
        _totals[kind] += 1
        _totals["all"] += 1
        _by_second[second][kind] += 1
        _by_second[second]["all"] += 1
        if len(_by_second) > ACTIVITY_WINDOW_SECONDS * 2:
            for stale in sorted(_by_second)[:-ACTIVITY_WINDOW_SECONDS]:
                del _by_second[stale]


def http_shape():
    """Requests per second over the last minute, plus per-class totals."""
    now = int(time.time())
    with _lock:
        totals = dict(_totals)
        buckets = {s: dict(c) for s, c in _by_second.items()}
    series = []
    for offset in range(59, -1, -1):
        second = now - offset
        counts = buckets.get(second, {})
        series.append({
            "at": second,
            "all": counts.get("all", 0),
            "asset": counts.get("asset", 0),
            "api": counts.get("api", 0),
            "manifest": counts.get("manifest", 0),
            "admin": counts.get("admin", 0),
        })
    window = series[-30:]
    rate = sum(b["all"] for b in window) / max(1, len(window))
    asset = sum(b["asset"] for b in window)
    return {
        "series": series,
        "totals": totals,
        "rate_per_second": round(rate, 2),
        "asset_share": round(asset / max(1, sum(b["all"] for b in window)), 3),
        "recent_requests": sum(b["all"] for b in window),
    }


def _family(message):
    """Groups log lines that differ only by ids/counts into one counter."""
    text = _NUMBERS.sub("N", str(message))
    return text[:160]


class _CaptureHandler(logging.Handler):
    """Counts WARNING+ by logger and message family, keeping the newest rows."""

    def emit(self, record):
        if record.levelno < logging.WARNING:
            return
        try:
            message = record.getMessage()
        except Exception:
            message = str(record.msg)
        family = _family(message)
        with _lock:
            _error_counts[(record.levelname, record.name, family)] += 1
            _error_states[record.levelname] += 1
            _errors.append({
                "ts": record.created,
                "level": record.levelname,
                "logger": record.name,
                "message": message[:400],
            })
            if len(_error_counts) > 400:
                keeper = dict(_error_counts.most_common(200))
                _error_counts.clear()
                _error_counts.update(keeper)


def install_log_capture():
    """Attaches the capture handler to the root logger exactly once."""
    global _capture_installed
    if _capture_installed:
        return
    handler = _CaptureHandler(level=logging.WARNING)
    logging.getLogger().addHandler(handler)
    _capture_installed = True


def errors_snapshot(limit=40):
    with _lock:
        ranked = [
            {"level": level, "logger": logger, "message": family, "count": count}
            for (level, logger, family), count in _error_counts.most_common(limit)
        ]
        newest = list(_errors)[-limit:][::-1]
        by_level = dict(_error_states)
    return {"families": ranked, "newest": newest, "by_level": by_level}


_cache = {"at": 0.0, "data": None}


def asset_cache_stats(paths, ttl=60):
    """Entries and bytes for the served bundle cache (memoised)."""
    now = time.time()
    if _cache["data"] is not None and now - _cache["at"] < ttl:
        return _cache["data"]
    entries = 0
    size = 0
    roots = [p for p in paths if p and os.path.isdir(p)]
    for root in roots:
        for directory, _, files in os.walk(root):
            entries += len(files)
            for name in files:
                try:
                    size += os.path.getsize(os.path.join(directory, name))
                except OSError:
                    pass
    data = {
        "roots": roots,
        "entries": entries,
        "bytes": size,
        "scanned_at": now,
    }
    _cache["data"] = data
    _cache["at"] = now
    return data


def disk_stats(path=None):
    path = path or PROJECT_ROOT
    try:
        usage = os.statvfs(path)
    except OSError:
        return None
    total = usage.f_blocks * usage.f_frsize
    free = usage.f_bavail * usage.f_frsize
    return {
        "path": path,
        "total_bytes": total,
        "free_bytes": free,
        "used_bytes": total - free,
        "free_percent": round(100.0 * free / total, 1) if total else 0.0,
    }


_RSS = re.compile(r"VmRSS:\s+(\d+) kB")


def process_stats():
    """RSS, thread count and uptime for the game process."""
    rss = None
    try:
        with open("/proc/self/status", encoding="utf-8") as f:
            match = _RSS.search(f.read())
        if match:
            rss = int(match.group(1)) * 1024
    except OSError:
        pass
    return {
        "pid": os.getpid(),
        "started_at": STARTED_AT,
        "uptime_seconds": int(time.time() - STARTED_AT),
        "rss_bytes": rss,
        "threads": threading.active_count(),
    }
