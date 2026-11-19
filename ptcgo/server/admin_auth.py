import secrets
import threading
import time

SESSION_TTL_SECONDS = 12 * 3600
COOKIE_NAME = "spirit_admin"

_sessions = {}  # token -> {"account_id", "username", "expires"}
_lock = threading.Lock()


def create_session(account_id: str, username: str) -> str:
    token = secrets.token_hex(32)
    with _lock:
        _sessions[token] = {
            "account_id": account_id,
            "username": username,
            "expires": time.time() + SESSION_TTL_SECONDS,
        }
    return token


def get_session(token: str):
    if not token:
        return None
    with _lock:
        session = _sessions.get(token)
        if session is None:
            return None
        if session["expires"] < time.time():
            del _sessions[token]
            return None
        return dict(session)


def destroy_session(token: str):
    with _lock:
        _sessions.pop(token, None)


def destroy_sessions_for(account_id: str, keep: str = "") -> int:
    """Ends every admin session of an account except `keep` (after a password change)."""
    with _lock:
        doomed = [t for t, s in _sessions.items() if s["account_id"] == account_id and t != keep]
        for t in doomed:
            del _sessions[t]
    return len(doomed)


def token_from_headers(headers) -> str:
    cookie_header = ""
    if headers is not None:
        cookie_header = headers.get("Cookie", "") or ""
    for part in cookie_header.split(";"):
        name, _, value = part.strip().partition("=")
        if name == COOKIE_NAME:
            return value
    return ""


def session_cookie(token: str, clear: bool = False) -> str:
    if clear:
        return f"{COOKIE_NAME}=; Path=/admin; HttpOnly; SameSite=Lax; Max-Age=0"
    return (f"{COOKIE_NAME}={token}; Path=/admin; HttpOnly; SameSite=Lax; "
            f"Max-Age={SESSION_TTL_SECONDS}")
