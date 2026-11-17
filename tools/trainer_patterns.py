"""Trainer rules-text patterns -> shared effect factories.

The card pool repeats itself: "Draw 3 cards." is printed in four sets, "Search
your deck for a Basic Pokemon..." in a dozen wordings across twenty years of
type names. This table turns that repetition into one wired implementation per
SHAPE, with the card's own numbers and type names as arguments, so a script
stays data and the behaviour lives in spirit/game/card_effects/trainers.py and
support_common.py.

Every pattern is anchored at both ends against `trainer_coverage.canonical_text`:
lowercase, class reminder sentences stripped, number words and articles turned
into digits, every punctuation mark turned into a space. That anchoring is the
safety property that matters: a card whose printed text deviates by even one
clause does NOT match, stays `effect=unimplemented`, and keeps doing nothing
rather than doing the wrong thing. When a phrase cannot be resolved into a
predicate the rule declines (`Unresolved`) instead of guessing.

A captured quantity is the count the card names; a captured category phrase is
resolved to a predicate expression by `resolve_predicate`.
"""

import re


class Unresolved(Exception):
    """The rule matched but a phrase inside it has no implementation."""


# --- Phrase -> predicate ----------------------------------------------------

# Predicate names are all importable from spirit.game.card_effects.trainers.
SIMPLE_PREDICATES = {
    "pokemon": "is_pokemon_card",
    "basic pokemon": "is_basic_pokemon",
    "evolution pokemon": "is_evolution_pokemon",
    "evolution card": "is_evolution_pokemon",
    "stage 1 pokemon": "is_stage_one",
    "stage 2 pokemon": "is_stage_two",
    "pokemon that doesnt have 1 rule box": "is_rule_box_free_pokemon",
    "basic pokemon that doesnt have 1 rule box": "all_of(is_basic_pokemon, is_rule_box_free_pokemon)",
    "pokemon ex": "is_pokemon_ex",
    "pokemon that has any damage counters on it": "is_damaged_pokemon",
    "pokemon that dont have 1 rule box": "is_rule_box_free_pokemon",
    "pokemon that doesnt have 1 rule box": "is_rule_box_free_pokemon",
    "pokemon gx": "is_pokemon_gx",
    "pokemon vstar": "is_pokemon_vstar",
    "item card": "is_item_card",
    "supporter card": "is_supporter_card",
    "stadium card": "is_stadium_card",
    "pokemon tool card": "is_tool_card",
    "trainer card": "is_trainer_card",
    "basic energy card": "is_basic_energy_card",
    "basic energy": "is_basic_energy_card",
    "energy card": "is_energy_card",
    "energy": "is_energy_card",
    "special energy card": "is_special_energy",
    "special energy": "is_special_energy",
    "card": "None",
    "baby pokemon": 'pokemon_of_subtype("Baby")',
    "judge card": 'named_exactly("Judge")',
    "unidentified fossil card": 'named_exactly("Unidentified Fossil")',
}

TYPE_NAMES = "grass|fire|water|lightning|psychic|fighting|darkness|metal|fairy|dragon|colorless"

# Possessive trainer names that appear inside a card category
# ("Team Rocket's Pokemon", "Ethan's Pokemon"). Canonical text drops the
# apostrophe, so the key is the printed name without it.
OWNER_NAMES = {
    "team rockets": "team rocket", "ethans": "ethan", "cynthias": "cynthia",
    "stevens": "steven", "marnies": "marnie", "arvens": "arven", "hops": "hop",
    "ns": "n", "ionos": "iono", "mistys": "misty", "brocks": "brock",
    "erikas": "erika", "sabrinas": "sabrina", "blaines": "blaine",
    "giovannis": "giovanni", "surges": "surge", "lanas": "lana",
    "guzmas": "guzma", "lusamines": "lusamine", "sadas": "sada",
    "turos": "turo", "nemonas": "nemona", "kukuis": "kukui", "draytons": "drayton",
    "cyllenes": "cyllene", "colresss": "colress", "klaras": "klara", "lillies": "lillie",
}

_TYPED_ENERGY = re.compile(
    r"^(?:1 |up to )?basic (?P<type>%s) energy cards?$" % TYPE_NAMES)
_TYPED_ENERGY_ANY = re.compile(r"^(?:1 )?(?P<type>%s) energy cards?$" % TYPE_NAMES)
_TYPED_POKEMON = re.compile(r"^(?:1 )?(?P<type>%s) pokemon$" % TYPE_NAMES)
_BASIC_TYPED_POKEMON = re.compile(
    r"^(?:1 )?basic (?P<type>%s) pokemon$" % TYPE_NAMES)


def resolve_predicate(phrase):
    """Expression source for a printed card-category phrase, or Unresolved.

    Returns the string "None" when the phrase means "any card", and raises
    Unresolved for a phrase with no implementation, which makes the whole rule
    decline rather than pick a wrong filter.
    """
    text = re.sub(r"\s+", " ", (phrase or "").strip().lower())
    text = re.sub(r" and or ", " or ", text)
    text = re.sub(r"^(up to|any number of) ", "", text)
    bare = re.sub(r" cards?$", "", text)
    if text not in SIMPLE_PREDICATES and bare in SIMPLE_PREDICATES:
        text = bare
    text = re.sub(r"^(1|a|an) ", "", text)
    combination = _any_combination(text)
    if combination is not None:
        return combination
    text = re.sub(r"^in any combination of ", "", text)
    text = re.sub(r" in any combination$", "", text)
    if text in SIMPLE_PREDICATES:
        return SIMPLE_PREDICATES[text]
    singular = re.sub(r"(?:es|s)$", "", text)
    if singular in SIMPLE_PREDICATES:
        return SIMPLE_PREDICATES[singular]
    match = _TYPED_ENERGY.match(text) or _TYPED_ENERGY_ANY.match(text)
    if match:
        return 'basic_energy_of("%s")' % match.group("type")
    match = _TYPED_POKEMON.match(text)
    if match:
        return 'pokemon_of("%s")' % match.group("type")
    match = _BASIC_TYPED_POKEMON.match(text)
    if match:
        return 'all_of(is_basic_pokemon, pokemon_of("%s"))' % match.group("type")
    excluded = _excluding(text)
    if excluded is not None:
        return excluded
    subtype = _subtype_category(text)
    if subtype is not None:
        return subtype
    owned = _owned_category(text)
    if owned is not None:
        return owned
    distributed = _distribute_noun(text)
    if distributed is not None:
        try:
            return _combine(distributed, "any_of")
        except Unresolved:
            pass
    for joiner, combinator in ((" or ", "any_of"),):
        if joiner in text:
            # "Basic Pokemon, Evolution card, or Energy card" loses its comma,
            # so the first choice still reads "basic pokemon evolution card".
            expanded = []
            for part in text.split(joiner):
                if part.startswith("basic pokemon ") and part != "basic pokemon":
                    expanded.extend(["basic pokemon", part[len("basic pokemon "):]])
                else:
                    expanded.append(part)
            parts = [resolve_predicate(part) for part in expanded]
            parts = [part for part in parts if part != "None"]
            if len(parts) > 1:
                return "%s(%s)" % (combinator, ", ".join(parts))
    raise Unresolved(phrase)


def _count(value, default=1):
    """A captured quantity ("up to 2", "2") as an int."""
    if value is None or value == "":
        return default
    try:
        return int(value)
    except ValueError:
        raise Unresolved(value)


def _any_combination(text):
    """"in any combination of supporter and stadium cards" -> any_of(...).

    The phrase means "a mix of either kind", so the parts are OR-ed. A plain
    "X and Y" phrase without it is NOT OR-ed: "an Item card and a Pokemon Tool
    card" asks for one of each and must not collapse into a single filter, so
    those decline instead.
    """
    prefix = "in any combination of "
    if not text.startswith(prefix):
        return None
    parts = [part.strip() for part in text[len(prefix):].split(" and ")]
    resolved = []
    for part in parts:
        expression = None
        for suffix in ("", " card", " cards"):
            try:
                expression = resolve_predicate(part + suffix)
                break
            except Unresolved:
                continue
        if expression is None:
            return None
        if expression != "None":
            resolved.append(expression)
    if not resolved:
        return None
    return resolved[0] if len(resolved) == 1 else "any_of(%s)" % ", ".join(resolved)


_CATEGORY_NOUNS = ("pokemon", "card", "cards", "energy")


def _distribute_noun(text):
    """"psychic or dragon pokemon" -> ['psychic pokemon', 'dragon pokemon']."""
    if " or " not in text:
        return None
    parts = [part.strip() for part in text.split(" or ")]
    last = parts[-1].split()
    if not last:
        return None
    noun = last[-1] if last[-1] in _CATEGORY_NOUNS else None
    if noun is None:
        return None
    filled = []
    for part in parts:
        if part.split()[-1] in _CATEGORY_NOUNS:
            filled.append(part)
        else:
            filled.append(part + " " + noun)
    return filled


def _combine(parts, combinator):
    """Resolve every phrase in `parts` and combine them."""
    expressions = []
    for part in parts:
        expression = resolve_predicate(part)
        if expression != "None":
            expressions.append(expression)
    if len(expressions) < 2:
        raise Unresolved(" or ".join(parts))
    return "%s(%s)" % (combinator, ", ".join(expressions))


def _excluding(text):
    """"basic pokemon excluding pokemon ex" -> all_of(category, excluding(ex))."""
    if " excluding " not in text:
        return None
    base, _, excluded = text.partition(" excluding ")
    try:
        category = resolve_predicate(base)
        rejection = resolve_predicate(excluded)
    except Unresolved:
        return None
    if rejection == "None":
        return None
    return "all_of(%s, excluding(%s))" % (category, rejection)


SUBTYPE_PHRASES = {
    "mega evolution pokemon ex": "MEGA",
    "ancient pokemon": "Ancient",
    "future pokemon": "Future",
    "tera pokemon": "Tera",
    "ultra beast": "Ultra Beast",
}


def _subtype_category(text):
    """Subtypes whose printed name is not a type or stage word."""
    for phrase, subtype in SUBTYPE_PHRASES.items():
        if phrase == text or text.endswith(phrase):
            prefix = text[:-len(phrase)].strip()
            if not prefix:
                return 'pokemon_of_subtype("%s")' % subtype
            try:
                category = resolve_predicate(prefix)
            except Unresolved:
                return None
            return "all_of(%s, pokemon_of_subtype(%s))" % (category, '"%s"' % subtype)
    return None


def _owned_category(text):
    """'evolution team rockets pokemon' -> all_of(is_evolution_pokemon,
    named("team rocket")); None when the phrase is not owner-qualified."""
    tokens = text.split()
    for owner_form, owner_word in OWNER_NAMES.items():
        wanted = owner_form.split()
        span = len(wanted)
        start = next((i for i in range(len(tokens) - span + 1)
                      if tokens[i:i + span] == wanted), None)
        if start is None:
            continue
        remainder = " ".join(tokens[:start] + tokens[start + span:])
        if not remainder:
            raise Unresolved(text)
        owner = 'owned_by("%s")' % owner_word
        try:
            category = resolve_predicate(remainder)
        except Unresolved:
            return None
        if category == "None":
            return owner
        return "all_of(%s, %s)" % (category, owner)
    return None


_CONDITIONS = {
    "asleep": "SpecialConditions.ASLEEP", "burned": "SpecialConditions.BURNED",
    "confused": "SpecialConditions.CONFUSED",
    "paralyzed": "SpecialConditions.PARALYZED",
    "poisoned": "SpecialConditions.POISONED",
}


def _condition(word):
    """Source for a SpecialConditions member; declines on anything else."""
    try:
        return _CONDITIONS[word]
    except KeyError:
        raise Unresolved(word)


def _active_subtype(phrase):
    """'1 tag team pokemon' -> 'TAG TEAM' (the printed subtype name)."""
    text = re.sub(r"\s+", " ", phrase.strip().lower())
    text = re.sub(r"^(1 )?", "", text)
    text = re.sub(r" pokemon$", "", text)
    if not text:
        raise Unresolved(phrase)
    return text.upper()


def _typed_or_decline(word):
    """A Pokemon type name, or the rule declines."""
    if word not in TYPE_NAMES.split("|"):
        raise Unresolved(word)
    return '"%s"' % word


def _colorless_count(phrase):
    """'colorless' -> 1, 'colorless colorless' -> 2 (energy icons concatenate)."""
    return max(1, phrase.count("colorless"))


def _tool_takes_less(match):
    """Arguments for a typical tool's damage reduction; declines on an
    owner-specific qualifier it cannot express."""
    holder_type = match.group("type")
    if holder_type in (None, "pokemon"):
        return [match.group("amount")]
    if holder_type not in TYPE_NAMES.split("|"):
        raise Unresolved(holder_type)
    return [match.group("amount"), 'protect_type="%s"' % holder_type]


def _typed_boost(match):
    """Arguments for a type-restricted damage boost; declines on a non-type."""
    if match.group("type") not in TYPE_NAMES.split("|"):
        raise Unresolved(match.group("type"))
    return [match.group("amount"), 'pokemon_type="%s"' % match.group("type")]


def _pred(phrase):
    """Predicate source for a captured category phrase; Unresolved declines."""
    return resolve_predicate(phrase)


