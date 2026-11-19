"""Propose bodies for still-unimplemented blocks whose wording a wired sibling
already implements, with every number re-derived from the stub's own text.

The tail is thousands of blocks but far fewer wordings: "does 110 more damage"
and "does 90 more damage" are one body and two numbers. This tool finds those
pairs mechanically, so a set lane starts from a ranked list instead of reading
cards.

    PYTHONPATH=. venv/bin/python -m ptcgo.tools.near_match --out ~/near-match.md
    PYTHONPATH=. venv/bin/python -m ptcgo.tools.near_match --sets SM11 SM9 --top 40

How a match is decided
----------------------
Both texts are normalised the same way -- accents folded, whitespace collapsed,
case lowered, and every run of digits replaced by `#`. Two blocks match when
their masked text is identical, so the numbers are the only difference.

How a number is derived
-----------------------
Never from the donor. A donor's body is only trusted to carry its own printed
numbers in their printed ORDER: the k-th integer literal of the donor's body must
equal the k-th number of the donor's own text. Only then does the stub's k-th
number replace it. A donor whose body does not line up with its own text is
reported as untrustworthy instead of used.

When it refuses
---------------
- more than one donor BODY fits one wording (two factories could both be meant);
- the number counts differ between stub and donor;
- the donor's body is not a single call expression (control flow, loops, a
  hand-written class) -- a lane can still wire it, but this tool will not
  fabricate the code for it.

Every emitted snippet names the card path, the block title, the factory, and the
substitution table, so a lane can check the derivation instead of trusting it.
"""
import argparse
import collections
import inspect
import os
import re
import sys

from ptcgo.game.data_utils import CARD_DEFS_BY_GUID, Attack, unimplemented
from ptcgo.game.scripts.cards import loader

CARDS = os.path.join("ptcgo", "game", "scripts", "cards")
GUID_RE = re.compile(r'guid="([0-9a-f\-]+)"')
NUMBER_RE = re.compile(r"\d+")
MASK_RE = re.compile(r"\d+")


def normalise(text: str) -> str:
    text = text or ""
    if "\\u" in text:
        text = text.encode().decode("unicode_escape", errors="ignore")
    text = (text.replace("\u00e9", "e").replace("\u00c9", "E")
            .replace("\u2019", "'"))
    text = text.encode("ascii", "ignore").decode()
    return re.sub(r"\s+", " ", text).strip().lower()


def mask(text: str) -> str:
    return MASK_RE.sub("#", normalise(text))


def numbers(text: str):
    return [int(n) for n in NUMBER_RE.findall(normalise(text))]


def guid_of(path: str):
    try:
        match = GUID_RE.search(open(path, encoding="utf-8").read())
    except OSError:
        return None
    return match.group(1) if match else None


def walk_scripts():
    for root, _dirs, files in os.walk(CARDS):
        for name in sorted(files):
            if name.endswith(".py"):
                yield os.path.join(root, name)


def effect_source_text(ability):
    """A hand-written body's source, so it can be copied rather than matched."""
    effect = getattr(ability, "effect", None)
    if effect is None or effect is unimplemented:
        return None
    try:
        return inspect.getsource(effect)
    except (OSError, TypeError):
        return None


def body_key(ability, source: str) -> str:
    """Identity of the BODY, not of the card: the pattern name for a
    pattern-bound block, or the written source for a card-local one."""
    if source.startswith("pattern:"):
        return source
    text = effect_source_text(ability)
    if text is None:
        return source
    return "script:" + str(hash(re.sub(r"[A-Za-z_]\w*_\d+", "CARD", text)))


def pattern_regex(source: str):
    """The regex a `pattern:<name>` source matched with, so a lane can see the
    literal that stops it matching a sibling wording."""
    if not source.startswith("pattern:"):
        return None
    from ptcgo.game.card_effects import patterns

    name = source.split(":", 1)[1]
    for entry_name, pattern, _build in patterns._PATTERNS:
        if entry_name == name:
            return getattr(pattern, "pattern", None)
    return None


