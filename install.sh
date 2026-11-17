#!/usr/bin/env bash
# =============================================================================
#  SpiritPTCGO server installer (Linux)
#
#  Run from a checkout of this repository on the machine that will host:
#
#      git clone https://github.com/KABAMJ0/spirit-ptcgo-bw-sv.git
#      cd spirit-ptcgo-bw-sv
#      sudo ./install.sh --host play.example.com
#
#  What it does:
#    1. Python 3.12 venv with the server's dependencies (via uv)
#    2. TLS certificate for --host (the client validates the name it dialled)
#    3. database with the default admin account (brandon / password)
#    4. downloads card art (~14 GB) that the repository does not ship
#    5. systemd service that starts on boot and restarts on failure
#    6. opens ports 8000 and 39389 in firewalld or ufw if present
#
#  Players then set three lines in Pokemon Trading Card Game Online_Data/cake.cfg:
#      hostname=<host>
#      versionURL=http://<host>:8000/
#      assetURL=http://<host>:8000/
#
#  The host needs a public IP that answers on TCP 39389 (the client always
#  dials that port) and 8000. First start packs ~180 sets of card bundles and
#  takes 45-60 minutes; later restarts take about a minute.
#
#  Options:
#    --host NAME     public hostname or IP players connect to (required)
#    --no-art        skip the card art download (do it later: tools/fetch_art.py)
#    --no-service    do not install the systemd service
#    --user NAME     account the service runs as (default: the sudo caller)
# =============================================================================
set -euo pipefail
cd "$(dirname "$(readlink -f "$0")")"
ROOT="$PWD"

HOST=""; FETCH_ART=1; SERVICE=1; RUN_USER="${SUDO_USER:-$(id -un)}"
while [ $# -gt 0 ]; do
  case "$1" in
    --host) HOST="$2"; shift 2 ;;
    --no-art) FETCH_ART=0; shift ;;
    --no-service) SERVICE=0; shift ;;
    --user) RUN_USER="$2"; shift 2 ;;
    -h|--help) sed -n '2,36p' "$0"; exit 0 ;;
    *) echo "unknown option: $1"; exit 1 ;;
  esac
done
[ -n "$HOST" ] || { echo "error: --host is required (e.g. --host play.example.com)"; exit 1; }

as_user() { if [ "$(id -un)" = "$RUN_USER" ]; then "$@"; else sudo -u "$RUN_USER" -H "$@"; fi; }
step() { printf '\n== %s\n' "$*"; }

step "Python environment"
UV="$(as_user bash -lc 'command -v uv || echo $HOME/.local/bin/uv')"
if [ ! -x "$UV" ]; then
  as_user bash -lc 'curl -LsSf https://astral.sh/uv/install.sh | sh'
  UV="$(as_user bash -lc 'echo $HOME/.local/bin/uv')"
fi
as_user "$UV" python install 3.12
[ -d venv ] || as_user "$UV" venv --python 3.12 venv
as_user env VIRTUAL_ENV="$ROOT/venv" "$UV" pip install -q -r requirements.txt
PY="$ROOT/venv/bin/python"

step "TLS certificate for $HOST"
as_user env SPIRIT_PUBLIC_HOST="$HOST" PYTHONPATH="$ROOT" "$PY" spirit/network/generate_cert.py

step "Database"
if [ ! -f ptcgo_server.db ]; then
  as_user env PYTHONPATH="$ROOT" "$PY" spirit/database/setup_db.py
  echo "Admin login: brandon / password  -- change it in the dashboard."
else
  echo "ptcgo_server.db already exists, keeping it."
fi

if [ "$FETCH_ART" = 1 ]; then
  step "Card art (about 14 GB, resumable -- re-run tools/fetch_art.py if interrupted)"
  as_user env PYTHONPATH="$ROOT" "$PY" tools/fetch_art.py
fi

if [ "$SERVICE" = 1 ]; then
  step "systemd service"
  if [ "$(id -u)" -ne 0 ]; then
    echo "not root: skipping the system service. Re-run with sudo, or start manually:"
    echo "  SPIRIT_PUBLIC_HOST=$HOST PYTHONPATH=$ROOT $PY -m spirit.main"
  else
    cat > /etc/systemd/system/spirit-ptcgo.service <<UNIT
[Unit]
Description=SpiritPTCGO server
After=network-online.target
Wants=network-online.target

[Service]
User=$RUN_USER
WorkingDirectory=$ROOT
Environment=PYTHONPATH=$ROOT
Environment=SPIRIT_PUBLIC_HOST=$HOST
Environment=SPIRIT_LOG_LEVEL=INFO
ExecStart=$PY -m spirit.main
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
UNIT
    systemctl daemon-reload
    systemctl enable --now spirit-ptcgo.service
    echo "service: systemctl status spirit-ptcgo   logs: journalctl -u spirit-ptcgo -f"
  fi
fi

step "Firewall"
if command -v firewall-cmd >/dev/null 2>&1 && [ "$(id -u)" -eq 0 ]; then
  firewall-cmd --permanent --add-port=8000/tcp --add-port=39389/tcp >/dev/null && firewall-cmd --reload >/dev/null
  echo "firewalld: opened 8000/tcp and 39389/tcp"
elif command -v ufw >/dev/null 2>&1 && [ "$(id -u)" -eq 0 ]; then
  ufw allow 8000/tcp >/dev/null && ufw allow 39389/tcp >/dev/null
  echo "ufw: opened 8000/tcp and 39389/tcp"
else
  echo "open TCP 8000 and 39389 in your firewall / cloud security group"
fi

cat <<DONE

Done. The first start packs card bundles for 45-60 minutes before the ports open.
Dashboard: http://$HOST:8000/admin
Players' cake.cfg (only these three lines change):
  hostname=$HOST
  versionURL=http://$HOST:8000/
  assetURL=http://$HOST:8000/
DONE