_NAMED_RULE_BOX = re.compile(r"^(?P<name>[a-z][a-z ]*?) (?P<suffix>ex|gx)$")


def _holder(phrase):
    """Predicate source for a tool's holder phrase; plain "pokemon" is any,
    and a named "<pokemon> ex/gx" holder matches that Pokemon by name."""
    text = phrase.strip()
    if text == "pokemon":
        return "None"
    if text in TYPE_NAMES.split("|"):
        return 'pokemon_of("%s")' % text
    try:
        resolved = resolve_predicate(text)
    except Unresolved:
        named = _NAMED_RULE_BOX.match(text)
        if named is None or named.group("name") in ("pokemon", "ultra beast"):
            raise
        return 'named_rule_box("%s", "%s")' % (named.group("name"), named.group("suffix"))
    if resolved == "None":
        raise Unresolved(phrase)
    return resolved


def _attacker_types(phrase):
    """Attacker-type list ("grass fire water or lightning") -> predicate."""
    words = [word for word in phrase.replace(" or ", " ").split() if word]
    if not words or any(word not in TYPE_NAMES.split("|") for word in words):
        raise Unresolved(phrase)
    return "attacker_of_types(%s)" % ", ".join('"%s"' % word for word in words)


def _name_choice(phrase):
    """A printed "A or B" choice of Pokemon names -> a name predicate.

    Canonical text turns the printed commas into spaces, so a list of three or
    more names is indistinguishable from a multi-word name: only a single
    "or" resolves."""
    parts = [part.strip() for part in phrase.split(" or ")]
    if len(parts) != 2 or any(" " in part or not part for part in parts):
        raise Unresolved(phrase)
    return "named_one_of(%s)" % ", ".join('"%s"' % part for part in parts)


_STADIUM_CATEGORY_SUBTYPES = {
    "pokemon sp": "SP", "pokemon team plasma": "Team Plasma",
}


def _stadium_cat(phrase):
    """A both-sides stadium's affected-Pokemon phrase -> predicate source.

    "psychic and darkness pokemon" means either type, and a bare type name is
    a Pokemon of that type, so the parts join with any_of."""
    text = re.sub(r" (?:in|is) play$", "", phrase.strip())
    if text in _STADIUM_CATEGORY_SUBTYPES:
        return 'pokemon_of_subtype("%s")' % _STADIUM_CATEGORY_SUBTYPES[text]
    basic_non = re.match(r"^basic non (?P<type>[a-z]+)(?: pokemon)?$", text)
    if basic_non:
        return 'all_of(is_basic_pokemon, excluding(pokemon_of("%s")))' % basic_non.group("type")
    energy = re.match(r"^pokemon that has any (?P<types>[a-z ]+?) energy attached to it$", text)
    if energy:
        words = [w for w in energy.group("types").replace(" or ", " ").split() if w]
        if words and all(w in TYPE_NAMES.split("|") for w in words):
            return "has_energy_of(%s)" % ", ".join('"%s"' % w for w in words)
        raise Unresolved(phrase)
    dark = re.match(r"^pokemon with (?P<word>[a-z]+) in its name$", text)
    if dark:
        return 'pokemon_named("%s")' % dark.group("word")
    if text.endswith(" pokemon"):
        text = text[:-len(" pokemon")]
    parts = [_type_or_predicate(part) for part in text.split(" and ")]
    return parts[0] if len(parts) == 1 else "any_of(%s)" % ", ".join(parts)


def _type_or_predicate(phrase):
    """A bare type name is a Pokemon of that type; else a full predicate."""
    text = phrase.strip()
    if text in TYPE_NAMES.split("|"):
        return 'pokemon_of("%s")' % text
    if text == "pokemon":
        return "is_pokemon_card"
    return resolve_predicate(text)


def _subtype_literal(phrase):
    """'ultra beasts' -> '"Ultra Beast"' (the printed subtype name)."""
    text = re.sub(r"^(\d+ )?", "", phrase.strip())
    text = re.sub(r"s$", "", text)
    if not text:
        raise Unresolved(phrase)
    return '"%s"' % text.title()


_TYPED_SUBTYPE = re.compile(r"^(?P<type>[a-z]+) pokemon (?P<sub>gx|ex|v|vmax|vstar)$")


def _pred_typed_subtype(phrase):
    """'lightning pokemon gx' -> type + subtype predicate; else Unresolved."""
    found = _TYPED_SUBTYPE.match(phrase.strip())
    if found is None:
        raise Unresolved(phrase)
    return 'pokemon_type_subtype("%s", "%s")' % (found.group("type"), found.group("sub"))


def _who(phrase):
    """Predicate source for a named card in a deck-reveal ("1 Tirtouga"):
    a known category resolves normally, a bare name becomes a name match."""
    text = phrase.strip()
    try:
        return _pred(text)
    except Unresolved:
        if not text or " " in text:
            raise
        return 'card_named_contains("%s")' % text


def _union(phrase):
    """A stadium's "<X> pokemon and <Y> pokemon" names every Pokemon that is
    either, so the parts join with any_of."""
    text = phrase.strip()
    if text == "pokemon":
        return "is_pokemon_card"
    parts = [resolve_predicate(part) for part in text.split(" and ")]
    if "None" in parts:
        raise Unresolved(phrase)
    return parts[0] if len(parts) == 1 else "any_of(%s)" % ", ".join(parts)


# --- Rules ------------------------------------------------------------------

class Rule:
    __slots__ = ("rule_id", "pattern", "factory", "module", "builder", "bare", "kind")

    def __init__(self, rule_id, pattern, factory, builder, module="trainers",
                 bare=False, kind="effect"):
        self.rule_id = rule_id
        self.pattern = re.compile(pattern + r"\Z")
        self.factory = factory
        self.module = module
        self.builder = builder
        # bare: the factory IS a `async def effect(ctx)` coroutine (Switch),
        # so the script passes it directly instead of calling a factory.
        self.bare = bare
        # effect: `effect=<factory>(...)`. passive: `passive=<factory>(...)`
        # for a tool/stadium's continuous stat effect.
        self.kind = kind

    def match(self, text):
        found = self.pattern.match(text)
        if not found:
            return None
        try:
            args = self.builder(found)
        except Unresolved:
            return None
        if args is None:
            return None
        expression = self.factory if self.bare \
            else "%s(%s)" % (self.factory, ", ".join(args))
        return {"rule": self.rule_id, "expr": expression, "kind": self.kind,
                "symbols": {self.factory} | _argument_symbols(args)}


# A card-category clause; the surrounding literal text pins its boundaries.
CAT = r"(?P<cat>[a-z0-9][a-z0-9 ]*?)"

# Printings differ only in how the deck shuffle is phrased; all forms mean
# the same thing, so one fragment covers them.
SHUFFLE_TAIL = r"(?: then)? shuffle your deck(?: afterward)?"