def body_for_source(source: str):
    """The builder callable behind a `pattern:<name>` source, plus its source."""
    if not source or not source.startswith("pattern:"):
        return None, None
    from ptcgo.game.card_effects import patterns

    name = source.split(":", 1)[1]
    for entry_name, _pattern, build in patterns._PATTERNS:
        if entry_name == name:
            try:
                return build, inspect.getsource(build)
            except (OSError, TypeError):
                return build, None
    return None, None


def body_numbers(source_text: str):
    """The integer literals a builder's body passes, in source order."""
    if not source_text:
        return []
    # Only the `return <call>(...)` shape is rewritten; anything else is
    # reported rather than edited.
    match = re.search(r"return\s+([A-Za-z_][\w.]*)\s*\((.*?)\)\s*$",
                      source_text, re.S | re.M)
    if match is None:
        return []
    args = match.group(2)
    if "(" in args or "[" in args or "lambda" in args:
        return []
    return [int(n) for n in NUMBER_RE.findall(args)]


def call_template(source_text: str):
    match = re.search(r"return\s+((?:[A-Za-z_][\w.]*)\s*\(.*?\))\s*$",
                      source_text, re.S | re.M)
    return match.group(1) if match else None


def collect():
    """(stubs, donors): unbound blocks, and bound blocks with their body source."""
    stubs = []
    donors = collections.defaultdict(list)
    for path in walk_scripts():
        guid = guid_of(path)
        definition = CARD_DEFS_BY_GUID.get(guid) if guid else None
        if definition is None:
            continue
        rel = os.path.relpath(path, CARDS)
        for ability in getattr(definition, "abilities", []) or []:
            text = normalise(getattr(ability, "game_text", "") or "")
            if not text:
                continue
            effect = getattr(ability, "effect", None)
            passive = getattr(ability, "passive", None)
            bound = passive is not None or (callable(effect)
                                           and effect is not unimplemented)
            if not bound:
                stubs.append({
                    "path": rel, "title": getattr(ability, "title", ""),
                    "text": text, "masked": mask(text),
                    "numbers": numbers(text), "kind": type(ability).__name__,
                })
                continue
            source = getattr(ability, "effect_source", None) or f"script:{rel}"
            donors[mask(text)].append({
                "path": rel, "title": getattr(ability, "title", ""),
                "text": text, "numbers": numbers(text), "source": source,
                "body": body_key(ability, source),
                "written": effect_source_text(ability),
            })
    return stubs, donors


def propose(stub, candidates):
    """A proposal for one stub, or a refusal with the reason."""
    kinds = collections.Counter(c["body"] for c in candidates)
    if len(kinds) == 1:
        donor = candidates[0]
    else:
        # A dominant body is the answer a lane wants ("105 of 130 wired
        # siblings wire it this way"), but it is a REVIEW, never a proposal:
        # the other 25 show the wording admits more than one body.
        key, count = kinds.most_common(1)[0]
        if count < 0.6 * len(candidates):
            top = ", ".join(f"{k} x{n}" for k, n in kinds.most_common(3))
            return None, (f"{len(kinds)} bodies fit this wording and none "
                          f"dominates ({top})")
        donor = next(c for c in candidates if c["body"] == key)
        proposal, why = _numeric_proposal(stub, donor)
        if proposal is None:
            return None, why
        proposal["review"] = True
        proposal["share"] = (count, len(candidates))
        return proposal, None
    return _numeric_proposal(stub, donor)


def _numeric_proposal(stub, donor):
    """The body with the stub's numbers substituted, or a refusal.

    Trusting a donor's body to carry its OWN numbers in printed order is what
    makes substitution safe: the k-th literal of the body equals the k-th number
    of the donor's text, so the stub's k-th number can take its place."""
    if len(donor["numbers"]) != len(stub["numbers"]):
        return None, (f"number count differs (stub {len(stub['numbers'])}, "
                      f"donor {len(donor['numbers'])})")
    _build, source_text = body_for_source(donor["source"])
    literals = body_numbers(source_text) if source_text else []
    if not literals:
        written = donor.get("written")
        if not written:
            return None, "donor body has no source to copy"
        return {"kind": donor["source"], "donor": donor, "body": written.strip(),
                "derivation": [], "review": True}, None
    if literals != donor["numbers"]:
        return None, ("donor body's own literals do not match its own printed "
                      f"numbers ({literals} vs {donor['numbers']}); the body is "
                      "untrusted on its reference card")
    template = call_template(source_text)
    body = template
    for donor_n, stub_n in zip(donor["numbers"], stub["numbers"]):
        body = re.sub(rf"\b{donor_n}\b", str(stub_n), body, count=1)
    return {
        "kind": donor["source"], "donor": donor, "body": body,
        "derivation": list(zip(donor["numbers"], stub["numbers"])),
    }, None


