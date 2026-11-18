#!/usr/bin/env python3
"""Repair collector numbers the importer cannot express as Python.

Radiant Collection cards are numbered RC14 and BW promos BW99, so the importer
writes `collector_number=RC14`, which raises NameError on load. This maps them
to integers: Radiant Collection is offset by 10000 so it never collides with
Legendary Treasures' own numbering, and prefixed promos keep their digits.

    python3 tools/fix_collector_numbers.py BW11 PROMO_BW
"""

import glob
import re
import sys

PATTERN = re.compile(r"^(\s*collector_number=)([^,]+),$", re.M)


def main():
    codes = sys.argv[1:]
    if not codes:
        raise SystemExit("usage: fix_collector_numbers.py <SET_CODE> [...]")

    fixed = 0
    for code in codes:
        for path in glob.glob(f"ptcgo/game/scripts/cards/{code}/*.py"):
            with open(path) as f:
                source = f.read()

            def repl(m):
                value = m.group(2).strip()
                if value.isdigit():
                    return m.group(0)
                digits = re.sub(r"\D", "", value)
                if not digits:
                    return f"{m.group(1)}0,"
                prefix = re.sub(r"\d", "", value).upper()
                number = int(digits)
                if prefix.startswith("RC"):
                    number += 10000
                return f"{m.group(1)}{number},"

            updated = PATTERN.sub(repl, source)
            if updated != source:
                with open(path, "w") as f:
                    f.write(updated)
                fixed += 1
    print(f"collector numbers fixed: {fixed}")


if __name__ == "__main__":
    main()
