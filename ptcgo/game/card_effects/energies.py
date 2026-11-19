"""Behaviors for the Special Energy cards of the Lugia VSTAR archetype deck."""

from ptcgo.game.attributes import AttrID, PokemonStage, PokemonTypes
from ptcgo.game.data_utils import def_for, is_pokemon_v, subtypes_for
from ptcgo.game.session.constants import BENCH_CAPACITY
from ptcgo.game.session.effects import is_basic_pokemon
from ptcgo.game.session.passives import Passive, carrier_pokemon

# Aurora Energy provides every type of Energy, one at a time.
ALL_TYPES_ONE_AT_A_TIME = [
    [t] for t in (
        PokemonTypes.GRASS, PokemonTypes.FIRE, PokemonTypes.WATER,
        PokemonTypes.LIGHTNING, PokemonTypes.PSYCHIC, PokemonTypes.FIGHTING,
        PokemonTypes.DARKNESS, PokemonTypes.METAL, PokemonTypes.FAIRY,
        PokemonTypes.DRAGON, PokemonTypes.COLORLESS,
    )
]

# Same as ALL_TYPES_ONE_AT_A_TIME but each option provides two of that type
# (Rainbow Energy's "provides 2 Energy of any 1 type" era).
ALL_TYPES_TWO_AT_A_TIME = [
    [t, t] for t in (
        PokemonTypes.GRASS, PokemonTypes.FIRE, PokemonTypes.WATER,
        PokemonTypes.LIGHTNING, PokemonTypes.PSYCHIC, PokemonTypes.FIGHTING,
        PokemonTypes.DARKNESS, PokemonTypes.METAL, PokemonTypes.FAIRY,
        PokemonTypes.DRAGON, PokemonTypes.COLORLESS,
    )
]


def _pokemon_has_type(pokemon, pokemon_type: PokemonTypes) -> bool:
    return pokemon_type.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])


def another_card_in_hand(board, player_id) -> bool:
    """Aurora's gate: the hand must hold a second card to discard."""
    hand = board.find_player_area(player_id, "hand")
    return hand is not None and len(hand.children) >= 2


async def aurora_attach_cost(ctx) -> bool:
    """Attaching Aurora Energy costs discarding another card from hand."""
    picks = await ctx.discard_from_hand(
        1, prompt="Discard a card to attach Aurora Energy", exclude=[ctx.source]
    )
    return bool(picks)


async def capture_on_attach(ctx):
    """On attach from hand: search the deck for a Basic onto the Bench."""
    if len(ctx.my_bench()) == BENCH_CAPACITY:
        return
    
    picks = await ctx.search_deck(
        is_basic_pokemon, count=1, minimum=0,
        prompt="Choose a Basic Pokémon to put onto your Bench.",
    )
    for card in picks:
        await ctx.bench_pokemon(card)
    await ctx.shuffle_deck()


async def speed_lightning_on_attach(ctx):
    """On attach from hand: draw 2 cards only if the target is a Lightning Pokemon."""
    if _pokemon_has_type(ctx.attached_to, PokemonTypes.LIGHTNING):
        await ctx.draw_cards(2)