RULES = [
    # --- Draw -------------------------------------------------------------
    Rule("draw", r"draw (?P<n>\d+) cards?", "draw_n",
         lambda m: [m.group("n")]),
    Rule("draw-until", r"draw cards?(?: from your deck)? until you have (?P<n>\d+) cards? in your hand",
         "draw_until_effect", lambda m: [m.group("n")], module="support_common"),
    Rule("discard-hand-draw",
         r"discard your hand and draw (?P<n>\d+) cards?", "discard_hand_draw",
         lambda m: [m.group("n")]),
    Rule("shuffle-hand-draw",
         r"shuffle your hand into your deck then draw (?P<n>\d+) cards?",
         "shuffle_hand_draw", lambda m: [m.group("n")]),
    Rule("each-shuffle-draw",
         r"each player shuffles (?:their|his or her) hand into (?:their|his or her) deck "
         r"and draws (?P<n>\d+) cards?",
         "each_player_shuffle_draw", lambda m: [m.group("n")]),
    Rule("opp-shuffle-draw",
         r"your opponent shuffles (?:their|his or her) hand into (?:their|his or her) deck "
         r"then draws (?P<n>\d+) cards?",
         "opponent_shuffle_hand_draw", lambda m: [m.group("n")]),

    # --- Deck search into hand -------------------------------------------
    Rule("search-hand-up-to",
         r"search your deck for (?:up to )?(?P<n>\d+ )?" + CAT +
         r" reveal (?:it|them)(?: to your opponent)? and put (?:it|them) into your hand" +
         SHUFFLE_TAIL,
         "search_to_hand",
         lambda m: [_pred(m.group("cat")), "count=" + str(_count(m.group("n")))],
         module="support_common"),
    Rule("search-hand-show",
         r"search your deck for (?:up to )?(?P<n>\d+ )?" + CAT +
         r" (?:reveal|show) (?:it|them)(?: to your opponent)? and put (?:it|them) into your " +
         r"hand" + SHUFFLE_TAIL,
         "search_to_hand",
         lambda m: [_pred(m.group("cat")), "count=" + str(_count(m.group("n")))],
         module="support_common"),
    Rule("search-hand-show-that",
         r"search your deck for (?:up to |any )?(?P<n>\d+ )?" + CAT +
         r" (?:reveal|show) that card(?:s)?(?: to your opponent)? then put (?:it|them) into your "
         r"hand" + SHUFFLE_TAIL,
         "search_to_hand",
         lambda m: [_pred(m.group("cat")), "count=" + str(_count(m.group("n")))],
         module="support_common"),
    Rule("search-hand-named-qualifier",
         r"search your deck for (?:up to )?(?P<n>\d+ )?(?P<base>[a-z0-9 ]+?) with "
         r"(?P<word>[a-z]+) in its name (?:reveal|show) (?:it|them)(?: to your opponent)? and put "
         r"(?:it|them) into your hand" + SHUFFLE_TAIL,
         "search_to_hand",
         lambda m: ["all_of(%s, card_named_contains(\"%s\"))"
                    % (_pred(m.group("base")), m.group("word")),
                    "count=" + str(_count(m.group("n")))],
         module="support_common"),
    Rule("search-hand-plain",
         r"search your deck for (?:up to )?(?P<n>\d+ )?" + CAT +
         r" and put (?:it|them) into your hand" + SHUFFLE_TAIL,
         "search_to_hand",
         lambda m: [_pred(m.group("cat")), "count=" + str(_count(m.group("n")))],
         module="support_common"),
    Rule("search-bench",
         r"search your deck for (?:up to )?(?P<n>\d+ )?" + CAT +
         r" and put (?:it|them) onto your bench" + SHUFFLE_TAIL,
         "search_to_bench",
         lambda m: [_pred(m.group("cat")), str(_count(m.group("n")))],
         module="support_common"),
    Rule("search-bench-low-hp",
         r"search your deck for (?:up to )?(?P<n>\d+) basic pokemon with (?P<hp>\d+) hp or "
         r"less and put (?:it|them) onto your bench" + SHUFFLE_TAIL,
         "search_to_bench",
         lambda m: ["is_basic_pokemon_with_hp_at_most(%s)" % m.group("hp"),
                    str(_count(m.group("n")))],
         module="support_common"),

    # --- Discard pile recursion ------------------------------------------
    Rule("recover-to-hand",
         r"put (?:up to )?(?P<n>\d+ )?" + CAT + r" from your discard pile into your hand",
         "recover_from_discard",
         lambda m: [_pred(m.group("cat")),
                    "count=" + str(_count(m.group("n"))), 'to="hand"'],
         module="support_common"),
    Rule("recover-to-deck",
         r"shuffle (?:up to )?(?P<n>\d+ )?" + CAT + r" from your discard pile into your deck",
         "recover_from_discard",
         lambda m: [_pred(m.group("cat")),
                    "count=" + str(_count(m.group("n"))), 'to="deck_shuffle"'],
         module="support_common"),
    Rule("recover-to-deck-then-draw",
         r"shuffle (?:up to )?(?P<n>\d+ )?" + CAT +
         r" from your discard pile into your deck if you shuffled any cards into your deck "
         r"in this way draw (?P<draw>\d+) cards?",
         "recover_then_draw",
         lambda m: [_pred(m.group("cat")),
                    "count=" + str(_count(m.group("n"))), "draw=" + m.group("draw")]),

    # --- Heal -------------------------------------------------------------
    Rule("heal-one",
         r"heal (?P<amount>\d+) damage from (?P<n>\d+) of your pokemon",
         "heal_item", lambda m: ["amount=" + m.group("amount"), 'scope="choice"'],
         module="support_common"),
    Rule("heal-one-typed",
         r"heal (?P<amount>\d+) damage from (?P<n>\d+) of your (?P<type>[a-z]+) pokemon",
         "heal_item",
         lambda m: ["amount=" + m.group("amount"), 'scope="choice"'],
         module="support_common"),
    Rule("heal-each-own",
         r"heal (?P<amount>\d+) damage from each of your pokemon",
         "heal_item", lambda m: ["amount=" + m.group("amount"), 'scope="each_own"'],
         module="support_common"),
    Rule("heal-all-one",
         r"heal all damage from (?P<n>\d+) of your pokemon",
         "heal_all_from_one", lambda m: [], module="support_common"),
    Rule("remove-counters",
         r"remove (?:up to )?(?P<counters>\d+) damage counters? from (?P<n>\d+) of your pokemon"
         r"(?: remove \d+ damage counters? if that pokemon has only \d+)?",
         "heal_item",
         lambda m: ["amount=" + str(int(m.group("counters")) * 10), 'scope="choice"'],
         module="support_common"),
    Rule("remove-counters-each",
         r"remove (?P<counters>\d+) damage counters? from each of your pokemon",
         "heal_item",
         lambda m: ["amount=" + str(int(m.group("counters")) * 10), 'scope="each_own"'],
         module="support_common"),
    Rule("heal-and-cure",
         r"heal (?P<amount>\d+) damage from (?P<n>\d+) of your pokemon and remove all "
         r"special conditions from (?:it|that pokemon)",
         "heal_item",
         lambda m: ["amount=" + m.group("amount"), 'scope="choice"',
                    "condition_cure=True"],
         module="support_common"),

    # --- Switching --------------------------------------------------------
    Rule("switch-self", r"switch (?:1 of )?your active pokemon with (?P<n>\d+) of your benched pokemon",
         "switch", lambda m: [], bare=True),
    Rule("switch-self-draw",
         r"switch (?:1 of )?your active pokemon with (?P<n>\d+) of your benched pokemon if you do draw "
         r"cards until you have (?P<draw>\d+) cards in your hand",
         "switch_then_draw_until", lambda m: [m.group("draw")]),
    Rule("gust",
         r"switch in (?P<n>\d+) of your opponents? benched pokemon to the active spot",
         "opponent_bench_to_active", lambda m: []),
    Rule("gust-flip",
         r"flip 1 coin if heads switch in (?P<n>\d+) of your opponents? benched pokemon to "
         r"the active spot",
         "opponent_bench_to_active", lambda m: ["flip=True"]),
    Rule("gust-opponent-chooses",
         r"switch your opponents? active pokemon with (?P<n>\d+) of (?:his or her|their) "
         r"benched pokemon",
         "opponent_bench_to_active", lambda m: ["opponent_chooses=True"]),

    # --- Discard from hand / from a Pokemon -------------------------------
    Rule("discard-hand",
         r"discard (?P<n>\d+) cards? from your hand",
         "discard_hand_n", lambda m: [m.group("n")]),
    Rule("discard-hand-then-draw",
         r"discard (?P<n>\d+) cards? from your hand if you do draw (?P<draw>\d+) cards?",
         "discard_then_draw", lambda m: [m.group("n"), m.group("draw")],
         module="support_common"),
    Rule("discard-energy-opp",
         r"discard (?:1 )?energy(?: card)?s? (?:attached to |from )?(?P<n>\d+) of your opponents? "
         r"pokemon",
         "discard_energy_opponent", lambda m: []),
    Rule("discard-energy-opp-active",
         r"discard (?P<n>\d+) energy(?: card)?s?(?: attached to| from)? your opponents active "
         r"pokemon",
         "discard_energy_opponent", lambda m: ['scope="active"']),
    Rule("discard-energy-opp-flip",
         r"flip 1 coin if heads discard (?:1 )?energy(?: card)?s? (?:attached to |from )?"
         r"(?P<n>\d+) of your opponents? pokemon",
         "discard_energy_opponent", lambda m: ["flip=True"]),
    Rule("discard-special-energy-opp",
         r"discard (?:1 )?special energy(?: card)?s? (?:attached to |from )?(?P<n>\d+) of your "
         r"opponents? pokemon",
         "discard_energy_opponent", lambda m: ["energy_pred=is_special_energy"]),
    Rule("discard-special-energy-each",
         r"discard (?:1 )?special energy(?: card)?s? from each of your opponents? pokemon",
         "discard_energy_each_opponent", lambda m: ["predicate=is_special_energy"]),
    Rule("discard-stadium", r"discard any stadium card in play",
         "discard_stadium_card", lambda m: []),

    # --- Look at the top --------------------------------------------------
    Rule("look-top-take",
         r"look at the top (?P<n>\d+) cards of your deck and put (?P<take>\d+) of them into "
         r"your hand (?:discard|shuffle) the other cards?(?: back into your deck)?",
         "look_at_top", lambda m: [m.group("n"), "take=" + m.group("take")],
         module="support_common"),
    Rule("look-top-reveal",
         r"look at the top (?P<n>\d+) cards of your deck you may reveal (?P<cat>.+?) you find "
         r"there and put (?:it|them) into your hand shuffle the other cards? back into your deck",
         "look_at_top",
         lambda m: [m.group("n"), "take=1", "predicate=" + _pred(m.group("cat"))],
         module="support_common"),

    # --- Special conditions / hand return ---------------------------------
    Rule("cure-active", r"remove all special conditions from your active pokemon",
         "cure_conditions_effect", lambda m: ['scope="active"'],
         module="support_common"),
    Rule("return-pokemon-to-hand",
         r"put (?P<n>\d+) of your (?P<cat>[a-z0-9 ]*?)pokemon (?:in play )?and all "
         r"(?:cards )?attached(?: cards)?(?: to it)? into your hand",
         "return_pokemon_to_hand",
         lambda m: ["predicate=" + _pred(m.group("cat") + "pokemon")]),
    Rule("return-pokemon-to-hand-discard-attachments",
         r"put (?P<n>\d+) of your pokemon in play into your hand discard all cards attached "
         r"to that pokemon",
         "return_pokemon_to_hand", lambda m: ['with_attachments="discard"']),
    Rule("search-to-top",
         r"search your deck for (?P<n>\d+) cards? shuffle your deck then put those cards on "
         r"top of it in any order",
         "search_to_top", lambda m: [m.group("n")]),
    Rule("shuffle-hand-draw-prize",
         r"shuffle your hand into your deck then draw (?P<n>\d+) cards? if your opponent has "
         r"(?P<threshold>\d+) or fewer prize cards remaining draw (?P<bigger>\d+) cards? instead",
         "shuffle_hand_draw",
         lambda m: [m.group("n"), "opponent_prizes_low=(%s, %s)"
                    % (m.group("threshold"), m.group("bigger"))]),
    Rule("return-pokemon-to-hand-flip",
         r"flip 1 coin if heads (?:return|put) (?P<n>\d+) of your pokemon "
         r"(?:in play )?and all (?:cards )?attached to it (?:to|into) your hand",
         "return_pokemon_to_hand", lambda m: ["flip=True"]),
    Rule("each-draw-per-prize",
         r"each player shuffles (?:their|his or her) hand(?: and puts it on the bottom of "
         r"(?:their|his or her) deck| into (?:their|his or her) deck)(?: if either player put "
         r"any cards on the bottom of their deck in this way)?(?: then)? each player draws "
         r"(?P<n>\d+) cards? for each of (?:their|his or her) remaining prize cards",
         "each_player_shuffle_draw_per_prize", lambda m: []),
    Rule("draw-until-first-turn",
         r"draw cards? until you have (?P<hand>\d+) cards? in your hand if its your first "
         r"turn draw cards? until you have (?P<first>\d+) cards? in your hand",
         "first_turn_draw_until", lambda m: [m.group("hand"), m.group("first")]),

    # --- Energy -----------------------------------------------------------
    Rule("move-basic-energy",
         r"move (?:up to )?(?P<count>\d+) (?:basic )?energy(?: card)?s? (?:attached to |from )?"
         r"(?P<n>\d+) of your pokemon to another of your pokemon",
         "move_basic_energy",
         lambda m: ["predicate=is_basic_energy_card", "count=" + m.group("count")]),
    Rule("attach-discard-energy",
         r"attach (?:up to )?(?P<n>\d+) " + CAT +
         r" from your discard pile to (?P<target>\d+) of your pokemon",
         "attach_from_discard",
         lambda m: [_pred(m.group("cat")), "count=" + m.group("n"), 'target="choice"'],
         module="support_common"),
    Rule("search-attach-energy",
         r"search your deck for (?:up to )?(?P<n>\d+) " + CAT +
         r" and attach (?:it|them|those cards) to (?P<target>\d+) of your pokemon"
         r"(?: in any way you like)? then shuffle your deck",
         "search_attach_energy",
         lambda m: [_pred(m.group("cat")), "count=" + m.group("n")],
         module="support_common"),

    # --- Damage modifiers -------------------------------------------------
    Rule("turn-damage-boost",
         r"during this turn (?:attacks used by your pokemon|your pokemons attacks) do "
         r"(?P<amount>\d+) more damage to (?:your opponents|the) active pokemon(?: before "
         r"applying weakness and resistance)?",
         "turn_damage_boost", lambda m: [m.group("amount")]),
    Rule("turn-damage-boost-ex-and-v",
         r"during this turn attacks used by your pokemon do (?P<amount>\d+) more damage to "
         r"your opponents active pokemon ex and active pokemon v(?: before applying weakness "
         r"and resistance)?",
         "turn_damage_boost_vs",
         lambda m: [m.group("amount"), "any_of(is_pokemon_ex, is_pokemon_v_card)"]),
    Rule("turn-damage-boost-ex",
         r"during this turn attacks used by your pokemon do (?P<amount>\d+) more damage to "
         r"your opponents active pokemon ex(?: before applying weakness and resistance)?",
         "turn_damage_boost_vs", lambda m: [m.group("amount"), "is_pokemon_ex"]),
    Rule("turn-damage-boost-no-rule-box",
         r"during this turn attacks used by your pokemon that dont have 1 rule box do "
         r"(?P<amount>\d+) more damage to your opponents active pokemon(?: before applying weakness "
         r"and resistance)?",
         "turn_damage_boost", lambda m: [m.group("amount"), "exclude_rule_box=True"]),
    Rule("turn-damage-boost-typed",
         r"during this turn attacks used by your (?P<type>[a-z]+) pokemon do (?P<amount>\d+) "
         r"more damage to your opponents active pokemon(?: before applying weakness and "
         r"resistance)?",
         "turn_damage_boost", lambda m: _typed_boost(m)),

    # --- Tool / Stadium continuous effects ---------------------------------
    # These wire `passive=`, not `effect=`: the card has no play-time effect,
    # it changes what happens while it sits attached or next to the Active.
    Rule("tool-takes-less",
         r"the (?:(?P<type>[a-z]+) )?pokemon this card is attached to takes (?P<amount>\d+) "
         r"less damage from attacks from your opponents pokemon(?: after applying weakness and "
         r"resistance)?",
         "holder_takes_less", lambda m: _tool_takes_less(m), kind="passive"),
    Rule("tool-takes-less-opp-attacks",
         r"the pokemon this card is attached to takes (?P<amount>\d+) less damage from your "
         r"opponents attacks",
         "holder_takes_less", lambda m: [m.group("amount")], kind="passive"),
    Rule("tool-damage-boost",
         r"the attacks of the pokemon this card is attached to do (?P<amount>\d+) more damage "
         r"to your opponents active pokemon(?: ex and active pokemon v)?(?: before applying "
         r"weakness and resistance)?",
         "holder_damage_boost", lambda m: [m.group("amount")], kind="passive"),
    Rule("tool-hp-bonus",
         r"the pokemon this card is attached to gets (?P<amount>\d+) hp",
         "holder_hp_bonus", lambda m: [m.group("amount")], kind="passive"),
    Rule("tool-no-weakness",
         r"the pokemon this card is attached to has no weakness",
         "holder_no_weakness", lambda m: [], kind="passive"),
    Rule("tool-retreat-discount",
         r"the retreat cost of the pokemon this card is attached to is (?P<count>(?:colorless)+) "
         r"less",
         "holder_retreat_discount", lambda m: [str(_colorless_count(m.group("count")))],
         kind="passive"),
    Rule("stadium-retreat-discount",
         r"the retreat cost of each (?:(?P<basic>basic) )?pokemon in play both yours and your "
         r"opponents is (?P<count>colorless(?: colorless)*) less",
         "stadium_retreat_discount",
         lambda m: [str(_colorless_count(m.group("count"))),
                    "basic_only=" + ("True" if m.group("basic") else "False")],
         kind="passive"),
    Rule("tool-takes-less-and-no-weakness",
         r"the (?:(?P<type>[a-z]+) )?pokemon this card is attached to takes (?P<amount>\d+) "
         r"less damage from your opponents attacks(?: after applying weakness and resistance)? "
         r"and has no weakness",
         "combined",
         lambda m: ["combined(holder_takes_less(%s), holder_no_weakness())"
                    % _tool_takes_less(m)[0]] if True else [], kind="passive"),
    Rule("tool-boost-and-no-weakness",
         r"the attacks of the pokemon this card is attached to do (?P<amount>\d+) more damage "
         r"to your opponents active pokemon(?: before applying weakness and resistance)? and "
         r"that pokemon has no weakness",
         "combined",
         lambda m: ["combined(holder_damage_boost(%s), holder_no_weakness())"
                    % m.group("amount")], kind="passive"),
    Rule("stadium-tools-off",
         r"pokemon tools attached to each pokemon both yours and your opponents have no effect",
         "ToolsSuppressedStadiumPassive", lambda m: [], kind="passive"),
    Rule("stadium-takes-less",
         r"(?P<owner>[a-z]+ )?pokemon both yours and your opponents take (?P<amount>\d+) less "
         r"damage from attacks from the opponents pokemon",
         "stadium_takes_less", lambda m: [m.group("amount")], kind="passive"),

    # --- Composed shapes --------------------------------------------------
    Rule("draw-prize-bonus",
         r"draw (?P<base>\d+) cards? if your opponent has (?P<threshold>\d+) or fewer prize "
         r"cards remaining draw (?P<bonus>\d+) more cards?",
         "draw_n_prize_bonus",
         lambda m: [m.group("base"), m.group("bonus"), m.group("threshold")]),
    Rule("shuffle-one-hand-draw",
         r"if you have any cards in your hand shuffle (?P<n>\d+) of them into your deck then "
         r"draw (?P<draw>\d+) cards?",
         "shuffle_one_hand_draw", lambda m: [m.group("draw")]),
    Rule("flip-recover-basic-energy",
         r"flip (?P<n>\d+) coins for each heads put (?P<each>\d+) basic energy card from your "
         r"discard pile into your hand.*",
         "flip_recover_basic_energy", lambda m: [m.group("n")]),
    Rule("recover-basic-to-bench",
         r"put (?P<n>\d+) basic pokemon? from your discard pile onto your bench",
         "recover_basic_to_bench", lambda m: [m.group("n")]),
    Rule("reveal-until-supporter",
         r"reveal cards from the top of your deck until you reveal (?P<n>\d+) supporter cards? "
         r"put (?:it|them) into your hand shuffle the other cards back into your deck",
         "reveal_until_supporter", lambda m: []),
    Rule("devolve-one",
         r"devolve (?P<n>\d+) of your evolved pokemon and put the highest stage evolution card "
         r"on it into your hand(?: that pokemon cant evolve this turn)?",
         "devolve_one", lambda m: [m.group("n")]),
    Rule("cure-each-active",
         r"remove all special conditions from each of your active pokemon",
         "cure_conditions_effect", lambda m: ['scope="each_own"'],
         module="support_common"),

    # --- Draw / discard compositions --------------------------------------
    Rule("draw-then-discard",
         r"draw (?P<draw>\d+) cards? then discard (?:any )?(?P<discard>\d+) card from your hand",
         "draw_then_discard", lambda m: [m.group("draw"), m.group("discard")]),
    Rule("draw-until-unless-owner",
         r"draw cards? until you have (?P<hand>\d+) cards? in your hand if all of your pokemon "
         r"in play are (?P<cat>[a-z0-9 ]+?) draw cards? until you have (?P<other>\d+) cards? in "
         r"your hand instead",
         "draw_until_unless",
         lambda m: [m.group("hand"), m.group("other"),
                    _pred(m.group("cat"))]),
    Rule("heal-all-own-discard-energy",
         r"remove all damage counters from all of your own pokemon with damage counters on them "
         r"then discard all energy cards attached to those pokemon",
         "heal_all_own_discard_energy", lambda m: []),
    Rule("discard-tools",
         r"choose up to (?P<n>\d+) pokemon tools attached to pokemon(?: yours or your "
         r"opponents)? and discard them",
         "discard_tools", lambda m: [m.group("n")]),
    Rule("trade-for-discard",
         r"trade (?P<n>\d+) of the other cards in your hand for up to (?P<count>\d+) "
         r"(?P<cat>[a-z0-9 ]+?) from your discard pile",
         "trade_to_hand",
         lambda m: [_pred(m.group("cat")), "count=" + m.group("count")]),
    Rule("devolve-to-basic",
         r"choose (?P<n>\d+) of your pokemon in play and return its basic pokemon card to your "
         r"hand discard all cards attached to that card",
         "devolve_to_basic", lambda m: []),
    Rule("tool-attack-discount-prize",
         r"if you have more prize cards remaining than your opponent attacks used by the pokemon "
         r"this card is attached to cost (?P<count>(?:colorless)+) less",
         "holder_attack_discount",
         lambda m: [str(_colorless_count(m.group("count"))), "prize_behind=True"],
         kind="passive"),

    # --- Heal / draw / discard compositions -------------------------------
    Rule("heal-chosen",
         r"choose up to (?P<count>\d+) of your pokemon and heal (?P<amount>\d+) damage from "
         r"each of them",
         "heal_chosen", lambda m: [m.group("amount"), "count=" + m.group("count")]),
    Rule("heal-all-chosen-low-hp",
         r"heal all damage from (?P<n>\d+) of your pokemon that has (?P<hp>\d+) hp or less "
         r"remaining",
         "heal_chosen",
         lambda m: ["-1", "count=" + m.group("n"), "hp_at_most=" + m.group("hp")]),
    Rule("draw-until-unless-energy",
         r"draw cards? until you have (?P<hand>\d+) cards? in your hand if none of your pokemon "
         r"have any energy attached draw cards? until you have (?P<other>\d+) cards? in your "
         r"hand instead",
         "draw_until_unless_energy",
         lambda m: [m.group("hand"), m.group("other")]),
    Rule("hand-to-bottom-draw-until",
         r"put (?P<n>\d+) card from your hand on the bottom of your deck if you do draw cards? "
         r"until you have (?P<hand>\d+) cards? in your hand.*",
         "hand_to_bottom_draw_until", lambda m: [m.group("hand")]),
    Rule("discard-no-rule-box-draw",
         r"discard up to (?P<count>\d+) pokemon that dont have 1 rule box from your hand and "
         r"draw (?P<per>\d+) cards? for each card you discarded in this way",
         "discard_hand_no_rule_box_draw_per_card",
         lambda m: [m.group("per"), "count=" + m.group("count")]),
    Rule("opponent-energy-to-deck-top",
         r"put (?P<n>\d+) energy attached to your opponents active pokemon on top of their deck",
         "opponent_energy_to_deck_top", lambda m: []),
    Rule("discard-from-opponent-hand",
         r"your opponent reveals their hand and you discard up to (?P<count>\d+) "
         r"(?P<cat>[a-z0-9 ]+?) you find there",
         "discard_from_opponent_hand",
         lambda m: ["predicate=" + _pred(m.group("cat")),
                    "count=" + m.group("count")]),
    Rule("attach-discard-energy-each",
         r"choose up to (?P<targets>\d+) of your (?P<cat>[a-z0-9 ]*?)pokemon and attach "
         r"(?P<per>\d+) (?P<energy>[a-z0-9 ]+?) from your discard pile to each of them",
         "attach_discard_energy_to_each",
         lambda m: [_pred(m.group("energy")), "per_target=" + m.group("per"),
                    "targets=" + m.group("targets")]),
    Rule("switch-then-move-energy",
         r"switch your active pokemon with (?P<n>\d+) of your benched pokemon if you do move "
         r"(?P<c>\d+) energy from the pokemon you moved to your bench to the new active pokemon",
         "switch_then_move_energy", lambda m: []),

    # --- Conditions / discard / switching compositions --------------------
    Rule("two-conditions-opponent-active",
         r"your opponents active pokemon is now (?P<a>[a-z]+) and (?P<b>[a-z]+)",
         "condition_opponent_active",
         lambda m: [_condition(m.group("a")), _condition(m.group("b"))]),
    Rule("condition-opponent-active",
         r"your opponents active pokemon is now (?P<a>[a-z]+)",
         "condition_opponent_active", lambda m: [_condition(m.group("a"))]),
    Rule("heal-all-then-discard-energy",
         r"heal all damage from (?P<n>\d+) of your pokemon if you do discard all energy(?: cards?)? "
         r"from that pokemon",
         "heal_all_then_discard_energy", lambda m: []),
    Rule("discard-benched-undamaged",
         r"discard up to (?P<n>\d+) of your benched pokemon that have no damage counters on them "
         r"and all cards attached to them",
         "discard_benched_undamaged", lambda m: [m.group("n")]),
    Rule("discard-tools-and-stadiums",
         r"choose up to (?P<n>\d+) in any combination of pokemon tool cards and stadium cards in "
         r"play(?: yours or your opponents)? and discard them",
         "discard_in_play",
         lambda m: ["[is_tool_card, is_stadium_card]", "count=" + m.group("n")]),
    Rule("opponent-draw-per-prize",
         r"your opponent shuffles their hand into their deck and draws (?P<n>\d+) card for each "
         r"of their remaining prize cards",
         "opponent_shuffle_draw_per_prize", lambda m: []),
    Rule("draw-if-active-subtype",
         r"draw (?P<base>\d+) cards? if your active pokemon is (?P<cat>[a-z0-9 ]+?) draw "
         r"(?P<bonus>\d+) more cards?",
         "draw_n_if_active",
         lambda m: ['"%s"' % _active_subtype(m.group("cat")),
                    m.group("base"), m.group("bonus")]),
    Rule("attach-hand-then-draw",
         r"attach up to (?P<n>\d+) " + CAT +
         r" from your hand to (?P<target>\d+) of your pokemon if you do draw (?P<draw>\d+) cards?",
         "attach_hand_then_draw",
         lambda m: [_pred(m.group("cat")), "count=" + m.group("n"),
                    "draw=" + m.group("draw")]),
    Rule("move-counters-between-opponents",
         r"move up to (?P<n>\d+) damage counters? from (?P<src>\d+) of your opponents pokemon to "
         r"another of their pokemon",
         "move_counters_between_opponents", lambda m: [m.group("n")]),
    Rule("escape-rope-composite",
         r"switch (?P<n>\d+) of your opponents benched pokemon with their active pokemon if you do "
         r"switch your active pokemon with (?P<m>\d+) of your benched pokemon",
         "opponent_switch_then_self_switch", lambda m: []),
    Rule("search-retreat-cost",
         r"search your deck for up to (?P<n>\d+) pokemon that have (?P<rc>\d+) retreat cost of "
         r"exactly (?P<cost>\d+) reveal them and put them into your hand then shuffle your deck",
         "search_to_hand",
         lambda m: ["retreat_cost_is(%s)" % m.group("cost"),
                    "count=" + m.group("n")],
         module="support_common"),

    # --- More composed shapes ---------------------------------------------
    Rule("flip-discard-opponent-energy",
         r"flip 1 coin if heads choose (?P<n>\d+) energy card attached to (?P<which>\d+) of your "
         r"opponents pokemon and discard it",
         "discard_energy_opponent", lambda m: ["flip=True"]),
    Rule("evade-rope-classic",
         r"your opponent switches (?P<n>\d+) of (?:his or her|their) defending pokemon with "
         r"(?P<m>\d+) of (?:his or her|their) benched pokemon if any you switch (?P<k>\d+) of "
         r"your active pokemon with (?P<j>\d+) of your benched pokemon if any",
         "opponent_switch_then_self_switch", lambda m: []),
    Rule("reveal-pokemon-then-search",
         r"reveal (?P<n>\d+) pokemon from your hand and put it into your deck if you do search "
         r"your deck for (?P<c>\d+) pokemon reveal it and put it into your hand then shuffle "
         r"your deck",
         "reveal_pokemon_then_search", lambda m: []),
    Rule("hand-to-top-then-search",
         r"choose (?P<n>\d+) card from your hand and put it on top of your deck search your deck "
         r"for (?P<c>\d+) pokemon show it to your opponent and put it into your hand.*",
         "hand_to_top_then_search", lambda m: []),
    Rule("flip-search-basic",
         r"flip (?P<n>\d+) coins for each heads search your deck for (?P<c>\d+) basic pokemon "
         r"card show it to your opponent and put it into your hand.*",
         "flip_search_basic", lambda m: []),
    Rule("heal-all-then-energy-to-hand",
         r"heal all damage from (?P<n>\d+) of your mega evolution pokemon ex if you healed any "
         r"damage in this way put all energy attached to that pokemon into your hand",
         "heal_all_then_energy_to_hand", lambda m: ['pokemon_of_subtype("MEGA")']),
    Rule("trade-pokemon",
         r"trade (?P<n>\d+) of the basic pokemon or evolution cards in your hand for (?P<c>\d+) "
         r"of the basic pokemon or evolution cards from your deck.*",
         "trade_pokemon", lambda m: []),
    Rule("shuffle-hand-n-draw",
         r"shuffle (?P<n>\d+) cards from your hand into your deck(?: if you cant shuffle \d+ "
         r"cards into your deck you cant play this card)?(?: then)? draw (?P<draw>\d+) card",
         "shuffle_hand_n_draw", lambda m: [m.group("n"), "draw=" + m.group("draw")]),
    Rule("recover-combination-to-deck",
         r"search your discard pile for up to (?P<n>\d+) " + CAT +
         r" show them? to your opponent and shuffle them? into your deck",
         "recover_from_discard",
         lambda m: [_pred(m.group("cat")), "count=" + m.group("n"),
                    'to="deck_shuffle"'],
         module="support_common"),

    # --- Remaining composed shapes ----------------------------------------
    Rule("shuffle-hand-draw-exact-prizes",
         r"shuffle your hand into your deck then draw (?P<n>\d+) cards? if you have exactly "
         r"(?P<prizes>\d+) prize cards remaining draw (?P<bigger>\d+) cards? instead",
         "shuffle_hand_draw_exact_prizes",
         lambda m: [m.group("n"), m.group("prizes"), m.group("bigger")]),
    Rule("attach-each-then-draw",
         r"choose up to (?P<targets>\d+) of your " + CAT +
         r" and attach (?P<per>\d+) (?P<energy>[a-z0-9 ]+?) from your discard pile to each of "
         r"them if you attached any energy in this way draw (?P<draw>\d+) cards?",
         "attach_discard_energy_each_then_draw",
         lambda m: [_pred(m.group("energy")), "per_target=" + m.group("per"),
                    "targets=" + m.group("targets"), "draw=" + m.group("draw")]),
    Rule("look-top-choose-back-on-top",
         r"look at the top (?P<n>\d+) cards (?:of|from) your deck(?: and)? choose (?P<take>\d+) "
         + CAT + r"(?: from those cards)? show it to your opponent and put it into your hand put "
         r"the (?:other|\d+ other) cards back on top of your deck(?: in any order)?(?: shuffle "
         r"your deck afterward)?",
         "look_at_top",
         lambda m: [m.group("n"), "take=" + m.group("take"),
                    "predicate=" + _pred(m.group("cat")), 'rest="back"'],
         module="support_common"),
    Rule("search-three-stages",
         r"search your deck for (?P<a>\d+) basic pokemon (?P<b>\d+) stage 1 pokemon and "
         r"(?P<c>\d+) stage 2 pokemon reveal them and put them into your hand then shuffle your "
         r"deck",
         "search_three_stages", lambda m: []),
    Rule("stadium-evolve-early-typed",
         r"each players (?P<type>[a-z]+) pokemon can evolve into (?P<type2>[a-z]+) pokemon during "
         r"the turn they play those pokemon except during their first turn",
         "evolve_early_passive",
         lambda m: [_typed_or_decline(m.group("type"))], kind="passive"),
    Rule("opponent-reveals-discard-energy",
         r"your opponent reveals their hand discard (?P<n>\d+) energy cards? from it",
         "discard_from_opponent_hand",
         lambda m: ["predicate=is_energy_card", "count=" + m.group("n")]),
    Rule("draw-per-typed",
         r"draw (?P<per>\d+) cards? for each (?P<type>[a-z]+) pokemon you have in play",
         "draw_per_typed", lambda m: [_typed_or_decline(m.group("type")), m.group("per")]),
    Rule("draw-per-opponent-pokemon",
         r"draw (?P<per>\d+) card for each of your opponents pokemon in play",
         "draw_per_opponent_pokemon", lambda m: [m.group("per")]),

    # --- Final composed shapes --------------------------------------------
    Rule("return-damaged-pokemon-to-hand",
         r"put (?P<n>\d+) of your pokemon that has any damage counters on it and all cards "
         r"attached to it into your hand",
         "return_pokemon_to_hand",
         lambda m: ["predicate=is_damaged_pokemon"]),
    Rule("switch-then-heal-ex",
         r"switch (?:1 of )?your active pokemon with (?P<n>\d+) of your benched pokemon if you "
         r"moved (?P<c>\d+) pokemon ex to your bench in this way heal (?P<amount>\d+) damage from "
         r"that pokemon",
         "switch_then_heal_ex", lambda m: [m.group("amount")]),
    Rule("attach-discard-to-typed-target",
         r"attach (?:up to )?(?P<n>\d+) " + CAT +
         r" from your discard pile to (?P<target>\d+) of your (?P<which>[a-z0-9 ]*?)pokemon",
         "attach_from_discard",
         lambda m: [_pred(m.group("cat")), "count=" + m.group("n"), 'target="choice"'],
         module="support_common"),
    Rule("search-split-energy",
         r"search your deck for up to (?P<n>\d+) basic energy cards of different types reveal "
         r"them and put (?P<take>\d+) of them into your hand attach the other to (?P<target>\d+) "
         r"of your pokemon then shuffle your deck",
         "search_split_energy_to_hand_and_attach", lambda m: []),
    Rule("attach-darkness-each-poison",
         r"choose up to (?P<n>\d+) of your darkness pokemon for each of those pokemon search your "
         r"deck for (?P<c>\d+) basic darkness energy card and attach it to that pokemon then "
         r"shuffle your deck if you attached energy to your active pokemon in this way it is now "
         r"poisoned",
         "attach_darkness_to_each_poison", lambda m: []),

    # --- Going-second, hand reveals, top-of-deck ---------------------------
    Rule("shuffle-hand-draw-going-second",
         r"shuffle your hand into your deck then draw (?P<n>\d+) cards? if you go second and its "
         r"your first turn draw (?P<bigger>\d+) cards? instead",
         "shuffle_hand_draw_going_second",
         lambda m: [m.group("n"), m.group("bigger")]),
    Rule("look-top-take-bottom",
         r"look at the top (?P<n>\d+) cards of your deck and put (?P<take>\d+) of them into your "
         r"hand shuffle the other cards and put them on the bottom of your deck",
         "look_at_top",
         lambda m: [m.group("n"), "take=" + m.group("take"), 'rest="bottom"'],
         module="support_common"),
    Rule("opponent-reveals-draw-per-supporter",
         r"your opponent reveals their hand and you draw (?P<per>\d+) cards? for each "
         r"(?P<cat>[a-z0-9 ]+?) you find there",
         "draw_per_opponent_hand_card",
         lambda m: ["predicate=" + _pred(m.group("cat")), "per=" + m.group("per")]),
    Rule("draw-per-opponent-bench",
         r"draw (?P<per>\d+) card for each of your opponents benched pokemon",
         "draw_per_opponent_bench", lambda m: [m.group("per")]),
    Rule("opponent-hand-to-bottom",
         r"your opponent reveals their hand and you choose (?P<n>\d+) card you find there and put "
         r"it on the bottom of their deck.*",
         "opponent_hand_to_bottom", lambda m: []),
    Rule("opponent-energy-to-hand-then-attach",
         r"put (?P<n>\d+) energy attached to your opponents active pokemon into their hand if you "
         r"do attach (?P<c>\d+) energy card from your hand to your active pokemon",
         "opponent_energy_to_hand_then_attach", lambda m: []),
    Rule("reveal-then-search-same",
         r"reveal up to (?P<n>\d+) pokemon in your hand and put them into your deck if you do "
         r"search your deck for up to that many pokemon reveal th.*",
         "reveal_then_search_same", lambda m: []),
    Rule("tool-damage-boost-ex-or-gx",
         r"the attacks of the pokemon this card is attached to do (?P<amount>\d+) more damage to "
         r"your opponents active pokemon gx or active pokemon ex(?: before applying weakness and "
         r"resistance)?",
         "holder_damage_boost",
         lambda m: [m.group("amount"),
                    "target_pred=any_of(is_pokemon_gx, is_pokemon_ex)"],
         kind="passive"),

    # --- Fossils printed as Basic Pokemon ---------------------------------
    Rule("fossil-basic",
         r"play this card as if it were (?:(?P<art>\d+) )?(?P<hp>\d+) hp (?:basic )?colorless "
         r"(?:basic )?pokemon .*discard this card from play.*",
         "fossil", lambda m: [m.group("hp")], kind="fossil"),

    # --- Typed heals and bench-to-active energy moves ---------------------
    Rule("heal-each-typed",
         r"heal (?P<amount>\d+) damage from each of your (?P<type>[a-z]+) pokemon",
         "heal_each_typed",
         lambda m: [m.group("amount"), _typed_or_decline(m.group("type"))]),
    Rule("gust-then-confuse",
         r"switch in (?P<n>\d+) of your opponents benched basic pokemon to the active spot if "
         r"you do the new active pokemon is now confused",
         "gust_then_confuse", lambda m: []),
    Rule("move-energy-to-active",
         r"move up to (?P<n>\d+) energy from your benched pokemon to your active pokemon",
         "move_energy_to_active", lambda m: [m.group("n")]),
    Rule("discard-stadium-opponent-discards",
         r"discard any stadium card in play if you do your opponent discards (?P<n>\d+) cards "
         r"from his or her hand",
         "discard_stadium_then_opponent_discards", lambda m: [m.group("n")]),
    Rule("opponent-bench-from-hand",
         r"your opponent reveals their hand and you put (?P<n>\d+) basic pokemon you find there "
         r"onto your opponents bench if you put (?P<c>\d+) pokemon onto their bench in this way "
         r"switch in that pokemon to the active spot",
         "opponent_bench_from_hand_then_switch", lambda m: []),

    # --- Tool stat-effect variants ----------------------------------------
    Rule("tool-damage-boost-vs",
         r"the attacks of the pokemon this card is attached to do (?P<amount>\d+) more damage to "
         r"your opponents active pokemon (?P<kind>ex|v|vmax|gx)(?: or active pokemon [a-z]+)?"
         r"(?: before applying weakness and resistance)?",
         "holder_damage_boost_vs",
         lambda m: [m.group("amount"), '"%s"' % m.group("kind")], kind="passive"),
    Rule("tool-takes-less-basic",
         r"if the pokemon this card is attached to is (?P<basic>1 basic) pokemon any damage done to "
         r"this pokemon by attacks is reduced by (?P<amount>\d+)(?: after applying weakness and "
         r"resistance)?",
         "holder_takes_less_basic", lambda m: [m.group("amount")], kind="passive"),
    Rule("tool-damage-reduced-by",
         r"any damage done to the pokemon this card is attached to by attacks is reduced by "
         r"(?P<amount>\d+)(?: after applying weakness and resistance)?",
         "holder_takes_less", lambda m: [m.group("amount")], kind="passive"),
    Rule("tool-no-retreat",
         r"the pokemon this card is attached to has no retreat cost",
         "holder_retreat_free", lambda m: [], kind="passive"),
    Rule("tool-hp-more",
         r"the pokemon this card is attached to has (?P<amount>\d+) more hp",
         "holder_hp_bonus", lambda m: [m.group("amount")], kind="passive"),

    # --- Holder-gated tools ---------------------------------------------
    Rule("gated-hp",
         r"the (?P<holder>[a-z0-9 ]+?) this card is attached to gets (?P<amount>\d+) hp"
         r"(?: ace spec you cant have more than 1 ace spec card in your deck)?",
         "gated_hp_bonus", lambda m: [m.group("amount"), _holder(m.group("holder"))],
         kind="passive"),
    Rule("gated-no-weakness",
         r"the (?P<holder>[a-z0-9 ]+?) this card is attached to has no weakness",
         "gated_no_weakness", lambda m: [_holder(m.group("holder"))], kind="passive"),
    Rule("gated-no-retreat",
         r"the (?P<holder>[a-z0-9 ]+?) this card is attached to has no retreat cost",
         "gated_retreat_free", lambda m: [_holder(m.group("holder"))], kind="passive"),
    Rule("gated-takes-less",
         r"the (?P<holder>[a-z0-9 ]+?) this card is attached to takes (?P<amount>\d+) less "
         r"damage from attacks from your opponents (?P<attacker>[a-z0-9 ]*?)pokemon after "
         r"applying weakness and resistance",
         "gated_takes_less",
         lambda m: [m.group("amount"), _holder(m.group("holder")),
                    "attacker=" + _holder((m.group("attacker") + "pokemon").strip())],
         kind="passive"),
    Rule("gated-damage-boost",
         r"(?:attacks used by|the attacks of) the (?P<holder>[a-z0-9 ]+?) this card is attached "
         r"to do (?P<amount>\d+) more damage to your opponents active pokemon(?P<ex> ex)? "
         r"before applying weakness and resistance",
         "gated_damage_boost",
         lambda m: [m.group("amount"), _holder(m.group("holder")),
                    "target=" + ("is_pokemon_ex" if m.group("ex") else "None")],
         kind="passive"),
    Rule("gated-hp-and-boost",
         r"the (?P<holder>[a-z0-9 ]+?) this card is attached to gets (?P<hp>\d+) hp and its "
         r"attacks do (?P<amount>\d+) more damage to your opponents active pokemon before "
         r"applying weakness and resistance",
         "combined",
         lambda m: ["gated_hp_bonus(%s, %s)" % (m.group("hp"), _holder(m.group("holder"))),
                    "gated_damage_boost(%s, %s)" % (m.group("amount"),
                                                    _holder(m.group("holder")))],
         kind="passive"),
    Rule("gated-no-retreat-and-boost",
         r"the (?P<holder>[a-z0-9 ]+?) this card is attached to has no retreat cost and the "
         r"attacks it uses do (?P<amount>\d+) more damage to your opponents active pokemon "
         r"before applying weakness and resistance",
         "combined",
         lambda m: ["gated_retreat_free(%s)" % _holder(m.group("holder")),
                    "gated_damage_boost(%s, %s)" % (m.group("amount"),
                                                    _holder(m.group("holder")))],
         kind="passive"),
    Rule("gated-boost-rule-box-free",
         r"if the pokemon this card is attached to doesnt have 1 rule box the attacks it uses "
         r"do (?P<amount>\d+) more damage to your opponents active pokemon ex before applying "
         r"weakness and resistance",
         "gated_damage_boost",
         lambda m: [m.group("amount"), "is_rule_box_free_pokemon", "target=is_pokemon_ex"],
         kind="passive"),
    Rule("gated-boost-non-ex",
         r"the attacks of the pokemon this card is attached to excluding pokemon ex do "
         r"(?P<amount>\d+) more damage to active pokemon ex before applying weakness and "
         r"resistance",
         "gated_damage_boost",
         lambda m: [m.group("amount"), "excluding(is_pokemon_EX)", "target=is_pokemon_EX"],
         kind="passive"),

    Rule("gated-type",
         r"the (?P<holder>[a-z0-9 ]+?) this card is attached to is 1 (?P<type>[a-z]+) pokemon",
         "gated_type",
         lambda m: [_typed_or_decline(m.group("type")), _holder(m.group("holder"))],
         kind="passive"),
    Rule("low-hp-retreat",
         r"the retreat cost of the pokemon this card is attached to is (?P<count>colorless(?: "
         r"?colorless)*) less if that pokemons remaining hp is (?P<hp>\d+) or less it has no "
         r"retreat cost",
         "low_hp_retreat",
         lambda m: [str(_colorless_count(m.group("count"))), m.group("hp")], kind="passive"),
    Rule("active-holder-retreat-tax",
         r"as long as the pokemon this card is attached to is in the active spot the retreat "
         r"cost of both active pokemon is (?P<count>colorless(?: ?colorless)*) more",
         "active_holder_retreat_tax",
         lambda m: [str(_colorless_count(m.group("count")))], kind="passive"),
    Rule("tool-reduced-by-opponents-attack",
         r"any damage done to the pokemon this card is attached to by 1 opponents attack is "
         r"reduced by (?P<amount>\d+) after applying weakness and resistance",
         "holder_takes_less", lambda m: [m.group("amount")], kind="passive"),
    Rule("holder-coin-reroll",
         r"once during your turn after you flip any coins for 1 attack of the "
         r"(?P<holder>[a-z0-9 ]+?) this card is attached to you may ignore all (?:results|"
         r"effects) of those coin flips and begin flipping those coins again(?: you may only "
         r"use effects that let you flip coins again including effects from other cards once "
         r"during your turn)?",
         "holder_coin_reroll", lambda m: [_holder(m.group("holder"))], kind="passive"),
    Rule("if-attached-boost",
         r"if this card is attached to (?:1 )?(?P<holder>[a-z0-9 ]+?) each of (?:its attacks|the "
         r"attacks of that pokemon) does (?P<amount>\d+) more damage to the active pokemon "
         r"before applying weakness and resistance",
         "gated_damage_boost",
         lambda m: [m.group("amount"), _holder(m.group("holder"))], kind="passive"),

    # --- Prize count on Knock Out ---------------------------------------
    Rule("holder-prize-fewer-any-ko",
         r"if the pokemon this card is attached to is knocked out your opponent takes "
         r"(?P<n>\d+) fewer prize cards?",
         "holder_prize_shift", lambda m: ["-" + m.group("n"), "None", "attack_only=False"],
         kind="passive"),
    Rule("holder-prize-fewer",
         r"if the (?P<holder>[a-z0-9 ]+?) this card is attached to is knocked out by damage from "
         r"1 attack from your opponents pokemon that player takes (?P<n>\d+) fewer prize cards?",
         "holder_prize_shift", lambda m: ["-" + m.group("n"), _holder(m.group("holder"))],
         kind="passive"),
    Rule("amulet-hp-and-prize-fewer",
         r"the pokemon gx or pokemon ex this card is attached to gets (?P<hp>\d+) hp and when it "
         r"is knocked out by damage from 1 opponents attack that player takes (?P<n>\d+) fewer "
         r"prize cards?",
         "combined",
         lambda m: ["gated_hp_bonus(%s, any_of(is_pokemon_gx, is_pokemon_EX))" % m.group("hp"),
                    "holder_prize_shift(-%s, any_of(is_pokemon_gx, is_pokemon_EX))" % m.group("n")],
         kind="passive"),
    Rule("cape-hp-and-prize-more",
         r"if the pokemon this card is attached to doesnt have 1 rule box it gets (?P<hp>\d+) hp "
         r"and if it is knocked out by damage from 1 attack from your opponents pokemon that "
         r"player takes (?P<n>\d+) more prize cards?",
         "combined",
         lambda m: ["gated_hp_bonus(%s, is_rule_box_free_pokemon)" % m.group("hp"),
                    "holder_prize_shift(%s, is_rule_box_free_pokemon)" % m.group("n")],
         kind="passive"),
    Rule("stadium-prize-fewer",
         r"whenever 1 (?P<cat>[a-z0-9 ]+?) yours or your opponents is knocked out by damage from "
         r"1 attack from the opponents pokemon that player takes (?P<n>\d+) fewer prize cards?",
         "stadium_prize_shift", lambda m: ["-" + m.group("n"), _union(m.group("cat"))],
         kind="passive"),

    Rule("tool-takes-less-special-energy-attacker",
         r"any damage done to the pokemon this card is attached to by attacks from your opponents "
         r"pokemon that have any special energy attached to them is reduced by (?P<amount>\d+) "
         r"after applying weakness and resistance",
         "takes_less_from",
         lambda m: [m.group("amount"), "None", "attacker_has_special_energy()"],
         kind="passive"),
    Rule("tool-takes-less-ability-attacker",
         r"the pokemon this card is attached to takes (?P<amount>\d+) less damage from attacks "
         r"from your opponents pokemon that have 1 ability after applying weakness and resistance",
         "takes_less_from",
         lambda m: [m.group("amount"), "None", "attacker_has_ability()"], kind="passive"),
    Rule("tool-takes-less-typed-attacker",
         r"the (?P<holder>[a-z0-9 ]+?) this card is attached to takes (?P<amount>\d+) less damage "
         r"from attacks from your opponents (?P<types>[a-z ]+?) pokemon after applying weakness "
         r"and resistance",
         "takes_less_from",
         lambda m: [m.group("amount"), _holder(m.group("holder")),
                    _attacker_types(m.group("types"))], kind="passive"),
    Rule("tool-takes-less-named-holder",
         r"the (?P<names>[a-z0-9 ]+?) this card is attached to takes (?P<amount>\d+) less damage "
         r"from your opponents attacks after applying weakness and resistance",
         "takes_less_from",
         lambda m: [m.group("amount"), _name_choice(m.group("names"))], kind="passive"),
    Rule("tool-takes-less-from-mega",
         r"if the pokemon this card is attached to isnt 1 mega evolution pokemon ex it takes "
         r"(?P<amount>\d+) less damage from attacks from your opponents mega evolution pokemon ex "
         r"after applying weakness and resistance",
         "takes_less_from",
         lambda m: [m.group("amount"), "excluding(pokemon_of_subtype(\"MEGA\"))",
                    'attacker_has_subtypes("MEGA", "ex")'], kind="passive"),
    Rule("stadium-retreat-zero",
         r"the retreat cost (?:of|for) each (?P<cat>[a-z0-9 ]+?)(?: pokemon)? both yours and your "
         r"opponents is 0",
         "stadium_no_retreat", lambda m: [_stadium_cat(m.group("cat"))],
         kind="passive"),
    Rule("stadium-retreat-shift-cat",
         r"the retreat cost (?:of|for) each (?P<cat>[a-z0-9 ]+?)(?: pokemon)?(?: in play)? both "
         r"yours and your opponents is (?P<count>colorless(?: ?colorless)*) (?P<dir>less|more)",
         "stadium_retreat_shift",
         lambda m: [("-" if m.group("dir") == "less" else "")
                    + str(_colorless_count(m.group("count"))),
                    _stadium_cat(m.group("cat"))],
         kind="passive"),
    Rule("stadium-retreat-shift-attached-energy",
         r"the retreat cost of each pokemon both yours and your opponents that has any "
         r"(?P<types>[a-z ]+?) energy attached to it is (?P<count>colorless(?: ?colorless)*) less",
         "stadium_retreat_shift",
         lambda m: ["-" + str(_colorless_count(m.group("count"))),
                    _stadium_cat("pokemon that has any " + m.group("types")
                                 + " energy attached to it")],
         kind="passive"),
    Rule("stadium-no-retreat-energy",
         r"each pokemon that has any (?P<types>[a-z ]+?) energy attached to it both yours and "
         r"your opponents has no retreat cost",
         "stadium_no_retreat",
         lambda m: [_stadium_cat("pokemon that has any " + m.group("types")
                                 + " energy attached to it")],
         kind="passive"),
    Rule("stadium-hp-named",
         r"each pokemon(?: in play)? with (?P<word>[a-z]+) in its name even your opponents gets "
         r"(?P<amount>\d+) hp",
         "stadium_hp_bonus",
         lambda m: [m.group("amount"), _stadium_cat("pokemon with %s in its name"
                                                    % m.group("word"))],
         kind="passive"),
    Rule("stadium-retreat-named",
         r"the retreat cost of each (?P<word>[a-z]+) in play both yours and your opponents is "
         r"(?P<count>colorless(?: ?colorless)*) less",
         "stadium_retreat_shift",
         lambda m: ["-" + str(_colorless_count(m.group("count"))),
                    'pokemon_named("%s")' % m.group("word")], kind="passive"),
    Rule("tool-prevent-all-from-typed-subtype",
         r"prevent all damage done to the (?P<holder>[a-z]+) pokemon this card is attached to by "
         r"attacks from your opponents (?P<type>[a-z]+) pokemon gx and (?P=type) pokemon ex",
         "prevents_all_from",
         lambda m: [_holder(m.group("holder")),
                    'attacker_of_types("%s")' % m.group("type")],
         kind="passive"),
    Rule("tool-prevent-all-from-ability-attacker",
         r"prevent all damage done to the (?P<holder>[a-z]+) pokemon this card is attached to by "
         r"attacks from your opponents pokemon gx and pokemon ex that have abilities",
         "prevents_all_from",
         lambda m: [_holder(m.group("holder")), "attacker_has_ability()"], kind="passive"),
    Rule("tool-prevent-all-from-ultra-beast",
         r"prevent all damage done to the (?P<holder>[a-z]+) pokemon this card is attached to by "
         r"attacks from your opponents ultra beast pokemon gx and ultra beast pokemon ex",
         "prevents_all_from",
         lambda m: [_holder(m.group("holder")),
                    'attacker_has_subtypes("Ultra Beast", "gx")'], kind="passive"),
    Rule("tool-prevent-effects-and-damage-from-named-team",
         r"prevent all effects of attacks including damage done to the pokemon this card is "
         r"attached to excluding pokemon ex by your opponents team plasma pokemon",
         "prevents_all_from",
         lambda m: ["None", 'attacker_named_team("team plasma")', "effects_too=True"],
         kind="passive"),
    Rule("tool-condition-immunity",
         r"the pokemon this card is attached to cant be affected by any special conditions "
         r"remove any special conditions affecting that pokemon",
         "holder_condition_immunity", lambda m: [], kind="passive"),
    Rule("ancient-booster",
         r"the ancient pokemon this card is attached to gets (?P<hp>\d+) hp recovers from all "
         r"special conditions and cant be affected by any special conditions",
         "combined",
         lambda m: ["gated_hp_bonus(%s, pokemon_of_subtype(\"Ancient\"))" % m.group("hp"),
                    'holder_condition_immunity(pokemon_of_subtype("Ancient"))'],
         kind="passive"),
    Rule("look-top-one-of-shuffle",
         r"look at the top (?P<n>\d+) cards from your deck choose (?P<take>\d+) "
         r"(?P<cat>[a-z0-9 ]+?) from those cards show it to your opponent and put it into your "
         r"hand put the other (?P<rest>\d+) cards back on top of your deck shuffle your deck "
         r"afterward",
         "look_at_top",
         lambda m: [m.group("n"), "take=" + m.group("take"), "predicate=" + _pred(m.group("cat")),
                    'rest="shuffle"'],
         module="support_common"),
    Rule("look-top-one-of-back",
         r"look at the top (?P<n>\d+) cards of your deck and choose (?P<take>\d+) "
         r"(?P<cat>[a-z0-9 ]+?) show it to your opponent and put it into your hand put the "
         r"(?P<rest>\d+) other cards back on top of your deck in any order",
         "look_at_top",
         lambda m: [m.group("n"), "take=" + m.group("take"), "predicate=" + _pred(m.group("cat")),
                    'rest="back"'],
         module="support_common"),
    Rule("look-top-trainer-except",
         r"look at the top (?P<n>\d+) cards of your deck you may reveal (?P<take>\d+) trainer card "
         r"you find there except (?P<except>[a-z0-9 ]+?) and put it into your hand shuffle the "
         r"other cards back into your deck",
         "look_at_top",
         lambda m: [m.group("n"), "take=" + m.group("take"),
                    'predicate=trainer_card_other_than("%s")' % m.group("except"),
                    'rest="shuffle"', "minimum=0"],
         module="support_common"),
    Rule("protect-chosen-next-turn",
         r"choose (?P<n>\d+) of your pokemon in play during your opponents next turn prevent all "
         r"damage from and effects of attacks done to that pokemon(?: by your opponents "
         r"pokemon(?: ex)?)?",
         "protect_chosen_next_turn", lambda m: [m.group("n")]),
    Rule("extra-prize-on-tera-ko",
         r"during this turn if your opponents active pokemon is knocked out by damage from 1 "
         r"attack used by your tera pokemon take (?P<n>\d+) more prize cards?",
         "extra_prize_on_ko", lambda m: ["tera_attacker()", m.group("n")]),
    Rule("look-top-pokemon-or-energy-back",
         r"look at the top (?P<n>\d+) cards of your deck you may reveal (?P<take>\d+) "
         r"(?P<cat>[a-z0-9 ]+?) you find there and put it into your hand put the other cards back "
         r"in any order",
         "look_at_top",
         lambda m: [m.group("n"), "take=" + m.group("take"), "predicate=" + _pred(m.group("cat")),
                    'rest="back"', "minimum=0"],
         module="support_common"),
    Rule("look-top-two-of-back",
         r"look at the top (?P<n>\d+) cards of your deck and choose (?P<take>\d+) "
         r"(?P<cat>[a-z0-9 ]+?) show it to your opponent and put it into your hand put the "
         r"(?P<rest>\d+) other cards back on top of your deck in any order",
         "look_at_top",
         lambda m: [m.group("n"), "take=" + m.group("take"), "predicate=" + _pred(m.group("cat")),
                    'rest="back"'],
         module="support_common"),
    Rule("beast-ring",
         r"search your deck for up to (?P<n>\d+) basic energy cards and attach them to "
         r"(?P<target>\d+) of your (?P<sub>[a-z ]+?) then shuffle your deck",
         "search_attach_energy",
         lambda m: ["is_basic_energy_card", "count=" + m.group("n"),
                    "target_pred=pokemon_of_subtype(%s)" % _subtype_literal(m.group("sub")),
                    "distribute=False"],
         module="support_common"),
    Rule("search-rule-box-free-plus-students",
         r"search your deck for (?P<n>\d+) pokemon that doesnt have 1 rule box reveal it and put "
         r"it into your hand for each (?P<extra>[a-z ]+?) card not including this card in your "
         r"discard pile you may search for (?P<more>\d+) additional pokemon in this way then "
         r"shuffle your deck",
         "search_rule_box_free_plus_students",
         lambda m: ['"%s"' % m.group("extra")]),
    Rule("switch-team-then-gust",
         r"switch your active (?P<owner>[a-z ]+?) pokemon with (?P<n>\d+) of your benched "
         r"(?P=owner) pokemon if you do switch in (?P<gust>\d+) of your opponents benched pokemon "
         r"to the active spot",
         "switch_team_then_gust",
         lambda m: ['"%s"' % OWNER_NAMES.get(m.group("owner"), m.group("owner"))]),
    Rule("discard-energy-draw-per-typed",
         r"discard (?P<n>\d+) energy card from your hand in order to draw cards until you have as "
         r"many cards in your hand as you have (?P<type>[a-z]+) pokemon in play",
         "with_discard_cost",
         lambda m: [m.group("n"),
                    'draw_until_per_typed_pokemon("%s")' % m.group("type")]),
    Rule("gambler",
         r"shuffle your hand into your deck flip (?P<coins>\d+) coin if heads draw (?P<a>\d+) "
         r"cards? if tails draw (?P<b>\d+) cards?",
         "shuffle_hand_flip_draw", lambda m: [m.group("a"), m.group("b")]),
    Rule("dual-ball",
         r"flip (?P<coins>\d+) coins for each heads search your deck for (?P<n>\d+) basic pokemon "
         r"card other than (?P<skip>\d+) baby pokemon card show it to your opponent and put it "
         r"into your hand",
         "flip_search_basic_count", lambda m: [m.group("coins")]),
    Rule("look-top-choose-discard-rest",
         r"look at the top (?P<n>\d+) cards of your deck choose (?P<take>\d+) of those cards and "
         r"put them into your hand discard the rest",
         "look_at_top",
         lambda m: [m.group("n"), "take=" + m.group("take"), 'rest="discard"', "minimum=0"],
         module="support_common"),
    Rule("retaliate-on-attack",
         r"if the pokemon this card is attached to is (?:your active pokemon|in the active spot) "
         r"and is damage(?:d)? by (?P<n>\d+) (?:opponents attack|attack from your opponents "
         r"pokemon) even if (?:that pokemon|it) is knocked out put (?P<counters>\d+) damage "
         r"counters? on the attacking pokemon",
         "retaliate_on_attack", lambda m: [m.group("counters")], kind="passive"),
    Rule("look-top-reorder",
         r"look at the top (?P<n>\d+) cards of your deck and put them back on top of your deck in "
         r"any order",
         "look_top_reorder", lambda m: [m.group("n")]),
    Rule("look-top-same-order",
         r"look at the top (?P<n>\d+) cards of your deck and put them back in the same order",
         "look_top_peek", lambda m: [m.group("n")]),
    Rule("search-hand-hp-qualifier",
         r"search your deck for (?:up to )?(?P<n>\d+ )?(?P<cat>[a-z0-9 ]+?) with (?P<hp>\d+) hp or "
         r"less (?:reveal|show) (?:it|them)(?: to your opponent)? and put (?:it|them) into your "
         r"hand" + SHUFFLE_TAIL,
         "search_to_hand",
         lambda m: ["all_of(%s, pokemon_with_hp_at_most(%s))"
                    % (_pred(m.group("cat")), m.group("hp")),
                    "count=" + str(_count(m.group("n")))],
         module="support_common"),
    Rule("search-hand-retreat-qualifier",
         r"search your deck for (?:up to )?(?P<n>\d+ )?(?P<cat>[a-z0-9 ]+?) with (?P<n2>\d+) retreat "
         r"cost of (?P<cost>\d+) or more (?:reveal|show) (?:it|them)(?: to your opponent)? and put "
         r"(?:it|them) into your hand" + SHUFFLE_TAIL,
         "search_to_hand",
         lambda m: ["all_of(%s, pokemon_with_retreat_at_least(%s))"
                    % (_pred(m.group("cat")), m.group("cost")),
                    "count=" + str(_count(m.group("n")))],
         module="support_common"),
    Rule("search-hand-word-in-name",
         r"search your deck for (?:up to )?(?P<n>\d+ )?(?P<cat>[a-z0-9 ]+?) that have the word "
         r"(?P<word>[a-z]+) in their name (?:reveal|show) (?:it|them) and put (?:it|them) into "
         r"your hand" + SHUFFLE_TAIL,
         "search_to_hand",
         lambda m: ["all_of(%s, card_named_contains(\"%s\"))"
                    % (_pred(m.group("cat")), m.group("word")),
                    "count=" + str(_count(m.group("n")))],
         module="support_common"),
    Rule("recycle-from-discard",
         r"flip (?P<coins>\d+) coin if heads put (?P<n>\d+) card in your discard pile on top of "
         r"your deck",
         "recycle_from_discard", lambda m: [m.group("n")]),
    Rule("look-top-two-take-one-bottom",
         r"look at the top (?P<n>\d+) cards of your deck choose (?P<take>\d+) of them and put it "
         r"into your hand put the other card on the bottom of your deck",
         "look_at_top",
         lambda m: [m.group("n"), "take=" + m.group("take"), 'rest="bottom"', "minimum=0"],
         module="support_common"),
    Rule("tool-takes-less-from-typed-attacker",
         r"if the pokemon this card is attached to is damaged by (?P<n>\d+) attack from your "
         r"opponents (?P<type>[a-z]+) pokemon it takes (?P<amount>\d+) less damage after applying "
         r"weakness and resistance(?: and discard this card)?",
         "takes_less_from",
         lambda m: [m.group("amount"), "None",
                    'attacker_of_types("%s")' % m.group("type")],
         kind="passive"),
    Rule("tool-retreat-discount-and-return",
         r"the retreat cost of the pokemon this card is attached to is (?P<count>colorless) less "
         r"if this card is discarded from play put it into your hand instead of the discard pile",
         "holder_retreat_discount",
         lambda m: [str(_colorless_count(m.group("count")))], kind="passive"),
    Rule("retaliate-poison",
         r"if the pokemon this card is attached to is your active pokemon and is damaged by "
         r"(?P<n>\d+) opponents attack even if this pokemon is knocked out the attacking pokemon "
         r"is now poisoned",
         "retaliate_poison", lambda m: [], kind="passive"),
    Rule("tool-takes-less-metal-holder",
         r"if this card is attached to (?P<n>\d+) of your pokemon discard it at the end of your "
         r"opponents turn the (?P<type>[a-z]+) pokemon this card is attached to takes "
         r"(?P<amount>\d+) less damage from your opponents attacks after applying weakness and "
         r"resistance",
         "takes_less_from",
         lambda m: [m.group("amount"), 'pokemon_of("%s")' % m.group("type")],
         kind="passive"),
    Rule("search-any-combination-of-two",
         r"search your deck for up to (?P<n>\d+) in any combination of (?P<a>[a-z0-9 ]+?) and "
         r"(?P<b>[a-z0-9 ]+?) (?:reveal|show) (?:it|them) and put (?:it|them) into your hand" +
         SHUFFLE_TAIL,
         "search_to_hand",
         lambda m: ["any_of(%s, %s)" % (_pred_typed_subtype(m.group("a")),
                                        _pred_typed_subtype(m.group("b"))),
                    "count=" + m.group("n")],
         module="support_common"),
    Rule("shuffle-hand-draw-lock-trainers",
         r"shuffle your hand into your deck then draw (?P<n>\d+) cards you cant play any more "
         r"trainer cards this turn",
         "shuffle_hand_draw_lock_trainers", lambda m: [m.group("n")]),
    Rule("discard-typed-pokemon-bench-then-draw",
         r"put (?P<n>\d+) (?P<type>[a-z]+) pokemon from your discard pile onto your bench then draw "
         r"(?P<draw>\d+) cards",
         "discard_typed_pokemon_to_bench_then_draw",
         lambda m: ['"%s"' % m.group("type"), m.group("draw")]),
    Rule("breeder-stage-two-onto-basic",
         r"put (?P<n>\d+) stage 2 evolution card from your hand on the matching basic pokemon(?: you "
         r"can only play this card when you would be allowed to evolve that pokemon anyway| you "
         r"can play this card only when you would be allowed to evolve that pokemon anyway)",
         "rare_candy", lambda m: []),
    Rule("colress-draw",
         r"shuffle your hand into your deck then draw (?P<n>\d+) number of cards equal to the "
         r"number of benched pokemon both yours and your opponents",
         "colress_draw", lambda m: []),
    Rule("full-heal",
         r"your active pokemon is no longer asleep confused paralyzed or poisoned",
         "cure_conditions_effect", lambda m: [], module="support_common"),
    Rule("gust-of-wind",
         r"choose (?P<n>\d+) of your opponents benched pokemon and switch it with his or her "
         r"active pokemon",
         "opponent_bench_to_active", lambda m: []),
    Rule("energy-removal",
         r"choose (?P<n>\d+) energy card attached to (?P<target>\d+) of your opponents pokemon and "
         r"discard it",
         "discard_opponent_energy", lambda m: [m.group("n")]),
    Rule("maintenance",
         r"shuffle (?P<n>\d+) of the other cards from your hand into your deck in order to draw "
         r"(?P<draw>\d+) card",
         "shuffle_hand_cards_draw", lambda m: [m.group("n"), m.group("draw")]),
    Rule("max-potion-then",
         r"heal all damage from (?P<n>\d+) of your pokemon then discard all energy attached to that "
         r"pokemon",
         "heal_all_then_discard_energy", lambda m: []),
    Rule("super-rod",
         r"shuffle (?P<n>\d+) in any combination of (?P<a>[a-z ]+?) and (?P<b>[a-z ]+?) from your "
         r"discard pile back into your deck",
         "shuffle_discard_combo_into_deck",
         lambda m: [m.group("n"), _pred(m.group("a")), _pred(m.group("b"))]),
    Rule("copycat",
         r"shuffle your hand into your deck then (?:count the number of cards in your opponents hand "
         r"and )?draw that many cards",
         "copycat_draw", lambda m: []),
    Rule("draw-then-bottom",
         r"draw (?P<n>\d+) cards then choose (?P<k>\d+) card from your hand and put it on the "
         r"bottom of your deck",
         "draw_then_bottom", lambda m: [m.group("n"), m.group("k")]),
    Rule("moo-moo-milk",
         r"choose (?P<n>\d+) of your pokemon flip (?P<coins>\d+) coins remove (?P<per>\d+) damage "
         r"counters times the number of heads from that pokemon(?: if the pokemon has fewer damage "
         r"counters than that remove all of them)?",
         "flip_heal_chosen", lambda m: [m.group("per"), m.group("coins")]),
    Rule("look-bottom-to-bench",
         r"look at the bottom (?P<n>\d+) cards of your deck you may reveal (?P<take>\d+) "
         r"(?P<who>[a-z0-9 ]+?) you find there and put it onto your bench shuffle the other cards "
         r"back into your deck",
         "look_bottom_to_bench",
         lambda m: [m.group("n"), _who(m.group("who"))]),
    Rule("look-bottom-to-hand",
         r"look at the (?P<n>\d+) cards from the bottom of your deck choose (?P<take>\d+) "
         r"(?P<who>[a-z0-9 ]+?) you find there show it to your opponent and put it into your hand "
         r"put the other cards back on the bottom of your deck in any order",
         "look_bottom_to_hand",
         lambda m: [m.group("n"), m.group("take"), _who(m.group("who"))]),
    Rule("escape-rope",
         r"each player switches (?:his or her|their) active pokemon with (?P<n>\d+) of (?:his or "
         r"her|their) benched pokemon your opponent switches first if (?P<x>\d+) player does not "
         r"have (?P<same>\d+) benched pokemon (?:he or she|that player) doesnt switch pokemon",
         "escape_rope", lambda m: [], bare=True),
    Rule("search-deck-or-discard-lv-x",
         r"search your deck or your discard pile for (?P<n>\d+) pokemon lv x show it to your "
         r"opponent and put it into your hand if you search your deck shuffle your deck afterward",
         "search_deck_or_discard_to_hand",
         lambda m: ["pokemon_lv_x()", "count=" + m.group("n")]),
    # --- Both-sides stadiums -------------------------------------------
    Rule("stadium-boost",
         r"(?:the attacks of|attacks used by) (?:each )?(?P<cat>[a-z0-9 ]+?)(?: in play)? both "
         r"yours and your opponents do (?P<amount>\d+) more damage to the (?:opponents active "
         r"pokemon|defending pokemon(?P<ex> ex)?) before applying weakness and resistance",
         "stadium_damage_boost",
         lambda m: [m.group("amount"), _union(m.group("cat")),
                    "target=" + ("is_pokemon_EX" if m.group("ex") else "None")],
         kind="passive"),
    Rule("stadium-takes-less-for",
         r"(?P<cat>[a-z0-9 ]+?) both yours and your opponents take (?P<amount>\d+) less damage "
         r"from (?:attacks from the opponents pokemon|the opponents attacks) after applying "
         r"weakness and resistance",
         "stadium_takes_less_for",
         lambda m: [m.group("amount"), _union(m.group("cat"))], kind="passive"),
    Rule("stadium-no-retreat",
         r"(?P<cat>[a-z0-9 ]+?) in play both yours and your opponents (?:have|has) no retreat "
         r"cost",
         "stadium_no_retreat", lambda m: [_union(m.group("cat"))], kind="passive"),
    Rule("stadium-retreat-shift",
         r"the retreat cost (?:of|for) each (?P<cat>[a-z0-9 ]+?)(?: (?:in|is) play)?(?: both "
         r"yours and your opponents)? is (?P<count>colorless(?: ?colorless)*) (?P<dir>less|more)",
         "stadium_retreat_shift",
         lambda m: [("-" if m.group("dir") == "less" else "")
                    + str(_colorless_count(m.group("count"))), _union(m.group("cat"))],
         kind="passive"),
    Rule("stadium-no-resistance",
         r"each pokemon in play has no resistance",
         "stadium_no_resistance", lambda m: [], kind="passive"),

    # --- Evolution shortcuts ---------------------------------------------
    Rule("evolve-from-hand",
         r"choose (?P<n>\d+) of your basic pokemon in play if you have (?P<stages>1 stage 1 or "
         r"stage 2 card|1 stage 1 card|1 stage 2 card) (?:in your hand )?that evolves from that "
         r"pokemon(?: in your hand)? put that card on(?:to)? the basic pokemon(?: to evolve it)?"
         r"(?: this counts as evolving that pokemon)?(?: you cant use this card during your first "
         r"turn or on 1 basic pokemon that was put into play this turn)?",
         "evolve_from_hand", lambda m: []),
    Rule("rare-candy",
         r"choose (?P<n>\d+) of your basic pokemon in play if you have 1 stage 2 card in your "
         r"hand that evolves from that pokemon put that card on(?:to)? the basic pokemon to "
         r"evolve it skipping the stage 1.*",
         "rare_candy", lambda m: []),
]

