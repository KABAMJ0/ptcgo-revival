"""Every card script must carry its own archetype GUID.

Two scripts sharing a GUID make the loader keep one and drop the other, and
the client then crashes at login building its archetype dictionary, so the
gate prints a non-zero count and exits 1:

    python -m ptcgo.tools.check_duplicate_guids

A new printing of an existing card gets its identity from the printing, not
from the script it was copied from:

    uuid.uuid5(uuid.NAMESPACE_URL, "ptcgo:card:<SET>:<NUMBER>")
"""
import collections
import pathlib
import re
import sys

from ptcgo.game.scripts.cards import SCRIPTS_DIR

GUID_RE = re.compile(r"guid\s*=\s*[\"']([0-9a-fA-F-]{36})[\"']")


def collect(root=None):
    """guid -> the script paths declaring it."""
    root = pathlib.Path(root or SCRIPTS_DIR)
    seen = collections.defaultdict(list)
    for path in sorted(root.rglob("*.py")):
        for guid in set(GUID_RE.findall(path.read_text(errors="ignore"))):
            seen[guid.lower()].append(str(path))
    return seen


def main() -> int:
    seen = collect()
    duplicates = {guid: paths for guid, paths in seen.items() if len(paths) > 1}
    print(f"scripts: {sum(len(p) for p in seen.values())} unique GUIDs: {len(seen)}")
    for guid, paths in sorted(duplicates.items()):
        print(f"  {guid}: {', '.join(paths)}")
    print(f"duplicate archetype GUIDs: {len(duplicates)}")
    return 1 if duplicates else 0


if __name__ == "__main__":
    sys.exit(main())
