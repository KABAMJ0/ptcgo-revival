#!/usr/bin/env bash
# Deploy the working checkout to the live one and restart the game server.
#
#   tools/deploy.sh            code deploy: sync, restart, skip the art scan
#   tools/deploy.sh --art      art deploy: sync, restart, rebuild bundles too
#
# The difference matters: the startup bundle scan opens every bundle to see
# whether any card art is newer than the built bundle, which is two to four
# minutes on a 2,000-bundle cache. Code deploys skip it.
set -euo pipefail

SOURCE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET="${PTCGO_LIVE_DIR:-$HOME/Downloads/ptcgo-revival-main}"
UNIT="${PTCGO_UNIT:-ptcgo}"
WEBHOOK_FILE="$HOME/.capy/work/discord_webhook"

SCAN=skip
if [ "${1:-}" = "--art" ]; then
  SCAN=run
fi

echo "[deploy] $SOURCE -> $TARGET (bundle scan: $SCAN)"

rsync -a --no-perms \
  --exclude '.git/' --exclude 'venv/' --exclude '__pycache__/' --exclude '*.pyc' \
  --exclude 'ptcgo_server.db*' --exclude 'server.crt' --exclude 'server.key' \
  --exclude 'logs/' --exclude '*.log' --exclude 'ptcgo/assets/bundleCache/' \
  --exclude 'baseline/' \
  "$SOURCE/ptcgo/" "$TARGET/ptcgo/"

if [ "$SCAN" = "skip" ]; then
  mkdir -p "$HOME/.config/systemd/user/${UNIT}.service.d"
  cat > "$HOME/.config/systemd/user/${UNIT}.service.d/bundle-scan.conf" <<EOF
[Service]
Environment=PTCGO_SKIP_BUNDLE_SCAN=1
EOF
else
  rm -f "$HOME/.config/systemd/user/${UNIT}.service.d/bundle-scan.conf"
fi

systemctl --user daemon-reload
systemctl --user restart "$UNIT"

# Wait for both ports, then report honestly.
for i in $(seq 1 60); do
  if ss -ltn 2>/dev/null | grep -q ':39389' && ss -ltn 2>/dev/null | grep -q ':8000'; then
    code=$(curl -s -o /dev/null -w '%{http_code}' --max-time 5 http://127.0.0.1:8000/admin || true)
    echo "[deploy] up after ~$((i*5))s, admin $code"
    if [ -x "$WEBHOOK_FILE" ] || [ -f "$WEBHOOK_FILE" ]; then
      message="Deploy complete ($(git -C "$SOURCE" rev-parse --short HEAD)): server up, admin $code."
      curl -s -X POST -H 'Content-Type: application/json' \
        -d "$(python3 -c 'import json,sys;print(json.dumps({"username":"Capy-AI","avatar_url":"https://capy.ai/avatars/capy-avatar-5.png","content":sys.argv[1]}))' "$message")" \
        "$(cat "$WEBHOOK_FILE")" > /dev/null || true
    fi
    exit 0
  fi
  sleep 5
done

echo "[deploy] FAILED: ports did not open within 300s. Last log lines:" >&2
tail -20 /tmp/${UNIT}-service.log >&2 2>/dev/null || true
exit 1
