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

_TYPED_ENERGY = re.compile(
    r"^(?:1 |up to )?basic (?P<type>%s) energy cards?$" % TYPE_NAMES)
_TYPED_ENERGY_ANY = re.compile(r"^(?:1 )?(?P<type>%s) energy cards?$" % TYPE_NAMES)
_TYPED_POKEMON = re.compile(r"^(?:1 )?(?P<type>%s) pokemon$" % TYPE_NAMES)


def resolve_predicate(phrase):
    """Expression source for a printed card-category phrase, or Unresolved.

    Returns the string "None" when the phrase means "any card", and raises
    Unresolved for a phrase with no implementation, which makes the whole rule
    decline rather than pick a wrong filter.
    """
    text = re.sub(r"\s+", " ", (phrase or "").strip().lower())
    text = re.sub(r"^(up to|any number of) ", "", text)
    text = re.sub(r"^(1|a|an) ", "", text)
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
    for joiner, combinator in ((" or ", "any_of"), (" and ", "all_of")):
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
    __slots__ = ("rule_id", "pattern", "factory", "module", "builder", "bare")

    def __init__(self, rule_id, pattern, factory, builder, module="trainers",
                 bare=False):
        self.rule_id = rule_id
        self.pattern = re.compile(pattern + r"\Z")
        self.factory = factory
        self.module = module
        self.builder = builder
        # bare: the factory IS a `async def effect(ctx)` coroutine (Switch),
        # so the script passes it directly instead of calling a factory.
        self.bare = bare

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
        return {"rule": self.rule_id, "expr": expression,
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
    Rule("draw-until", r"draw cards? until you have (?P<n>\d+) cards? in your hand",
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
    Rule("heal-each-own",
         r"heal (?P<amount>\d+) damage from each of your pokemon",
         "heal_item", lambda m: ["amount=" + m.group("amount"), 'scope="each_own"'],
         module="support_common"),
    Rule("heal-all-one",
         r"heal all damage from (?P<n>\d+) of your pokemon",
         "heal_all_from_one", lambda m: [], module="support_common"),
    Rule("remove-counters",
         r"remove (?P<counters>\d+) damage counters? from (?P<n>\d+) of your pokemon"
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
         r"(?:cards )?attached to it into your hand",
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
         r"any cards on the bottom of their deck in this way)? then each player draws "
         r"(?P<n>\d+) cards? for each of (?:their|his or her) remaining prize cards",
         "each_player_shuffle_draw_per_prize", lambda m: []),
    Rule("draw-until-first-turn",
         r"draw cards? until you have (?P<hand>\d+) cards? in your hand if its your first "
         r"turn draw cards? until you have (?P<first>\d+) cards? in your hand",
         "first_turn_draw_until", lambda m: [m.group("hand"), m.group("first")]),

    # --- Energy -----------------------------------------------------------
    Rule("move-basic-energy",
         r"move (?:1 )?basic energy(?: card)?s? (?:attached to |from )?(?P<n>\d+) of your pokemon "
         r"to another of your pokemon",
         "move_basic_energy", lambda m: ["predicate=is_basic_energy_card"]),
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
         r"(?P<amount>\d+) more damage to your opponents active pokemon",
         "turn_damage_boost", lambda m: [m.group("amount"), "exclude_rule_box=True"]),
    Rule("turn-damage-boost-typed",
         r"during this turn attacks used by your (?P<type>[a-z]+) pokemon do (?P<amount>\d+) "
         r"more damage to your opponents active pokemon",
         "turn_damage_boost", lambda m: _typed_boost(m)),

    # --- Evolution shortcuts ---------------------------------------------
    Rule("evolve-from-hand",
         r"choose (?P<n>\d+) of your basic pokemon in play if you have (?P<stages>1 stage 1 or "
         r"stage 2 card|1 stage 1 card|1 stage 2 card) that evolves from that pokemon"
         r"(?: in your hand)? put that card on the basic pokemon"
         r"(?: this counts as evolving that pokemon)?",
         "evolve_from_hand", lambda m: []),
    Rule("rare-candy",
         r"choose (?P<n>\d+) of your basic pokemon in play if you have 1 stage 2 card in your "
         r"hand that evolves from that pokemon put that card onto the basic pokemon to evolve "
         r"it skipping the stage 1.*",
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
WRAPPERS = [
    (re.compile(r"^flip 1 coin if heads "), "if_heads", None),
    (re.compile(r"^you can (?:use|play) this card only if you discard (?P<n>\d+) other cards? "
                r"from your hand "), "with_discard_cost", None),
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
