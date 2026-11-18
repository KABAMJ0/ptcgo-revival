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
