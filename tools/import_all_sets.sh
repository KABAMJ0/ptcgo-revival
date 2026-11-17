#!/bin/bash
# Regenerate every card era in this fork from scratch.
#
#   ./tools/import_all_sets.sh            # all sets
#   ./tools/import_all_sets.sh bw1 bw2    # only these
#
# For each set: download the card data, generate one script + one 1024x1024
# texture per card, then repair non-integer collector numbers (Radiant
# Collection uses RC14, BW promos use BW99 -- neither is valid Python).
#
# Art is not committed; this script recreates it. Expect ~5 GB for all eras.
set -u
cd "$(dirname "$0")/.." || exit 1

PY="./venv/bin/python"
[ -x "$PY" ] || PY="python3"

# set_id:SET_CODE
BW_SETS="bw1:BW1 bw2:BW2 bw3:BW3 bw4:BW4 bw5:BW5 bw6:BW6 bw7:BW7 bw8:BW8 bw9:BW9 bw10:BW10 bw11:BW11 dv1:DV bwp:PROMO_BW"
SV_SETS="sv1:SV1 sv2:SV2 sv3:SV3 sv3pt5:SV3PT5 sv4:SV4 sv4pt5:SV4PT5 sv5:SV5 sv6:SV6 sv6pt5:SV6PT5 sv7:SV7 sv8:SV8 sv8pt5:SV8PT5 sv9:SV9 sv10:SV10 zsv10pt5:ZSV10PT5 rsv10pt5:RSV10PT5 svp:SVP sve:SVE"

SELECTED="$*"
if [ -n "$SELECTED" ]; then
  ALL=""
  for want in $SELECTED; do
    for pair in $BW_SETS $SV_SETS; do
      case "${pair##*:}" in
        "$(echo "$want" | tr '[:lower:]' '[:upper:]')") ALL="$ALL $pair" ;;
      esac
    done
  done
else
  ALL="$BW_SETS $SV_SETS"
fi

for pair in $ALL; do
  id="${pair%%:*}"
  code="${pair##*:}"
  echo "=== $id -> $code"
  python3 tools/fetch_set.py "$id" "$code" || { echo "fetch failed: $id"; continue; }
  $PY spirit/tools/import_set.py "spirit/game/scripts/cards/$code/$id.json" --set-code "$code" \
    2>&1 | grep -E 'Processing|Starting download|Error|Traceback' | tail -2
  python3 tools/fix_collector_numbers.py "$code"
  echo "scripts: $(ls spirit/game/scripts/cards/$code/*.py 2>/dev/null | wc -l) images: $(ls spirit/assets/cards/$code/*.png 2>/dev/null | wc -l)"
done
echo "done"