_KEYWORD_ARGUMENTS = {
    "count", "take", "predicate", "amount", "scope", "to", "flip", "target",
    "energy_pred", "condition_cure", "draw", "minimum", "reveal", "prompt",
}


def _argument_symbols(args):
    """Names an argument expression references (predicates, mostly)."""
    names = set()
    for arg in args:
        value = arg.split("=", 1)[1] if "=" in arg else arg
        head = value.split("(")[0].strip()
        if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", head) \
                and head not in _KEYWORD_ARGUMENTS \
                and head not in ("None", "True", "False"):
            names.add(head)
    return names


# Wrappers: a requirement or coin flip the printing puts in front of an effect
# that is otherwise a shape this table already knows. Each entry maps the
# leading clause onto a combinator in trainers.py and keeps the remainder as
# the inner effect.
# Prefix (or, for " your turn ends", suffix) clauses that only gate or finish
# the card rather than changing the effect: they land on condition= or wrap
# the effect in ends_turn_after.
CONDITION_PREFIXES = [
    (re.compile(r"^you can (?:use|play) this card only if your opponent has (?P<n>\d+) or fewer "
                r"prize cards remaining "), "opponent_prizes_at_most"),
    (re.compile(r"^you can (?:use|play) this card only if your opponent has exactly (?P<n>\d+) "
                r"prize cards remaining "), "opponent_prizes_exactly"),
    (re.compile(r"^you can (?:use|play) this card only if your opponent has exactly (?P<low>\d+) "
                r"or (?P<high>\d+) prize cards remaining "), "opponent_prizes_in"),
    (re.compile(r"^you can (?:use|play) this card only if you have (?P<n>\d+) or fewer other "
                r"cards in your hand "), "hand_at_most"),
    (re.compile(r"^you can (?:use|play) this card only when it is the last card in your hand "),
     "hand_is_last"),
    (re.compile(r"^you can (?:use|play) this card only if you have more prize cards remaining "
                r"than your opponent "), "behind_on_prizes"),
    (re.compile(r"^you can (?:use|play) this card only if you have any (?P<sub>[a-z]+) pokemon "
                r"in play "), "has_subtype_in_play"),
    (re.compile(r"^you can (?:use|play) this card only if your opponents active pokemon is "
                r"(?P<cond>[a-z]+) "), "opponent_active_has"),
    (re.compile(r"^you can (?:use|play) this card only if your opponents active pokemon is "
                r"(?P<n>\d+) (?P<stage>stage 1|stage 2|basic) pokemon "), "opponent_active_is"),
]

