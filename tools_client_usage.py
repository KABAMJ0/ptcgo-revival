"""Which client classes touch each message type.

A message that nothing references is a message nothing in the UI waits for, and a
message referenced by a scene provider is one whose absence freezes that scene.
This reads notes/client-metadata.jsonl (already extracted) and maps message ->
classes, from field/property types and method signatures.

    python tools_client_usage.py
        -> notes/client-usage.md
"""
import collections
import json
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
METADATA = os.path.join(ROOT, "notes", "client-metadata.jsonl")
PROTOCOL = os.path.join(ROOT, "notes", "client-protocol.json")
OUT = os.path.join(ROOT, "notes", "client-usage.md")


def simple(name):
    return name.rsplit(".", 1)[-1].split("+")[-1]


def main():
    catalogue = json.load(open(PROTOCOL, encoding="utf-8"))["messages"]
    names = {simple(full) for full in catalogue}
    usage = collections.defaultdict(set)

    with open(METADATA, encoding="utf-8") as handle:
        for line in handle:
            record = json.loads(line)
            owner = simple(record["name"])
            if owner in names:
                continue
            mentions = set()
            for field in record.get("fields", []):
                for name in names:
                    if re.search(rf"\b{re.escape(name)}\b", field["type"]):
                        mentions.add(name)
            for prop in record.get("properties", []):
                for name in names:
                    if re.search(rf"\b{re.escape(name)}\b", prop["type"]):
                        mentions.add(name)
            for method in record.get("methods", []):
                text = f"{method.get('returns', '')} {' '.join(method.get('params', []))}"
                for name in names:
                    if re.search(rf"\b{re.escape(name)}\b", text):
                        mentions.add(name)
                if method["name"] in names:
                    mentions.add(method["name"])   # a facade method named after its message
            for name in mentions:
                usage[name].add(record["name"])

    with open(OUT, "w", encoding="utf-8") as out:
        out.write("# Who uses each client message\n\n")
        out.write("Built by `tools_client_usage.py` from `client-metadata.jsonl`: for each "
                  "message type, the classes that name it in a field, property or method "
                  "signature, or expose a method named after it.\n\n")
        out.write("This is a **lower bound**, not a usage oracle. The client subscribes to "
                  "most messages through generic base classes (`Subscription<EntityAdded>`) "
                  "or by type at runtime, and neither shows up as a concrete field type, so "
                  "a message in the unreferenced list below is still very likely in use. "
                  "What the map is good for: finding the class that owns a message when you "
                  "need to know what a screen does with it.\n\n")
        unanswered = [name for name in sorted(names) if name not in usage]
        out.write(f"- messages with a user: **{sum(1 for n in names if usage[n])}** of "
                  f"**{len(names)}**\n")
        out.write(f"- messages nothing references: **{len(unanswered)}**\n\n")

        out.write("## No direct type reference (see the caveat above)\n\n")
        out.write(", ".join(f"`{name}`" for name in unanswered) or "_None._")
        out.write("\n\n## Full map\n\n")
        for name in sorted(usage, key=lambda value: (-len(usage[value]), value)):
            owners = ", ".join(f"`{simple(owner)}`" for owner in sorted(usage[name]))
            out.write(f"- **{name}** ({len(usage[name])}) — {owners}\n")

    print(f"wrote {OUT}: {len(usage)} messages referenced, {len(unanswered)} unreferenced")


if __name__ == "__main__":
    main()
