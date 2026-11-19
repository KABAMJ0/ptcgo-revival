import time
import logging
import threading

from ptcgo import config

# CAS tickets issued by the HTTP server (worker threads) and consumed by the TCP
# server (event loop). Guarded by a lock since writers and the sweeper race across
# threads. Format: { "ST-TICKET-12345": (username, issued_at_monotonic) }
PENDING_TICKETS = {}
PENDING_TICKETS_LOCK = threading.Lock()
TICKET_TTL_SECONDS = 600

def issue_ticket(ticket, username):
    with PENDING_TICKETS_LOCK:
        PENDING_TICKETS[ticket] = (username, time.monotonic())

def _ticket_key(ticket: str) -> str:
    """The comparable part of a CAS ticket.

    The client is observed to present a ticket one character short of the one we
    issued -- `ST-<uuid>` arriving as `T-<uuid>`, the leading `S` eaten somewhere in
    its own parsing. Comparing the UUID portion rather than the whole string keeps
    the handshake working without weakening the check: the UUID is 122 random bits.
    """
    tail = (ticket or "").strip().rsplit("-", 5)[-5:]
    return "-".join(tail).lower() if len(tail) == 5 else (ticket or "").strip().lower()


def consume_ticket(ticket, username):
    """Atomically validates and removes a ticket; returns True on success."""
    key = _ticket_key(ticket)
    with PENDING_TICKETS_LOCK:
        match = None
        for stored, (stored_user, issued_at) in PENDING_TICKETS.items():
            if _ticket_key(stored) == key and stored_user.strip().lower() == (username or "").strip().lower():
                match = stored
                break
        if match is None:
            logging.warning("[CAS] rejected a ticket that was never issued, or one already used")
            return False
        del PENDING_TICKETS[match]
        return True


def sweep_expired_tickets():
    """Drops tickets whose CAS handshake never completed."""
    now = time.monotonic()
    with PENDING_TICKETS_LOCK:
        expired = [t for t, (_, issued_at) in PENDING_TICKETS.items()
                   if now - issued_at > TICKET_TTL_SECONDS]
        for ticket in expired:
            PENDING_TICKETS.pop(ticket, None)

# The active server host (captured from HTTP config request). Honours the
# PTCGO_HTTP_BASE_URL override so the fallback matches what clients are told.
SERVER_HOST = config.client_base_url().split("://", 1)[-1]

# Set by PTCGOServer.start() so the admin API (an HTTP worker thread) can read
# live connection state without importing the asyncio server module.
ACTIVE_TCP_SERVER = None

