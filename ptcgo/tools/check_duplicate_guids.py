"""Gate: no two card scripts may share an archetype GUID.

The loader keys cards by GUID in a dict, so a duplicate silently overwrites the
first card instead of failing — and the client then crashes at login building its
own archetype dictionary ("An item with the same key has already been added").
That is exactly how a byte-copied script shipped and hung the game at 63%.

Run: python -m ptcgo.tools.check_duplicate_guids
Exit code 1 with a list of offenders, 0 when every GUID is unique.
"""

import collections
import os
import re
import sys

CARDS_ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                          "game", "scripts", "cards")
GUID_PATTERN = re.compile(r'guid\s*=\s*"([0-9a-fA-F-]{36})"')


def scan(root: str = CARDS_ROOT) -> dict:
    """archetype GUID -> the script paths that declare it."""
    seen = collections.defaultdict(list)
    for dirpath, dirs, files in os.walk(root):
        dirs.sort()
        for name in sorted(files):
            if not name.endswith(".py") or name == "__init__.py":
                continue
            path = os.path.join(dirpath, name)
            try:
                with open(path, encoding="utf-8", errors="ignore") as f:
                    source = f.read()
            except OSError as e:
                print(f"cannot read {path}: {e}", file=sys.stderr)
                continue
            for guid in GUID_PATTERN.findall(source):
                seen[guid.lower()].append(os.path.relpath(path, root))
    return {guid: paths for guid, paths in seen.items() if len(paths) > 1}


def main() -> int:
    duplicates = scan()
    if not duplicates:
        print("duplicate archetype GUIDs: 0")
        return 0
    print(f"duplicate archetype GUIDs: {len(duplicates)}")
    for guid, paths in sorted(duplicates.items()):
        print(f"  {guid}: {', '.join(paths)}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
