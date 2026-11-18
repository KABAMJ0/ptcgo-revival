"""Audits the JSON keys this server emits against the client's own DTOs.

The dashboard of "does this payload work" is notes/client-protocol.json, read out
of the shipped assemblies. This walks the server source for `send_packet` /
`send(...)` payload dictionaries, takes each one's `messageName`, and compares its
top-level keys with the DTO's declared keys. Unknown keys are the ones that make
a client drop the message (JsonFx ignores them silently), so they are worth a
static check.

    python tools_client_key_audit.py            # report
    python tools_client_key_audit.py --strict   # non-zero exit when a mismatch exists
"""
import ast
import json
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)

PROTOCOL = os.path.join(ROOT, "notes", "client-protocol.json")
SCAN_DIRS = [os.path.join(ROOT, "ptcgo"), os.path.join(ROOT, "spirit")]
SKIP_DIRS = {"__pycache__", "handlers", "test", "tests", "tools", "re_tools"}


def simple(name):
    return name.rsplit(".", 1)[-1].split("+")[-1]


def dict_keys(node):
    keys = []
    for key in node.keys:
        if isinstance(key, ast.Constant) and isinstance(key.value, str):
            keys.append(key.value)
    return keys


def resolve_message_name(value):
    """`OutboundMsg.X.value` or a plain string literal -> the message name."""
    if isinstance(value, ast.Constant) and isinstance(value.value, str):
        return value.value
    if isinstance(value, ast.Attribute):        # OutboundMsg.X.value
        return value.attr if value.attr != "value" else _enum_member_name(value.value)
    return None


def _enum_member_name(node):
    if isinstance(node, ast.Attribute):
        return node.attr
    return None


def enum_map():
    """OutboundMsg member -> wire value, so `OutboundMsg.X.value` resolves."""
    from ptcgo.network.message_names import OutboundMsg
    return {member.name: member.value for member in OutboundMsg}


def collect_payloads(path, messages):
    with open(path, encoding="utf-8") as handle:
        source = handle.read()
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return []
    found = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Dict):
            continue
        keys = dict_keys(node)
        if "messageName" not in keys:
            continue
        value = None
        for key, val in zip(node.keys, node.values):
            if isinstance(key, ast.Constant) and key.value == "messageName":
                value = val
        name = resolve_message_name(value)
        if name:
            found.append({
                "file": os.path.relpath(path, ROOT),
                "line": node.lineno,
                "message": messages.get(name, name),
                "keys": [k for k in keys if k != "messageName"],
            })
    return found


def main():
    strict = "--strict" in sys.argv
    catalogue = json.load(open(PROTOCOL, encoding="utf-8"))["messages"]
    by_simple = {}
    for full, fields in catalogue.items():
        by_simple.setdefault(simple(full), fields)
    messages = enum_map()

    payloads = []
    for base in SCAN_DIRS:
        for directory, dirs, files in os.walk(base):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
            for name in files:
                if name.endswith(".py"):
                    payloads.extend(collect_payloads(os.path.join(directory, name), messages))

    problems = []
    checked = 0
    for payload in payloads:
        fields = by_simple.get(payload["message"])
        if fields is None:
            problems.append({**payload, "issue": "no such message type in the client"})
            continue
        checked += 1
        allowed = set(fields)
        unknown = [k for k in payload["keys"] if k not in allowed]
        missing = [k for k in allowed if k not in payload["keys"]]
        if unknown or missing:
            problems.append({**payload, "unknown": unknown, "missing": missing,
                             "allowed": sorted(allowed)})

    print(f"payloads inspected: {len(payloads)}  compared: {checked}  flagged: {len(problems)}")
    print("(only literal payload dictionaries are visible to this scan; values built "
          "through variables or ** unpacking are skipped)")
    for problem in problems:
        print(f"\n{problem['file']}:{problem['line']}  {problem['message']}")
        if problem["unknown"]:
            print(f"    extra keys the client does not declare: {problem['unknown']}")
        if problem["missing"]:
            print(f"    client keys never sent: {problem['missing']}")
        print(f"    client keys: {', '.join(problem['allowed'][:14])}"
              + (" …" if len(problem["allowed"]) > 14 else ""))

    if strict and problems:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