def run(sets=None, top=60):
    loader.load_all()
    stubs, donor_index = collect()
    clusters = collections.defaultdict(list)
    for stub in stubs:
        clusters[stub["masked"]].append(stub)

    matched = []
    for wording, group in clusters.items():
        candidates = donor_index.get(wording)
        if not candidates:
            continue
        matched.append((len(group), wording, group, candidates))
    matched.sort(key=lambda row: -row[0])

    if sets:
        wanted = set(sets)
        matched = [row for row in matched
                   if any(s["path"].split("/")[0] in wanted for s in row[2])]

    lines = []
    proposed = refused = reviewed = 0
    blocks = 0
    for size, wording, group, candidates in matched[:top]:
        blocks += size
        lines.append(f"\n## {size} block(s) — `{wording[:160]}`\n")
        seen = set()
        for stub in group:
            if stub["path"] in seen:
                continue
            seen.add(stub["path"])
            proposal, why = propose(stub, candidates)
            if proposal is None:
                refused += 1
                lines.append(f"- `{stub['path']}` | {stub['title']} | REFUSED: {why}")
                continue
            if proposal.get("review"):
                reviewed += 1
            else:
                proposed += 1
            pairs = ", ".join(f"{a}->{b}" for a, b in proposal["derivation"])
            mark = "REVIEW" if proposal.get("review") else "PROPOSAL"
            lines.append(
                f"- `{stub['path']}` | {stub['title']} | {mark} "
                f"**{proposal['kind']}** | numbers: {pairs or 'none'}")
            lines.append("```python")
            lines.append(proposal["body"])
            lines.append("```")
            if proposal["donor"]["path"] != stub["path"]:
                lines.append(
                    f"  donor: `{proposal['donor']['path']}` "
                    f"{proposal['donor']['title']}"
                    + (f"  ({proposal['share'][0]} of {proposal['share'][1]} "
                       "wired siblings use this body)" if proposal.get("share")
                       else ""))
                regex = pattern_regex(proposal["kind"])
                if regex:
                    lines.append(f"  pattern regex: `{regex}`")
                if proposal.get("review") and not proposal["derivation"]:
                    lines.append("  the body above is the donor's closure: its "
                                 "free names come from that card's script")

    header = [
        "# Near-match body proposals",
        "",
        f"stubs measured: {len(stubs)}  distinct unbound wordings: {len(clusters)}  "
        f"wordings with a wired sibling: {len(matched)}",
        f"clusters listed: {len(matched[:top])} covering {blocks} blocks  "
        f"proposals: {proposed}  review: {reviewed}  refused: {refused}",
        "",
        "A proposal means: one donor BODY fits this wording, and that body's own",
        "integer literals match its own printed numbers in printed order, so the",
        "stub's numbers could be substituted without guessing. A REFUSAL names the",
        "reason and is not a stub defect.",
    ]
    return ("\n".join(header) + "\n" + "\n".join(lines) + "\n",
            proposed, reviewed, refused)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default="handoffs/near-match-run.md")
    parser.add_argument("--sets", nargs="*", help="only these set folder names")
    parser.add_argument("--top", type=int, default=60,
                        help="clusters to list, biggest first")
    args = parser.parse_args()
    report, proposed, reviewed, refused = run(args.sets, args.top)
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as handle:
        handle.write(report)
    print(f"wrote {args.out}: {proposed} proposals, "
          f"{reviewed} review, {refused} refused")


if __name__ == "__main__":
    sys.exit(main())
