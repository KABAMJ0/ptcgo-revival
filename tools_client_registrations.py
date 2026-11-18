"""Documents how the client registers messages, and what it registers.

`DwdModelAnalyzer` does not carry a table of message names: its registrars are
called from `dwd.core.data.ReflectionTypeInitializer.Initialize`, which sweeps the
assemblies and feeds it every type carrying `[DwdJsonMessage]`, `[DwdJsonEffect]`
or `[TypeHinting]`. That means the wire name of a message is the *type name*, and
polymorphic payloads are keyed by the type names carrying `[TypeHinting]`.

    python tools_client_registrations.py
        -> notes/client-registry.md
"""
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)

from tools_client_dump import Assembly, DEFAULT_DLLS, DEFAULT_DIR  # noqa: E402

OUT = os.path.join(ROOT, "notes", "client-registry.md")


def type_attrs(asm, position):
    return asm.type_attrs.get(position, [])


def collect(assemblies):
    messages, effects, hints = [], [], []
    for asm in assemblies:
        for position, name in asm.typedef_names.items():
            attrs = type_attrs(asm, position)
            key = asm.nested_name(position)
            base = asm.base_name(position)
            for attr in attrs:
                if "DwdJsonMessageAttribute" in attr:
                    messages.append((key, base, asm))
                elif "DwdJsonEffectAttribute" in attr:
                    effects.append((key, base, asm))
                elif "TypeHintingAttribute" in attr:
                    field = attr.rsplit(".", 1)[-1] if "." in attr else ""
                    hints.append((key, field, base, asm))
    return messages, effects, hints


def main():
    assemblies = []
    for dll in DEFAULT_DLLS:
        path = os.path.join(DEFAULT_DIR, dll)
        if os.path.exists(path):
            print(f"reading {dll}")
            assemblies.append(Assembly(path))

    messages, effects, hints = collect(assemblies)

    with open(OUT, "w", encoding="utf-8") as out:
        out.write("# Client message registry\n\n")
        out.write("Read from the assemblies by `tools_client_registrations.py`. "
                  "`DwdModelAnalyzer` is filled by `dwd.core.data.ReflectionTypeInitializer."
                  "Initialize`, which reflects over types rather than reading a literal "
                  "table — so the wire name of a message is the **CLR type name**, and the "
                  "type-hint map is keyed by the class names below.\n\n")
        out.write(f"- `[DwdJsonMessage]` types: **{len(messages)}**\n")
        out.write(f"- `[DwdJsonEffect]` types: **{len(effects)}**\n")
        out.write(f"- `[TypeHinting]` types: **{len(hints)}**\n\n")

        out.write("## Type hints (polymorphic payloads)\n\n")
        out.write("A field named in the second column carries a class name that selects "
                  "which of these types the client instantiates.\n\n")
        out.write("| type | hinting field | base |\n| --- | --- | --- |\n")
        for name, field, base, _ in sorted(hints):
            out.write(f"| `{name}` | `{field}` | `{base}` |\n")

        out.write("\n## JSON message types\n\n")
        out.write("Every type the client will deserialize as a wire message. Names here are "
                  "the exact `messageName` strings; shapes are in `client-protocol.md`.\n\n")
        for name, base, _ in sorted(messages):
            out.write(f"- `{name}` — base `{base}`\n")

        out.write("\n## JSON effect types\n\n")
        for name, base, _ in sorted(effects):
            out.write(f"- `{name}` — base `{base}`\n")

    print(f"wrote {OUT}: {len(messages)} messages, {len(effects)} effects, {len(hints)} hints")


if __name__ == "__main__":
    main()