ENDS_TURN = re.compile(r" your turn ends$")

WRAPPERS = [
    (re.compile(r"^flip 1 coin if heads "), "if_heads", None),
    (re.compile(r"^you may "), None, None),
    (re.compile(r"^you can (?:use|play) this card only if you discard (?P<n>\d+) other cards? "
                r"from your hand "), "with_discard_cost", None),
    (re.compile(r"^you can (?:use|play) this card only if you discard another card from your "
                r"hand "), "with_discard_cost", "1"),
    (re.compile(r"^discard (?P<n>\d+) cards? from your hand if you do "),
     "with_discard_cost", None),
    (re.compile(r"^discard (?P<n>\d+) card from your hand in order to play this card "),
     "with_discard_cost", None),
    (re.compile(r"^discard (?P<n>\d+) of the other cards in your hand in order to "),
     "with_discard_cost", None),
    (re.compile(r"^discard (?P<n>\d+) cards? from your hand if you cant discard \d+ cards "
                r"you cant play this card "), "with_discard_cost", None),
    (re.compile(r"^if you go first you may use this card during your first turn "),
     None, None),
]

RESOLVE_DEPTH = 4


def resolve(text, depth=0):
    """The wiring for a canonical rules text, or None.

    Returns {"rule", "expr", "symbols"} where `expr` is the `effect=` source
    expression. Direct shapes win; otherwise a leading requirement clause is
    peeled off and its remainder resolved, so "Flip a coin. If heads, search
    your deck for ..." reuses the search implementation.
    """
    if not text or depth > RESOLVE_DEPTH:
        return None
    for rule in RULES:
        found = rule.match(text)
        if found is not None:
            return found
    for pattern, factory in CONDITION_PREFIXES:
        found = pattern.match(text)
        if not found:
            continue
        inner = resolve(text[found.end():], depth + 1)
        if inner is None:
            continue
        groups = found.groupdict()
        if factory == "has_subtype_in_play":
            condition = '%s("%s")' % (factory, groups["sub"].capitalize())
        elif factory == "opponent_active_has":
            condition = '%s("%s")' % (factory, groups["cond"].upper())
        elif factory == "opponent_active_is":
            stage_pred = {"stage 1": "is_stage_one", "stage 2": "is_stage_two",
                          "basic": "is_basic_pokemon"}[groups["stage"]]
            condition = "opponent_active_is(%s)" % stage_pred
        elif factory == "opponent_prizes_in":
            condition = "opponent_prizes_in(%s, %s)" % (groups["low"], groups["high"])
        elif "n" in groups:
            condition = "%s(%s)" % (factory, groups["n"])
        else:
            condition = "%s()" % factory
        return dict(inner, condition=condition)

    match = ENDS_TURN.search(text)
    if match:
        inner = resolve(text[:match.start()], depth + 1)
        if inner is not None:
            return {
                "rule": "ends-turn+" + inner["rule"],
                "expr": "ends_turn_after(%s)" % inner["expr"],
                "symbols": inner["symbols"] | {"ends_turn_after"},
            }

    for pattern, combinator, cost in WRAPPERS:
        found = pattern.match(text)
        if not found:
            continue
        inner = resolve(text[found.end():], depth + 1)
        if inner is None:
            continue
        if combinator is None:
            return dict(inner, rule="first-turn+" + inner["rule"])
        if combinator == "if_heads":
            return {
                "rule": "if-heads+" + inner["rule"],
                "expr": "if_heads(%s)" % inner["expr"],
                "symbols": inner["symbols"] | {"if_heads"},
            }
        amount = cost if cost is not None else found.group("n")
        return {
            "rule": combinator + "+" + inner["rule"],
            "expr": "%s(%s, %s)" % (combinator, amount, inner["expr"]),
            "symbols": inner["symbols"] | {combinator},
        }
    return None