class PowerfulColorlessPassive(Passive):
    """+20 damage to the opponent's Active from the Colorless carrier."""

    def modify_damage_dealt(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        pokemon = carrier_pokemon(carrier)
        if pokemon is not calc.attacker:
            return
        if _pokemon_has_type(pokemon, PokemonTypes.COLORLESS):
            calc.amount += 20


class DoubleTurboPassive(Passive):
    """The carrier's attacks do 20 less damage."""

    def modify_damage_dealt(self, calc, carrier):
        if (
            calc.is_attack
            and calc.is_opposing
            and carrier_pokemon(carrier) is calc.attacker
        ):
            calc.amount -= 20


class HeatFirePassive(Passive):
    """The Fire Pokemon this card is attached to gets +20 max HP."""

    def max_hp_bonus(self, pokemon, carrier):
        if carrier_pokemon(carrier) is pokemon \
                and _pokemon_has_type(pokemon, PokemonTypes.FIRE):
            return 20
        return 0


async def gift_energy_on_ko(ctx):
    """When the carrier is Knocked Out by an opponent's attack: draw cards
    until you have 7 cards in your hand."""
    await ctx.draw_until(7)


class VGuardPassive(Passive):
    """The carrier takes 30 less damage from opposing Pokemon V (after W/R)."""

    def modify_damage_taken(self, calc, carrier):
        if (
            calc.is_attack
            and calc.is_opposing
            and carrier_pokemon(carrier) is calc.target
            and calc.attacker is not None
            and is_pokemon_v(calc.attacker.archetype_id)
            # "This effect can't be applied more than once at a time."
            and not getattr(calc, "_v_guard_applied", False)
        ):
            calc._v_guard_applied = True
            calc.amount = max(0, calc.amount - 30)


# --- provision shapes ------------------------------------------------------
DOUBLE_COLORLESS = [[PokemonTypes.COLORLESS, PokemonTypes.COLORLESS]]


def one_at_a_time(*types) -> list:
    """Provided options for an energy that gives one of `types` at a time.

    Unit Energy (Grass, Fire and Water) and the Blend energies (one of four) read
    as a single clause over several types, so they share this shape.
    """
    return [[t] for t in types]


async def rainbow_on_attach(ctx):
    """Rainbow Energy's rider: put 1 damage counter on the Pokemon it lands on."""
    target = ctx.attached_to
    if target is not None:
        await ctx.place_damage_counters(1, candidates=[target])


class PrismEnergyPassive(Passive):
    """Prism Energy: Colorless by default, every type while on a Basic Pokemon."""

    def modify_energy_provided(self, options, energy, holder, board):
        if holder is not None and is_basic_pokemon(holder):
            return ALL_TYPES_ONE_AT_A_TIME
        return options


class MultiEnergyPassive(Passive):
    """Multi Energy and Luminous Energy: every type until a second Special Energy
    joins it on the same Pokemon, where they provide Colorless instead."""

    def modify_energy_provided(self, options, energy, holder, board):
        if holder is None or board is None:
            return options
        energy_id = getattr(energy, "entity_id", None)
        others = [
            card for card in board.attached_energies(holder)
            if getattr(card, "entity_id", None) != energy_id
            and bool(card.get_attribute(AttrID.IS_SPECIAL_ENERGY))
        ]
        return [[PokemonTypes.COLORLESS.value]] if others else options


# --- attach restrictions ---------------------------------------------------
def pokemon_is_evolved(target) -> bool:
    """Attach restriction: "can be attached only to an Evolved Pokemon"."""
    if target is None:
        return False
    stage = target.get_attribute(AttrID.STAGE)
    return stage is not None and stage != PokemonStage.BASIC.value


def evolved_excluding_ex(target) -> bool:
    """Old Double Rainbow / Scramble wording: Evolved, but not a Pokemon-ex."""
    if not pokemon_is_evolved(target):
        return False
    archetype_id = getattr(target, "archetype_id", None)
    if archetype_id is None:
        return True
    return not any(sub.lower() == "ex" for sub in subtypes_for(archetype_id))


def pokemon_of_type(*types):
    """Attach restriction: "can only be attached to <type> Pokemon"."""
    def predicate(target) -> bool:
        return target is not None and any(_pokemon_has_type(target, t) for t in types)
    return predicate


def pokemon_with_subtype(marker: str):
    """Attach restriction: "can only be attached to a Rapid Strike Pokemon"."""
    def predicate(target) -> bool:
        archetype_id = getattr(target, "archetype_id", None) if target is not None else None
        return archetype_id is not None and marker in subtypes_for(archetype_id)
    return predicate


def pokemon_named_like(fragment: str):
    """Attach restriction for name-based gateways ("Team Rocket's Pokemon")."""
    def predicate(target) -> bool:
        archetype_id = getattr(target, "archetype_id", None) if target is not None else None
        if archetype_id is None:
            return False
        definition = def_for(archetype_id)
        name = getattr(definition, "display_name", "") or ""
        return fragment.lower() in name.lower()
    return predicate


# --- continuous modifiers --------------------------------------------------
def pokemon_has_name_fragment(target, fragment: str) -> bool:
    """True when the carrier's printed name contains `fragment` ("has Dark in
    its name" on the old Darkness Energies)."""
    archetype_id = getattr(target, "archetype_id", None)
    if archetype_id is None:
        return False
    definition = def_for(archetype_id)
    name = (getattr(definition, "display_name", "") or "")
    return fragment.lower() in name.lower()


class DamageBonusPassive(Passive):
    """The carrier's attacks do `amount` more damage to the Active Pokemon.

    Gated either by type (Darkness Metal-Energy wording: "ignore this effect if
    the Pokemon is not Darkness") or by a name fragment ("has Dark in its name").
    """

    def __init__(self, amount: int, pokemon_type=None, name_fragment: str = ""):
        self.amount = amount
        self.pokemon_type = pokemon_type
        self.name_fragment = name_fragment

    def _carrier_qualifies(self, pokemon) -> bool:
        """Both gates read as "Darkness, or has Dark in its name"."""
        if self.pokemon_type is None and not self.name_fragment:
            return True
        by_type = self.pokemon_type is not None and _pokemon_has_type(pokemon, self.pokemon_type)
        by_name = bool(self.name_fragment) and pokemon_has_name_fragment(pokemon, self.name_fragment)
        return by_type or by_name

    def modify_damage_dealt(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        pokemon = carrier_pokemon(carrier)
        if pokemon is not calc.attacker or pokemon is None:
            return
        if self._carrier_qualifies(pokemon):
            calc.amount += self.amount


class DamageReductionPassive(Passive):
    """The carrier takes `amount` less damage from attacks (after W/R)."""

    def __init__(self, amount: int, pokemon_type=None):
        self.amount = amount
        self.pokemon_type = pokemon_type

    def modify_damage_taken(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return
        pokemon = carrier_pokemon(carrier)
        if pokemon is not calc.target:
            return
        if self.pokemon_type is not None and not _pokemon_has_type(pokemon, self.pokemon_type):
            return
        calc.amount = max(0, calc.amount - self.amount)


class MetalEnergyLegacyPassive(DamageReductionPassive):
    """ECARD-era Metal Energy: the carrier takes 10 less, and a non-Metal carrier
    deals 10 less with its own attacks."""

    def __init__(self, amount: int = 10):
        super().__init__(amount)

    def modify_damage_dealt(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return
        pokemon = carrier_pokemon(carrier)
        if pokemon is not calc.attacker or pokemon is None:
            return
        if not _pokemon_has_type(pokemon, PokemonTypes.METAL):
            calc.amount = max(0, calc.amount - self.amount)


class NoWeaknessPassive(Passive):
    """The carrier has no Weakness while this energy is attached."""

    def __init__(self, pokemon_type=None):
        self.pokemon_type = pokemon_type

    def modify_weakness(self, calc, carrier):
        pokemon = carrier_pokemon(carrier)
        if pokemon is not calc.target or pokemon is None:
            return
        if self.pokemon_type is not None and not _pokemon_has_type(pokemon, self.pokemon_type):
            return
        calc.weakness_applies = False


class NoRetreatCostPassive(Passive):
    """The carrier has no Retreat Cost (Magnetic Metal / Hiding Darkness)."""

    def __init__(self, pokemon_type=None):
        self.pokemon_type = pokemon_type

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        holder = carrier_pokemon(carrier)
        if holder is not pokemon:
            return cost
        if self.pokemon_type is not None and not _pokemon_has_type(holder, self.pokemon_type):
            return cost
        return 0


def heal_on_attach(counters: int, cure_conditions: bool = False):
    """On attach from hand: remove `counters` damage counters from the carrier,
    and all special conditions with it (Potion/Full Heal/Heal Energy)."""
    async def effect(ctx):
        target = ctx.attached_to
        if target is None:
            return
        if cure_conditions:
            await ctx.cure_all_conditions(target)
        await ctx.heal(counters * 10, target)
    return effect


def pairs_of(*types) -> list:
    """Two-at-a-time provision over a fixed set of types.

    Aqua Energy: "provides Water and Darkness Energy but provides 2 Energy at a
    time" - any combination of the listed types, including two of one.
    """
    return [[a, b] for index, a in enumerate(types) for b in types[index:]]


async def cure_on_attach(ctx):
    """On attach from hand: the carrier is no longer affected by special
    conditions (Full Heal Energy)."""
    target = ctx.attached_to
    if target is not None:
        await ctx.cure_all_conditions(target)


class EffectShieldPassive(Passive):
    """Opposing attack effects are prevented on the carrier.

    Mist Energy, Wash Water Energy and Rocky Fighting Energy name the protected
    type; the plain wording protects whatever carries the energy.
    """

    def __init__(self, pokemon_type=None):
        self.pokemon_type = pokemon_type

    def blocks_attack_effects(self, target, carrier):
        holder = carrier_pokemon(carrier)
        if holder is None or holder is not target:
            return False
        if self.pokemon_type is not None and not _pokemon_has_type(holder, self.pokemon_type):
            return False
        return True


class SubtypeProvisionPassive(Passive):
    """Every type one at a time while the carrier has a printed subtype.

    Beast Energy's rule is Prism Energy's with "Ultra Beast" in place of "Basic
    Pokemon", so both read from the archetype's subtypes.
    """

    def __init__(self, marker: str):
        self.marker = marker

    def modify_energy_provided(self, options, energy, holder, board):
        archetype_id = getattr(holder, "archetype_id", None) if holder is not None else None
        if archetype_id is not None and self.marker in subtypes_for(archetype_id):
            return ALL_TYPES_ONE_AT_A_TIME
        return options


class SuperBoostEnergyPassive(Passive):
    """Super Boost: every type on a Stage 2, four at a time with three Stage 2 in
    play (the four-at-once form is reported, not offered, when unsupported)."""

    def modify_energy_provided(self, options, energy, holder, board):
        archetype_id = getattr(holder, "archetype_id", None) if holder is not None else None
        if archetype_id is None or "Stage 2" not in subtypes_for(archetype_id):
            return options
        if board is not None:
            owner = getattr(holder, "owning_player_id", None)
            stage_twos = 0
            for pokemon in board.pokemon_in_play(owner) if owner else []:
                other = getattr(pokemon, "archetype_id", None)
                if other is not None and "Stage 2" in subtypes_for(other):
                    stage_twos += 1
            if stage_twos >= 3:
                return [[t, t, t, t] for t in (PokemonTypes.GRASS, PokemonTypes.FIRE,
                                               PokemonTypes.WATER, PokemonTypes.LIGHTNING,
                                               PokemonTypes.PSYCHIC, PokemonTypes.FIGHTING,
                                               PokemonTypes.DARKNESS, PokemonTypes.METAL,
                                               PokemonTypes.FAIRY, PokemonTypes.DRAGON,
                                               PokemonTypes.COLORLESS)]
        return ALL_TYPES_ONE_AT_A_TIME


# --- switching -------------------------------------------------------------
async def warp_on_attach(ctx):
    """Warp Energy: attached to your Active, it may be switched for a Benched
    Pokemon of your choice."""
    active = ctx.my_active()
    if active is None or ctx.attached_to is not active:
        return
    bench = ctx.my_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose your new Active Pokemon")
    if target is not None:
        await ctx.switch_active(ctx.player_id, target)


async def cyclone_on_attach(ctx):
    """Cyclone Energy: the opponent switches their Active for one of their
    Benched Pokemon."""
    active = ctx.my_active()
    if active is None or ctx.attached_to is not active:
        return
    from ptcgo.game.card_effects.support_common import opponent_switches
    await opponent_switches(ctx)


async def jet_on_attach(ctx):
    """Jet Energy: attached to a Benched Pokemon, it becomes your Active."""
    target = ctx.attached_to
    if target is None:
        return
    if any(pokemon is target for pokemon in ctx.my_bench()):
        await ctx.switch_active(ctx.player_id, target)


# --- prize comparison and attached-energy readers ---------------------------
def _prizes_remaining(board, player_id) -> int:
    area = board.find_player_area(player_id, "prizePile") if board is not None else None
    return len(area.children) if area is not None else 0


def _opponent_of(board, player_id):
    others = [pid for pid in getattr(board, "player_ids", []) if pid != player_id]
    return others[0] if others else None


class UpperEnergyPassive(Passive):
    """Upper Energy: two Colorless while you have more prizes left than the
    opponent, and never on a Pokemon LV.X."""

    def modify_energy_provided(self, options, energy, holder, board):
        if holder is None or board is None:
            return options
        archetype_id = getattr(holder, "archetype_id", None)
        if archetype_id is not None and "LV.X" in subtypes_for(archetype_id):
            return options
        owner = getattr(holder, "owning_player_id", None)
        opponent = _opponent_of(board, owner) if owner else None
        if opponent is None:
            return options
        if _prizes_remaining(board, owner) > _prizes_remaining(board, opponent):
            return [[PokemonTypes.COLORLESS, PokemonTypes.COLORLESS]]
        return options


class CrystalEnergyPassive(Passive):
    """Crystal Energy: one Energy of every type among the basic Energy cards
    attached to the carrier, Colorless when there are none."""

    def modify_energy_provided(self, options, energy, holder, board):
        if holder is None or board is None:
            return options
        types = []
        for card in board.attached_energies(holder):
            definition = def_for(getattr(card, "archetype_id", None))
            if definition is None or getattr(definition, "is_special", False):
                continue
            energy_type = getattr(definition, "energy_type", None)
            if energy_type is not None and energy_type not in types:
                types.append(energy_type)
        return [[t] for t in types] if types else [[PokemonTypes.COLORLESS]]


class ScrambleEnergyPassive(Passive):
    """Scramble Energy: three Energy of any types while you have more prizes left
    than the opponent, Colorless otherwise."""

    def __init__(self):
        types = [PokemonTypes.GRASS, PokemonTypes.FIRE, PokemonTypes.WATER,
                 PokemonTypes.LIGHTNING, PokemonTypes.PSYCHIC, PokemonTypes.FIGHTING,
                 PokemonTypes.DARKNESS, PokemonTypes.METAL, PokemonTypes.FAIRY,
                 PokemonTypes.DRAGON, PokemonTypes.COLORLESS]
        self.options = [[types[i], types[j], types[k]]
                        for i in range(len(types))
                        for j in range(i, len(types))
                        for k in range(j, len(types))]

    def modify_energy_provided(self, options, energy, holder, board):
        if holder is None or board is None:
            return options
        owner = getattr(holder, "owning_player_id", None)
        opponent = _opponent_of(board, owner) if owner else None
        if opponent is None:
            return options
        if _prizes_remaining(board, owner) > _prizes_remaining(board, opponent):
            return self.options
        return options


# --- Holon Energies: two riders, each gated on a basic Energy attached -------
def _has_basic_energy(board, holder, energy_type) -> bool:
    if board is None or holder is None:
        return False
    for card in board.attached_energies(holder):
        definition = def_for(getattr(card, "archetype_id", None))
        if definition is None or getattr(definition, "is_special", False):
            continue
        if getattr(definition, "energy_type", None) == energy_type:
            return True
    return False


class HolonEnergyPassive(Passive):
    """Holon Energy FF/GL/WP.

    Each card grants two riders, one while a basic Energy of a given type sits on
    the carrier: `primary` and `secondary` are (type, behaviour) pairs, where the
    behaviour is one of "no_weakness", "ignore_resistance", "no_conditions",
    "ex_reduction", "effect_shield" or "free_retreat".
    """

    def __init__(self, primary, secondary):
        self.primary = primary
        self.secondary = secondary

    def _active(self, behaviour, board, holder) -> bool:
        for energy_type, name in (self.primary, self.secondary):
            if name == behaviour and _has_basic_energy(board, holder, energy_type):
                return True
        return False

    def modify_weakness(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        if holder is calc.target and self._active("no_weakness", getattr(calc, "board", None), holder):
            calc.weakness_applies = False

    def modify_resistance(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        if holder is calc.attacker and self._active("ignore_resistance", getattr(calc, "board", None), holder):
            calc.resistance_applies = False

    def blocks_special_conditions(self, target, condition, carrier):
        holder = carrier_pokemon(carrier)
        return holder is target and self._active("no_conditions", None, holder)

    def modify_damage_taken(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        if holder is not calc.target or not calc.is_attack or not calc.is_opposing:
            return
        if not self._active("ex_reduction", getattr(calc, "board", None), holder):
            return
        attacker = getattr(calc, "attacker", None)
        archetype_id = getattr(attacker, "archetype_id", None) if attacker is not None else None
        if archetype_id is not None and "ex" in [s.lower() for s in subtypes_for(archetype_id)]:
            calc.amount = max(0, calc.amount - 10)

    def blocks_attack_effects(self, target, carrier):
        holder = carrier_pokemon(carrier)
        return holder is target and self._active("effect_shield", None, holder)

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        holder = carrier_pokemon(carrier)
        if holder is pokemon and self._active("free_retreat", board, holder):
            return 0
        return cost


# --- EX-era Darkness / Metal / Holon / δ Energies ---------------------------
# Transplanted verbatim from the upstream card library so its EX-era card
# scripts (which name these classes at construction time) load against this
# engine. Only the import paths changed to `ptcgo.`

def discard_energy_end_of_turn(energy_guid: str):
    """END_OF_TURN granted ability: discard this Energy from the holder."""
    async def effect(ctx):
        pokemon = ctx.source
        if pokemon is None:
            return
        energy = next(
            (c for c in pokemon.children
             if (c.archetype_id or "").lower() == energy_guid.lower()),
            None)
        if energy is not None:
            await ctx.discard_cards([energy])
    return effect


def discard_energy_if_not_evolved(energy_guid: str):
    """BETWEEN_TURNS: if holder is no longer Evolved, discard this Energy."""
    from ptcgo.game.session.effects import is_evolution_pokemon

    async def effect(ctx):
        pokemon = ctx.source
        if pokemon is None:
            return
        if is_evolution_pokemon(pokemon):
            return
        energy = next(
            (c for c in pokemon.children
             if (c.archetype_id or "").lower() == energy_guid.lower()),
            None)
        if energy is not None:
            await ctx.discard_cards([energy])
    return effect


class DarknessEnergyPassive(Passive):
    """+10 damage to Active if holder is Darkness or has Dark in its name."""

    def modify_damage_dealt(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        pokemon = carrier_pokemon(carrier)
        if pokemon is not calc.attacker:
            return
        if _pokemon_has_type(pokemon, PokemonTypes.DARKNESS):
            calc.amount += 10
            return
        d = def_for(pokemon.archetype_id)
        dn = (getattr(d, "display_name", None) or "").lower()
        if "dark" in dn:
            calc.amount += 10


class MetalEnergyPassive(Passive):
    """Holder takes 10 less if it is Metal."""

    def modify_damage_taken(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return
        pokemon = carrier_pokemon(carrier)
        if pokemon is not calc.target:
            return
        if _pokemon_has_type(pokemon, PokemonTypes.METAL):
            calc.amount = max(0, calc.amount - 10)


def _holder_is_ex(pokemon) -> bool:
    return "ex" in subtypes_for(getattr(pokemon, "archetype_id", None) or "")


def _has_basic_energy_of_type(pokemon, ptype: PokemonTypes) -> bool:
    from ptcgo.game.card_effects.trainers import is_basic_energy_card
    from ptcgo.game.card_effects.pokemon import energy_provides_type
    for c in pokemon.children:
        if is_basic_energy_card(c) and energy_provides_type(c, ptype.value):
            return True
    return False


class HolonEnergyFFPassive(Passive):
    """With basic Fire: no Weakness. With basic Fighting: ignore Resistance.
    Ignored on Pokémon-ex."""

    def modify_weakness(self, calc, carrier):
        pokemon = carrier_pokemon(carrier)
        if pokemon is None or pokemon is not calc.target:
            return
        if _holder_is_ex(pokemon):
            return
        if _has_basic_energy_of_type(pokemon, PokemonTypes.FIRE):
            calc.weakness_applies = False

    def modify_resistance(self, calc, carrier):
        # "damage done by that Pokémon's attack isn't affected by Resistance"
        pokemon = carrier_pokemon(carrier)
        if pokemon is None or pokemon is not calc.attacker:
            return
        if _holder_is_ex(pokemon):
            return
        if _has_basic_energy_of_type(pokemon, PokemonTypes.FIGHTING):
            calc.resistance_applies = False


class HolonEnergyGLPassive(Passive):
    """With basic Grass: immune to Special Conditions.
    With basic Lightning: -10 from opposing Pokémon-ex.
    Ignored on Pokémon-ex."""

    def blocks_special_conditions(self, target, condition, carrier):
        holder = carrier_pokemon(carrier)
        if holder is not target or _holder_is_ex(target):
            return False
        return _has_basic_energy_of_type(target, PokemonTypes.GRASS)

    def modify_damage_taken(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return
        pokemon = carrier_pokemon(carrier)
        if pokemon is not calc.target or _holder_is_ex(pokemon):
            return
        if not _has_basic_energy_of_type(pokemon, PokemonTypes.LIGHTNING):
            return
        if calc.attacker is not None and "ex" in subtypes_for(
                calc.attacker.archetype_id or ""):
            calc.amount = max(0, calc.amount - 10)


class HolonEnergyWPPassive(Passive):
    """With basic Water: prevent attack effects (not damage).
    With basic Psychic: retreat cost 0. Ignored on Pokémon-ex."""

    def blocks_attack_effects(self, target, carrier) -> bool:
        holder = carrier_pokemon(carrier)
        if holder is not target or _holder_is_ex(target):
            return False
        return _has_basic_energy_of_type(target, PokemonTypes.WATER)

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        holder = carrier_pokemon(carrier)
        if holder is not pokemon or _holder_is_ex(pokemon):
            return cost
        if _has_basic_energy_of_type(pokemon, PokemonTypes.PSYCHIC):
            return 0
        return cost


class DeltaRainbowEnergyPassive(Passive):
    """δ Rainbow Energy: Colorless normally; every type one-at-a-time while
    attached to a Pokémon that has δ on its card."""

    def modify_energy_provided(self, options, energy, holder, board):
        d = def_for(energy.archetype_id)
        if not isinstance(getattr(d, "passive", None), DeltaRainbowEnergyPassive):
            return options
        if holder is None:
            return [[PokemonTypes.COLORLESS.value]]
        hd = def_for(holder.archetype_id)
        dn = (getattr(hd, "display_name", None) or "")
        sb = " ".join(getattr(hd, "searchable_by", None) or [])
        if "δ" in dn or "δ" in sb or "delta" in dn.lower() or "delta" in sb.lower():
            return options  # keep provides=ALL_TYPES_ONE_AT_A_TIME from card def
        return [[PokemonTypes.COLORLESS.value]]
