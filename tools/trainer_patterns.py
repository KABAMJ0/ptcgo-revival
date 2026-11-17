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
    "cyllenes": "cyllene", "colresss": "colress", "klaras": "klara",
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
    text = re.sub(r"^(up to|any number of) ", "", text)
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
            parts = [resolve_predicate(part) for part in text.split(joiner)]
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
        owner = 'named("%s")' % owner_word
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
         r"during this turn attacks used by your pokemon do (?P<amount>\d+) more damage to "
         r"your opponents active pokemon(?: ex| v| vstar| gx)?(?: before applying weakness and "
         r"resistance)?",
         "turn_damage_boost", lambda m: [m.group("amount")]),
    Rule("turn-damage-boost-ex",
         r"during this turn attacks used by your pokemon do (?P<amount>\d+) more damage to "
         r"your opponents active pokemon ex",
         "turn_damage_boost", lambda m: [m.group("amount")]),
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
         "heal_all_then_energy_to_hand", lambda m: []),
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
]

ENDS_TURN = re.compile(r" your turn ends$")

WRAPPERS = [
    (re.compile(r"^flip 1 coin if heads "), "if_heads", None),
    (re.compile(r"^you can (?:use|play) this card only if you discard (?P<n>\d+) other cards? "
                r"from your hand "), "with_discard_cost", None),
    (re.compile(r"^you can (?:use|play) this card only if you discard another card from your "
                r"hand "), "with_discard_cost", "1"),
    (re.compile(r"^discard (?P<n>\d+) cards? from your hand if you do "),
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
