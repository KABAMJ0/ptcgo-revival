"""Global server addressing config — the single place to set the host players connect to."""
import os
from typing import Optional

# The address players use to reach this server (IP or domain, no scheme/port).
# For public hosting set this to your public IP/domain, or export PTCGO_PUBLIC_HOST.
# The client is redirected here mid-login (ConnectionService), so 127.0.0.1 only works
# when the client runs on the same machine as the server.
PUBLIC_HOST = os.environ.get("PTCGO_PUBLIC_HOST", "127.0.0.1")

HTTP_PORT = int(os.environ.get("PTCGO_HTTP_PORT", "8000"))

# The admin dashboard can be moved to its own port so a tunnel pointed at HTTP_PORT
# carries card art to the internet and can never carry the panel. Defaults to HTTP_PORT,
# where the admin routes are served by the same listener exactly as before.
ADMIN_PORT = int(os.environ.get("PTCGO_ADMIN_PORT", str(HTTP_PORT)))
ADMIN_ON_SEPARATE_PORT = ADMIN_PORT != HTTP_PORT
TCP_PORT = int(os.environ.get("PTCGO_TCP_PORT", "39389"))

# Player database. Leave unset for local SQLite, or set a mysql+pymysql:// or
# mariadb+pymysql:// URL for MariaDB/MySQL
# See example in README in sql/README.md
DATABASE_URL = os.environ.get("PTCGO_DATABASE_URL")

# WARNING: experimental bundle packing algorithm, we default to lz4 but lzma would cut the sizes in half
BUNDLE_PACKER = os.environ.get("PTCGO_BUNDLE_PACKER", "lz4").strip().lower()

# The URL players' clients use for every HTTP fetch (manifests, bundles, art).
#
# By default it is built from PUBLIC_HOST and HTTP_PORT, which is right when the HTTP
# port is forwarded. Behind a reverse proxy or a Cloudflare Tunnel it is wrong: the
# public URL has a hostname and no port, and it is HTTPS. Export
#   PTCGO_HTTP_BASE_URL=https://cards.example.com
# and that string is used VERBATIM as the base for every client-facing URL. A trailing
# slash is stripped so `{base}/path` never doubles it. Unset keeps the old behaviour
# exactly, including the per-request Host header fallback in the HTTP server.
HTTP_BASE_URL_OVERRIDE = (os.environ.get("PTCGO_HTTP_BASE_URL") or "").strip().rstrip("/")


def client_base_url(request_host: Optional[str] = None) -> str:
    """The absolute base a client should fetch from, with no trailing slash.

    With PTCGO_HTTP_BASE_URL set the override wins for every caller. Otherwise the
    request's Host header is used when the server has one, falling back to
    `PUBLIC_HOST:HTTP_PORT`.
    """
    if HTTP_BASE_URL_OVERRIDE:
        return HTTP_BASE_URL_OVERRIDE
    host = (request_host or "").strip() or f"{PUBLIC_HOST}:{HTTP_PORT}"
    return ("http://" + host).rstrip("/")


HTTP_BASE_URL = client_base_url()
PLACEHOLDER_IMG = f"{HTTP_BASE_URL}/placeholder.png"

# --- Operational tunables (env-overridable; safe defaults chosen to never affect legit play) ---
LOG_LEVEL = os.environ.get("PTCGO_LOG_LEVEL", "INFO").upper()

# Inbound read idle deadlines. The client pings regularly, so a header that never
# arrives for this long is a half-open/dead socket. Pre-auth is tighter to reap
# port-scanners and stalled handshakes before they allocate a router.
IDLE_TIMEOUT_SECONDS = float(os.environ.get("PTCGO_IDLE_TIMEOUT", "240"))
PREAUTH_TIMEOUT_SECONDS = float(os.environ.get("PTCGO_PREAUTH_TIMEOUT", "60"))

# Max bytes an inbound zlib body may expand to (decompression-bomb guard). Legit
# client-originated compressed payloads are decks/telemetry, well under 1 MB.
# Seconds a player may sit alone in a versus queue before the server pairs them
# with the built-in AI bot. 0 disables the fallback (queue waits for a human).
BOT_QUEUE_DELAY_SECONDS = float(os.environ.get("PTCGO_BOT_QUEUE_DELAY", "6"))

MAX_DECOMPRESSED_BYTES = int(os.environ.get("PTCGO_MAX_DECOMPRESSED", str(16 * 1024 * 1024)))

# Hard cap on simultaneous TCP connections (0 = unlimited). Excess accepts are
# closed immediately, before a router is built.
MAX_CONNECTIONS = int(os.environ.get("PTCGO_MAX_CONNECTIONS", "0"))

# Per-connection inbound packet-rate token bucket (abuse guard). Generous enough
# that normal offer/reply cadence and reconnect replay never trip it.
INBOUND_RATE_PER_SEC = float(os.environ.get("PTCGO_INBOUND_RATE", "80"))
INBOUND_RATE_BURST = float(os.environ.get("PTCGO_INBOUND_BURST", "240"))
