#!/usr/bin/env bash
# Progress of the bundling pass, for a server started with the log redirected.
#
#   ./tools/pack_progress.sh [log-path]
#
# Reads the log file the server was started with (defaults to
# /tmp/ptcgo-server.log) and reports how many sets have been packed, how big the
# bundle cache has grown and whether anything has errored.

LOG="${1:-/tmp/ptcgo-server.log}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CACHE="$ROOT/ptcgo/assets/bundleCache"

packed=$(find "$CACHE" -mindepth 1 -maxdepth 1 -type d -name 'en_US_*' 2>/dev/null | wc -l)
latest=$(grep -oE "Generating bundle 'en_US_[A-Za-z0-9_]*'" "$LOG" 2>/dev/null | tail -1 | grep -oE 'en_US_[A-Za-z0-9_]*')
errors=$(grep -cE 'ERROR|Traceback' "$LOG" 2>/dev/null || echo 0)
ports=$(ss -ltn 2>/dev/null | grep -cE ':8000|:39389')

printf 'packed sets : %s of about 190\n' "$packed"
printf 'now packing: %s\n' "${latest:-nothing yet}"
printf 'cache size : %s\n' "$(du -sh "$CACHE" 2>/dev/null | cut -f1)"
printf 'errors     : %s\n' "$errors"
if [ "$ports" -ge 2 ]; then
  printf 'status     : LISTENING on 8000 and 39389 - it is up\n'
elif [ "$ports" -eq 1 ]; then
  printf 'status     : one port open, still finishing\n'
else
  printf 'status     : packing, ports not open yet\n'
fi
if [ "$errors" -gt 0 ]; then
  printf '\nlast errors:\n'
  grep -E 'ERROR|Traceback' "$LOG" | tail -3 | cut -c1-160
fi