# --- Modal cards ------------------------------------------------------------

MODAL_HEAD = re.compile(r"^\s*choose (1 or both|1|one)(?:\s+of the following)?\s*:?\s*", re.I)


def resolve_modal(raw_text):
    """Wire a "Choose 1: A / B" card from its printed bullets.

    Both the bullets and the head come from the raw rules text, because the
    canonical form has lost the bullet separators. Every bullet has to resolve
    to a known shape: a modal card wired with one option missing would let the
    player pick something that does nothing.
    """
    if not raw_text or "\u2022" not in raw_text:
        return None
    head = MODAL_HEAD.match(raw_text)
    if head is None:
        return None
    body = raw_text[head.end():]
    bullets = [part.strip(" .") for part in body.split("\u2022") if part.strip(" .")]
    if len(bullets) < 2:
        return None
    options = []
    for bullet in bullets:
        inner = resolve(canonicalize(bullet))
        if inner is None or inner.get("kind") != "effect":
            return None
        label = _label(bullet)
        options.append((label, inner))
    expression = "%s([%s])" % (
        "choose_any" if "both" in head.group(1).lower() else "choose_one",
        ", ".join('("%s", %s)' % (label, inner["expr"]) for label, inner in options),
    )
    symbols = set()
    for _option_label, inner in options:
        symbols |= inner["symbols"]
    symbols.add("choose_any" if "both" in head.group(1).lower() else "choose_one")
    return {"rule": "modal", "expr": expression, "symbols": symbols}


def _label(bullet):
    """A short button label from a printed bullet."""
    text = re.sub(r"\s+", " ", bullet).strip()
    return text[:70].replace('"', "'").replace("\\", "/")


def canonicalize(text):
    """Same normalization trainer_coverage applies, for bullet sub-text."""
    import trainer_coverage
    return trainer_coverage.canonical_text([text])


STADIUM_ABILITY_HEADS = (
    "once during each players turn that player may ",
    "once during each players turn the player may ",
    "once during each players turn before attacking that player may ",
    "once during each players turn before attacking the player may ",
)


def resolve_stadium_ability(text):
    """A Stadium's "Once during each player's turn, that player may <X>":
    <X> is worded for "that player", so it is rewritten in the second person
    and resolved like any trainer effect. Text that also names the opponent
    is declined, because "their" can no longer be told apart."""
    head = next((h for h in STADIUM_ABILITY_HEADS if text.startswith(h)), None)
    if head is None:
        return None
    inner = text[len(head):]
    if "opponent" in inner:
        return None
    inner = inner.replace("then that player shuffles their deck", "then shuffle your deck")
    inner = inner.replace("and shuffle their deck", "then shuffle your deck")
    inner = inner.replace("they have", "you have").replace("they do", "you do")
    inner = (inner.replace("he or she", "you").replace("his or her", "your")
             .replace("that player", "you").replace("the player", "you")
             .replace("their", "your"))
    THIRD_PERSON = {"draws": "draw", "searches": "search", "chooses": "choose",
                    "discards": "discard", "flips": "flip", "puts": "put",
                    "shuffles": "shuffle", "removes": "remove", "heals": "heal",
                    "attaches": "attach", "reveals": "reveal", "takes": "take",
                    "shows": "show", "places": "place"}
    inner = re.sub(r"\b(%s)\b" % "|".join(THIRD_PERSON),
                   lambda m: THIRD_PERSON[m.group(1)], inner)
    inner = inner.replace("if heads you ", "if heads ")
    inner = inner.replace("if you do you ", "if you do ")
    ends_turn = False
    tail = re.search(r" if \d+ player searches (?:their|your) deck in this way "
                    r"(?:their|your) turn ends$", inner)
    if tail is not None:
        inner = inner[:tail.start()]
        ends_turn = True
    found = resolve(inner)
    if found is None or found.get("kind", "effect") != "effect" or found.get("condition"):
        return None
    expr = found["expr"]
    symbols = found["symbols"] | {"stadium_ability"}
    if ends_turn:
        expr = "ends_turn_after(%s)" % expr
        symbols.add("ends_turn_after")
    return {"rule": "stadium-ability:" + found["rule"], "expr": expr,
            "symbols": symbols, "kind": "ability"}

