"""Continuous (passive) card effects.

A Passive is contributed by a card while it is in play: a Pokemon ability
(Ability(passive=...)), an attached Pokemon Tool, or an attached Special
Energy (both via their CardDefinition's passive=). The engine collects the
active (passive, carrier) pairs each time it computes damage, attack costs,
or max HP, so effects switch on/off purely by board position.
"""

from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional, Set, Tuple

from ptcgo.game.attributes import AttrID, PokemonTypes, TrainerType
from ptcgo.game.data_utils import ABILITIES_BY_ID, Attack, def_for, subtypes_for
from ptcgo.game.models.board import (
    BENCH_SLOT_COUNT,
    BoardEntity,
    BoardState,
    CardEntity,
    PokemonEntity,
)

WEAKNESS_MULTIPLIER = 2
RESISTANCE_REDUCTION = 30

# Areas whose top-level cards keep a temporary passive alive.
_IN_PLAY_AREAS = ("activePokemonArea", "bench", "activeStadium")


@dataclass
class TurnDamageModifier:
    """A turn-scoped attacker-side damage boost (Power Tablet: "+30 damage
    during this turn to your Fusion Strike Pokemon's attacks")."""
    amount: int
    player_id: str
    requires_subtype: Optional[str] = None
    opposing_active_only: bool = True
    # None = this turn only; otherwise the last turn number it still applies.
    expires_after_turn: Optional[int] = None
    # Only while THIS entity attacks (Scyther's next-turn self boost).
    source_entity_id: Optional[str] = None
    # Only while resolving this attack title (Metagross' Fullmetal Impact rider).
    attack_title: Optional[str] = None
    # Arbitrary attacker gate (Ludicolo/Rapidash predicates).
    source_predicate: Optional[Callable[[BoardEntity], bool]] = None


@dataclass
class TargetDamageModifier:
    """A defender-side damage step: "the Defending Pokemon takes N more
    damage from attacks (after applying Weakness and Resistance)" (Mabosstiff,
    Onix, Stunfisk) and the mirror "each of your opponent's Pokemon takes N
    less damage from attacks" (Zamazenta VSTAR's Star Shield). `amount` is
    signed: positive = the defender takes more, negative = less.

    Unlike Passive.modify_damage_taken (a continuous ability that a card
    declares once, keyed to a carrier), these are created by an EFFECT, stack
    with each other, and expire on a turn window. Composition rule: every
    applicable modifier sums into ONE flat delta applied once, after the
    Weakness/Resistance stage and before damage prevention, so +30 and +50 on
    the same Pokemon is +80 and a -100 side-wide reduction plus a -30 tool is
    -130; the running total never falls below 0 damage.

    Scope: `target_entity_id` names one Pokemon (the modifier rides that
    card and is dropped by clear_pokemon_effects when it leaves play or
    evolves); leaving it None instead applies it to every Pokemon the
    `owner_player_id` player has in play, including ones that arrive later.

    Turn window: applied while from_turn <= turn_number <= through_turn, so
    "during your opponent's next turn" is exactly one turn wide rather than
    "from now until then". A target-side modifier is an effect ON the
    defender, so ignore_target_effects (max_mercy_attack / Phoebe) skips it.
    """

    amount: int
    from_turn: int
    through_turn: int
    target_entity_id: Optional[str] = None
    owner_player_id: Optional[str] = None
    attacks_only: bool = True
    # Narrows a player-wide modifier to some of that player's Pokemon
    # ("your Metal Pokemon take 30 less this turn", Iron Defender): takes the
    # candidate Pokemon and returns whether the modifier applies to it.
    target_predicate: Optional[Callable[[Any], bool]] = None
    opposing_only: bool = True
    # The effect that created it, for clear_pokemon_effects bookkeeping.
    source_entity_id: Optional[str] = None
    # Whether an attack's effect created it, so a card that removes "all
    # effects of attacks" (Channeler) can leave the others alone.
    from_attack: bool = False

    def applies_to(self, calc: "DamageCalc") -> bool:
        """Whether this modifier is part of THIS damage calculation."""
        if self.attacks_only and not calc.is_attack:
            return False
        if self.opposing_only and not calc.is_opposing:
            return False
        if calc.ignore_target_effects:
            return False
        if self.target_entity_id is not None:
            if calc.target.entity_id != self.target_entity_id:
                return False
        elif calc.target.owning_player_id != self.owner_player_id:
            return False
        if self.target_predicate is not None \
                and not self.target_predicate(calc.target):
            return False
        turn_state = getattr(calc.board, "turn_state", None)
        turn = getattr(turn_state, "turn_number", self.from_turn)
        return self.from_turn <= turn <= self.through_turn


@dataclass
class EnergyTypeOverride:
    """Effect-created "all Energy attached to this Pokemon provide X Energy
    instead of their usual type" (Steelix, Erika's Oddish) and "treat [X]
    Energy as [Y]" -- a read-time rewrite, so the attached cards never change.

    Composition: every applicable override replaces the card's provision with
    its own types, and when two apply the LAST one registered wins (the most
    recent effect is the one the player just created). Card-bound rewrites
    (Passive.modify_energy_provided) run first and are therefore the base a
    later effect overrides.
    """

    types: List[int]
    holder_entity_id: Optional[str] = None
    player_id: Optional[str] = None
    # Only basic Energy cards ("each basic Grass Energy attached to ...").
    basic_only: bool = False
    # Only cards currently providing exactly Colorless ("Energy cards that
    # provide only Colorless Energy").
    colorless_only: bool = False
    # Only cards whose printed provision is one of these types ("treat Fire
    # Energy as Fighting Energy").
    from_types: Optional[List[int]] = None
    through_turn: Optional[int] = None
    source_entity_id: Optional[str] = None

    def applies(self, energy: BoardEntity, holder: Optional[PokemonEntity],
                board: BoardState) -> bool:
        turn = getattr(getattr(board, "turn_state", None), "turn_number", 0)
        if self.through_turn is not None and turn > self.through_turn:
            return False
        if self.holder_entity_id is not None:
            if holder is None or holder.entity_id != self.holder_entity_id:
                return False
        elif self.player_id is not None:
            if holder is None or holder.owning_player_id != self.player_id:
                return False
        if self.basic_only and not is_basic_energy(energy):
            return False
        printed = [
            list(option)
            for option in (energy.get_attribute(AttrID.ENERGY_INFO) or {}).get("options", [])
        ]
        provided = {t for option in printed for t in option}
        if self.colorless_only and provided != {PokemonTypes.COLORLESS.value}:
            return False
        if self.from_types is not None and not provided.issubset(set(self.from_types)):
            return False
        return True

    def apply(self, options: List[List[int]], energy: BoardEntity,
              holder: Optional[PokemonEntity], board: BoardState) -> List[List[int]]:
        return [list(self.types)] if self.applies(energy, holder, board) else options


@dataclass
class BurnOverride:
    """Effect-created change to what Burn does at Pokemon Checkup: "put 4
    damage counters instead of 2 on your opponent's Burned Pokemon between
    turns" and "instead of flipping a coin for Burned Pokemon".

    Composition: the highest explicit `counters` among applicable overrides
    replaces the base 2, `extra_counters` add on top, and `no_flip` sticks if
    any applicable override sets it. Scope is one Pokemon (target_entity_id) or
    one side (player_id, keyed to the Burned Pokemon's owner).
    """

    counters: Optional[int] = None
    extra_counters: int = 0
    no_flip: bool = False
    target_entity_id: Optional[str] = None
    player_id: Optional[str] = None
    through_turn: Optional[int] = None
    source_entity_id: Optional[str] = None

    def applies(self, pokemon: PokemonEntity, board: BoardState) -> bool:
        turn = getattr(getattr(board, "turn_state", None), "turn_number", 0)
        if self.through_turn is not None and turn > self.through_turn:
            return False
        if self.target_entity_id is not None:
            return pokemon.entity_id == self.target_entity_id
        return self.player_id is None or pokemon.owning_player_id == self.player_id


def is_basic_energy(energy: BoardEntity) -> bool:
    """Whether an attached card is a basic Energy card (not a Special Energy)."""
    return not bool(energy.get_attribute(AttrID.IS_SPECIAL_ENERGY))


def burn_checkup_counters(board: BoardState, pokemon: PokemonEntity) -> int:
    """Damage counters a Burned Pokemon takes at checkup: base 2, replaced by
    an effect override, then shifted by burn passives and extra overrides."""
    counters = 2
    overrides = [o for o in (getattr(board, "burn_overrides", None) or [])
                 if o.applies(pokemon, board)]
    explicit = [o.counters for o in overrides if o.counters is not None]
    if explicit:
        counters = max(explicit)
    for passive, carrier in active_passives(board):
        counters = passive.modify_burn_counters(counters, pokemon, carrier)
    counters += sum(o.extra_counters for o in overrides)
    return max(0, counters)


def burn_recovery_suppressed(board: BoardState, pokemon: PokemonEntity) -> bool:
    """"Instead of flipping a coin for Burned Pokemon": True when an override
    removes the checkup flip, so the Burned Pokemon cannot recover."""
    return any(o.no_flip and o.applies(pokemon, board)
               for o in (getattr(board, "burn_overrides", None) or []))


@dataclass
class TempPassive:
    """An effect-granted passive with a lifetime. expires_after_turn None =
    until the carrier leaves the Active spot / play (clear_pokemon_effects)."""
    passive: "Passive"
    carrier_entity_id: str
    expires_after_turn: Optional[int] = None
    from_attack: bool = False


class DamageCalc:
    """One damage computation, mutated in stages by the passive hooks."""

    def __init__(
        self,
        board: BoardState,
        attacker: Optional[BoardEntity],
        target: PokemonEntity,
        base: int,
        is_attack: bool = True,
        apply_modifiers: bool = True,
        ignore_target_effects: bool = False,
        attack_title: Optional[str] = None,
    ):
        self.board = board
        self.attacker = attacker
        self.target = target
        self.base = base
        self.amount = base
        # True for attack damage; False for ability/effect damage.
        self.is_attack = is_attack
        # Weakness/Resistance stage runs only versus the defending Active.
        self.apply_modifiers = apply_modifiers
        # Title of the attack being resolved (matches TurnDamageModifier riders).
        self.attack_title = attack_title
        self.weakness_applies = True
        self.weakness_multiplier = WEAKNESS_MULTIPLIER
        # Rewritable by modify_weakness hooks (Spiritomb/UnownVSTAR overrides).
        self.weak_types: List[Any] = list(
            target.get_attribute(AttrID.WEAKNESS_TYPES) or []
        )
        self.resistance_applies = True
        self.weakness_hit = False
        self.resistance_hit = False
        self.prevented = False
        # Max Miracle-style: skip passives riding the DEFENDING Pokemon in the
        # taken/prevention stages (attacker-side and third-party still run).
        self.ignore_target_effects = ignore_target_effects
        # Scratch set for non-stacking effects (e.g. Lesson in Zeal) to mark
        # themselves applied and skip on a later pass within the same calc.
        self.applied_once: Set[str] = set()

    @property
    def to_bench(self) -> bool:
        """Whether the target sits on its owner's Bench."""
        parent = self.target.parent
        return bool(parent) and parent.get_attribute(AttrID.NAME) == "bench"

    @property
    def to_active(self) -> bool:
        """Whether the target sits in its owner's Active spot."""
        parent = self.target.parent
        return bool(parent) and parent.get_attribute(AttrID.NAME) == "activePokemonArea"

    @property
    def is_opposing(self) -> bool:
        """Whether attacker and target belong to different players."""
        return (
            self.attacker is not None
            and self.attacker.owning_player_id != self.target.owning_player_id
        )


class Passive:
    """Override only the hooks a card's continuous effect needs.

    `carrier` is the entity contributing the passive: the Pokemon whose
    ability it is, or the attached tool/energy card (carrier_pokemon gives
    the Pokemon an attachment rides on).
    """

    # Same-key passives count once in effective_max_hp (Abomasnow stacks).
    stacking_key: Optional[str] = None

    # Optional awaitable damage stage: async (ctx, calc, target, carrier) ->
    # Optional[int], consulted in ctx.deal_damage AFTER compute_damage and
    # BEFORE the HP write (None = unchanged, else the new dealt amount).
    # Flip-to-prevent (Infiltrator) and KO-survive (Guts) live here; may queue
    # coin flips via ctx so they choreograph inside the attack bracket.
    damage_interceptor: Optional[Any] = None

    # Optional awaitable post-attack stage: async (ctx, carrier) -> None, run
    # by resolve_attack AFTER knockouts/deferred actions resolve (end-of-turn
    # riders like Blunder Policy); queued messages flush as their own brackets.
    attack_followup: Optional[Any] = None

    def modify_damage_dealt(self, calc: DamageCalc, carrier: BoardEntity):
        """Attacker-side "does more/less damage" step (runs before W/R)."""

    def modify_weakness(self, calc: DamageCalc, carrier: BoardEntity):
        """May clear calc.weakness_applies (e.g. "... have no Weakness"), or
        rewrite calc.weak_types / calc.weakness_multiplier."""

    def modify_resistance(self, calc: DamageCalc, carrier: BoardEntity):
        """May clear calc.resistance_applies ("... has no Resistance")."""

    def modify_damage_taken(self, calc: DamageCalc, carrier: BoardEntity):
        """Defender-side "takes less damage" step (runs after W/R)."""

    def prevents_damage(self, calc: DamageCalc, carrier: BoardEntity) -> bool:
        """True to prevent the hit entirely (calc.amount becomes 0)."""
        return False

    def modify_attack_cost(
        self,
        cost: Dict[str, int],
        pokemon: PokemonEntity,
        carrier: BoardEntity,
        board: BoardState,
    ) -> Dict[str, int]:
        """Returns the (possibly reduced) cost dict, client-name keyed."""
        return cost

    def max_hp_bonus(self, pokemon: PokemonEntity, carrier: BoardEntity,
                     board: Optional[BoardState] = None) -> int:
        """Extra max HP granted to `pokemon` (e.g. Heat Fire Energy's +20).
        `board` lets a bonus whose number depends on the game state read it
        (Pangoro's per-taken-Prize HP); a constant bonus may ignore it."""
        return 0

    def modify_retreat_cost(
        self, cost: int, pokemon: PokemonEntity, carrier: BoardEntity,
        board: BoardState,
    ) -> int:
        """Returns the (possibly reduced) retreat cost (Air Balloon's -2);
        `board` lets stadium-gated hooks read global state (Thwackey)."""
        return cost

    def blocks_bench_damage(self, calc: "DamageCalc", carrier: BoardEntity) -> bool:
        """True to prevent attack damage to BENCHED Pokemon (Mountain Ring,
        Sky Pillar); only consulted when the target sits on a Bench."""
        return False

    def blocks_attack_effects(self, target: PokemonEntity, carrier: BoardEntity,
                              attacker: Optional[PokemonEntity] = None) -> bool:
        """True to shield `target` from opponents' attack EFFECTS (not damage).
        `attacker` is the Pokemon whose attack is resolving, so a shield whose
        printed scope names its attackers ("by attacks from Pokemon-EX") can
        see the same Pokemon the damage path sees."""
        return False

    def blocks_abilities(self, pokemon: PokemonEntity, carrier: BoardEntity) -> bool:
        """True to turn off `pokemon`'s Abilities (Path to the Peak style)."""
        return False

    def blocks_retreat(self, pokemon: PokemonEntity, carrier: BoardEntity) -> bool:
        """True to forbid `pokemon` from retreating (Octolock, Flygon)."""
        return False

    def attacks_despite_conditions(self, pokemon: PokemonEntity, carrier: BoardEntity) -> bool:
        """True to let `pokemon` attack even while Asleep/Paralyzed (Windup Arm)."""
        return False

    def permits_turn_continue_after_mega(
        self, pokemon: PokemonEntity, carrier: BoardEntity
    ) -> bool:
        """True to keep the turn going when `pokemon` becomes a Mega Evolution
        (Spirit Link: "your turn does not end if the Pokemon this card is
        attached to becomes M <name> ex")."""
        return False

    def permits_retreat_while_immobilized(
        self, pokemon: PokemonEntity, carrier: BoardEntity
    ) -> bool:
        """True to let `pokemon` retreat even while Asleep or Paralyzed
        (Escape Board). Retreat only: attacking stays blocked."""
        return False

    def blocks_special_conditions(
        self, target: PokemonEntity, condition: Any, carrier: BoardEntity
    ) -> bool:
        """True to shield `target` from having `condition` applied to it."""
        return False

    def prevents_healing(self, target: PokemonEntity, carrier: BoardEntity) -> bool:
        """True to prevent healing damage from `target` (Mimikyu SWSH3)."""
        return False

    def knockout_destination(
        self, pokemon: PokemonEntity, carrier: BoardEntity, from_attack: bool = False
    ) -> Optional[str]:
        """Area name replacing "discard" for a knocked-out Pokemon (e.g. "lostZone",
        "hand"). `from_attack` is True when attack damage caused the knockout, which
        Rescue Scarf's wording requires."""
        return None

    def modify_prizes_for_knockout(
        self, pokemon: PokemonEntity, ctx: Any, count: int, carrier: BoardEntity
    ) -> int:
        """Prize count the opponent takes for knocking out `pokemon` (Komala);
        evaluated BEFORE the stack moves, so board/conditions still count."""
        return count

    def prize_destination(
        self, pokemon: PokemonEntity, ctx: Any, carrier: BoardEntity
    ) -> Optional[str]:
        """Area name replacing "hand" for the prizes taken for this knockout
        ("discard" = Billowing Smoke, "lostZone" = Barbaracle)."""
        return None

    def modify_energy_provided(
        self, options: List[List[int]], energy: BoardEntity,
        holder: Optional[PokemonEntity], board: BoardState,
    ) -> List[List[int]]:
        """Rewrites an energy's provided-type options (Charizard PGO doubling)."""
        return options

    def modify_subtypes(
        self, subtypes: List[str], pokemon: BoardEntity, carrier: BoardEntity
    ) -> List[str]:
        """"This Pokemon counts as a [subtype]": rewrites the subtype list a
        card counts against (Single Strike, Fusion Strike, Stage 1 ...). Runs
        after the printed subtypes, before any effect-created override."""
        return subtypes

    def modify_pokemon_types(
        self, types: List[Any], pokemon: BoardEntity, carrier: BoardEntity
    ) -> List[Any]:
        """Rewrites `pokemon`'s live type list (Kecleon's Chromashift)."""
        return types

    def blocks_energy_removal(
        self, energy: BoardEntity, mover_player_id: str, carrier: BoardEntity
    ) -> bool:
        """True to keep an attached Energy from being moved to hand/deck/
        discard by `mover_player_id`'s Item/Supporter effect (Brazen Tail)."""
        return False

    def suppresses_special_energy(self, energy: BoardEntity, carrier: BoardEntity) -> bool:
        """True to neutralize a Special Energy (Temple of Sinnoh): it loses
        its passive and provides only Colorless."""
        return False

    def suppresses_tool(self, tool: BoardEntity, carrier: BoardEntity) -> bool:
        """True to neutralize an attached Pokemon Tool's passive hooks
        (Tool Jammer); evaluated on the unfiltered set like ability locks."""
        return False

    def granted_attacks(
        self, board: BoardState, pokemon: PokemonEntity, carrier: BoardEntity
    ) -> List[Any]:
        """Extra Attack definitions `pokemon` may use (Ditto's Sudden
        Transformation, Memory Capsule); costs/locks still apply normally."""
        return []

    def blocks_trainer_play(
        self, card: BoardEntity, player_id: str, carrier: BoardEntity,
        board: Optional["BoardState"] = None
    ) -> bool:
        """True to forbid `player_id` playing `card` from hand (Vileplume)."""
        return False

    def may_evolve_early(self, pokemon: PokemonEntity, carrier: BoardEntity) -> bool:
        """True to exempt `pokemon` from the just-played/first-turn evolution
        gates (Caterpie's Adaptive Evolution)."""
        return False

    def blocks_evolution(
        self, player_id: str, target: PokemonEntity, carrier: BoardEntity
    ) -> bool:
        """True to forbid `player_id` evolving `target` at all (Dracovish)."""
        return False

    def modify_burn_counters(
        self, counters: int, pokemon: PokemonEntity, carrier: BoardEntity
    ) -> int:
        """Damage counters the Burn checkup tick places (default 2)."""
        return counters

    def blocks_burn_recovery(self, pokemon: PokemonEntity, carrier: BoardEntity) -> bool:
        """True to skip the Burn recovery flip entirely (stays Burned)."""
        return False

    def modify_heal_amount(self, pokemon: PokemonEntity, carrier: BoardEntity,
                           amount: int) -> int:
        """Healing done TO `pokemon`, this passive's view (Sylveon: heals of 30
        or more become 50); the card rewrites the number."""
        return amount

    def energy_discard_destination(self, energy: BoardEntity,
                                   pokemon: Optional[PokemonEntity],
                                   discarder_id: Optional[str],
                                   carrier: BoardEntity) -> Optional[str]:
        """Where an Energy discarded from `pokemon` by `discarder_id` goes
        instead of the discard pile ("hand" for Ecogym); None keeps it."""
        return None

    def discard_to_hand_blocked(self, card: BoardEntity,
                                carrier: BoardEntity) -> bool:
        """True to keep a card in its discard pile instead of returning it to
        its owner's hand (Pokemon Tower)."""
        return False

    def trainer_play_cost(self, card: BoardEntity, player_id: str,
                          carrier: BoardEntity) -> int:
        """Extra OTHER hand cards `player_id` must discard to play `card`
        (No Removal Gym charges 2 for an Energy Removal); 0 = no opinion."""
        return 0

    def voids_stadium_play(self, carrier: BoardEntity) -> bool:
        """True to discard any Stadium played while this one is in play, and
        this one with it ("the new Stadium card has no effect", Chaotic Swell)."""
        return False

    def trainer_play_flips(self, card: BoardEntity, player_id: str,
                           carrier: BoardEntity) -> bool:
        """True to coin-flip a Trainer play before it resolves; tails makes the
        card do nothing (Chaos Gym)."""
        return False

    def retreat_flips(self, pokemon: PokemonEntity,
                      carrier: BoardEntity) -> bool:
        """True to coin-flip a retreat attempt; tails refuses it for the turn
        (Mirage Stadium)."""
        return False

    def wr_applies_to_bench(self, calc: "DamageCalc", carrier: BoardEntity) -> bool:
        """True to apply Weakness/Resistance to a BENCHED defender from this
        passive's side of the board (Wide Lens)."""
        return False

    def modify_resistance_amount(self, amount: int, calc: "DamageCalc",
                                 carrier: BoardEntity) -> int:
        """The Resistance reduction after this passive's say (Resistance Gym:
        every Resistance is 20 smaller). `amount` is the printed reduction."""
        return amount

    def blocks_attack(self, pokemon: PokemonEntity, carrier: BoardEntity) -> bool:
        """True to forbid `pokemon` attacking at all (Blizzard Town: Pokemon
        with 40 HP or less remaining can't attack)."""
        return False

    def keeps_condition_on_evolve(self, condition: str, pokemon: PokemonEntity,
                                  carrier: BoardEntity) -> bool:
        """True to keep `condition` when the Pokemon evolves or devolves (Sea of
        Nothingness, Dizzying Valley)."""
        return False

    def poison_checkup_counters(self, pokemon: PokemonEntity, carrier: BoardEntity,
                                counters: int) -> int:
        """Damage counters `pokemon` takes from Poison at Checkup, this
        passive's view; the card raises it (Virbank City Gym: 2 more)."""
        return counters

    def tool_capacity(self, pokemon: PokemonEntity, carrier: BoardEntity) -> int:
        """Pokemon Tools `pokemon` may hold (GarbodorVMAX 2); highest wins."""
        return 1

    def bench_capacity(self, player_id: str, carrier: BoardEntity) -> Optional[int]:
        """Bench size override for `player_id` (Collapsed Stadium 4); None =
        no opinion, the smallest override wins."""
        return None

    def bench_capacity_raise(self, player_id: str, carrier: BoardEntity,
                             board: Optional[BoardState] = None) -> Optional[int]:
        """Bench size this passive RAISES `player_id` to (Sky Field: 8); None =
        no opinion. Caps still win: the tighter of the two applies."""
        return None

    def bench_trim_area(self, player_id: str, carrier: BoardEntity) -> Optional[str]:
        """Where a stack removed by the bench-shrink ruling goes ("hand" for
        Narrow Gym); None keeps the default discard."""
        return None

    def sleep_recovery_coins(self, pokemon: PokemonEntity,
                             carrier: BoardEntity) -> Optional[int]:
        """Coins an Asleep `pokemon` flips to wake at Checkup (Slumbering
        Forest: 2, and one tails keeps it Asleep); None = no opinion."""
        return None

    def attack_keeps_turn(self, attacker: PokemonEntity, ability: Any,
                          ctx: Any, carrier: BoardEntity) -> bool:
        """True to keep the turn going after `attacker`'s attack resolved
        (Fluffy Barrage); runs after knockouts resolve, so KO evidence rides
        ctx.knockouts_resolved, not ctx.knockouts."""
        return False

    def blocks_ability_effects(self, target: PokemonEntity, carrier: BoardEntity) -> bool:
        """True to shield `target` from opponents' Ability effects (Corviknight VMAX)."""
        return False

    def blocks_discard(self, card: BoardEntity, carrier: BoardEntity) -> bool:
        """True to keep `card` from being discarded by an opponent's effect."""
        return False

    async def on_attack_resolved(self, ctx, attacker, defender, carrier) -> None:
        """After an attack resolved, for a Stadium rider keyed on the attacker
        (Vermilion City Gym: "whenever a player attacks with a Pokemon with
        Lt. Surge in its name, he or she may flip a coin"). Extra damage lands
        as its own step, which is what "after applying Weakness and Resistance"
        means for the +10 half."""
        return None

    async def on_active_switched(self, ctx, player_id: str,
                                 outgoing: PokemonEntity,
                                 incoming: PokemonEntity,
                                 outgoing_conditions: List[str],
                                 via_trainer: bool,
                                 carrier: BoardEntity) -> None:
        """Runs after `outgoing` leaves the Active spot for `incoming`.

        `outgoing_conditions` is the condition list captured before the swap
        cleared them; `via_trainer` is whether a Trainer's effect caused it
        (Dust Island)."""
        return None

    async def on_retreat(self, ctx, pokemon: PokemonEntity,
                         carrier: BoardEntity) -> None:
        """Runs after `pokemon` finishes retreating, this passive's carrier
        still attached (Balloon Berry: "when the Pokemon this card is attached
        to retreats, discard this card")."""
        return None

    def blocks_play(self, player_id: str, card: BoardEntity,
                    carrier: BoardEntity, board: Optional["BoardState"] = None
                    ) -> bool:
        """True to forbid `player_id` playing `card` from hand while this
        passive is on (Gothitelle: "your opponent can't play any Item cards
        from his or her hand"). Continuous, so it is asked at offer time
        rather than recorded as a turn-scoped lock."""
        return False

    def blocks_trainer_effects(
        self, affected_player_id: str, trainer_card: BoardEntity,
        trainer_type: Any, carrier: BoardEntity,
        affected_entity: Optional[BoardEntity] = None,
        board: Optional["BoardState"] = None,
    ) -> bool:
        """True to shield `affected_player_id`'s side from an opposing trainer
        card's effects (Dew Guard); trainer_type is the TrainerType value.
        affected_entity is the primitive's direct object (None for
        player-level effects like draws/hand shuffles)."""
        return False

    def replace_supporter_effect(
        self, card: BoardEntity, player_id: str, carrier: BoardEntity
    ) -> Optional[Any]:
        """Replacement effect coroutine for `player_id`'s Supporter `card`
        (Shifty Substitution); None = no replacement."""
        return None

    def taxes_energy_attach(
        self, attaching_player_id: str, energy: BoardEntity,
        target: PokemonEntity, carrier: BoardEntity,
    ) -> bool:
        """True to coin-flip `attaching_player_id`'s manual energy attach
        (Slimy Room): tails discards the energy instead of attaching."""
        return False

    def retreat_cost_destination(
        self, pokemon: PokemonEntity, energy: BoardEntity, carrier: BoardEntity
    ) -> Optional[str]:
        """Player-area name replacing "discard" for `energy` paid for
        `pokemon`'s retreat (Skaters' Park sends basic Energy to "hand")."""
        return None

    def counters_on_active_to_bench(
        self, pokemon: PokemonEntity, carrier: BoardEntity
    ) -> int:
        """Damage counters put on an Active that moved to its owner's Bench
        during that owner's turn (Spikemuth)."""
        return 0

    def heal_on_evolve(
        self, evolved: PokemonEntity, pre_evolution: BoardEntity,
        player_id: str, carrier: BoardEntity,
    ) -> int:
        """Damage healed from a Pokemon `player_id` just evolved from hand
        (Wyndon Stadium)."""
        return 0

    def offers_attack_coin_reroll(self, player_id: str, carrier: BoardEntity) -> bool:
        """True to let `player_id` re-flip an attack's coins once during
        their turn (Glimwood Tangle)."""
        return False


def carrier_pokemon(carrier: BoardEntity) -> Optional[PokemonEntity]:
    """The in-play Pokemon a passive rides: the carrier itself, or the
    top-level Pokemon its attachment stack hangs under."""
    entity = carrier
    while entity is not None:
        parent = entity.parent
        if isinstance(entity, PokemonEntity) and not isinstance(parent, CardEntity):
            return entity
        entity = parent if isinstance(parent, CardEntity) else None
    return None


def _collect_passives(board: BoardState) -> List[Tuple[Passive, BoardEntity, bool]]:
    """All (passive, carrier, is_ability) triples currently switched on by
    board position, before ability locks are applied. is_ability is True only
    for passives contributed by a Pokemon's own PIE_ABILITIES entry."""
    triples: List[Tuple[Passive, BoardEntity, bool]] = []
    for player_id in board.player_ids:
        for pokemon in board.pokemon_in_play(player_id):
            # Card-level PokemonCardDef(passive=): rules text that is not an
            # Ability, so ability locks never switch it off.
            card_passive = getattr(def_for(pokemon.archetype_id), "passive", None)
            if card_passive is not None:
                triples.append((card_passive, pokemon, False))
            for entry in pokemon.get_attribute(AttrID.PIE_ABILITIES) or []:
                if not isinstance(entry, dict):
                    continue
                ability = ABILITIES_BY_ID.get(entry.get("abilityID"))
                if ability is not None and ability.passive is not None:
                    # A Tool-granted ability's passive rides the tool, not the
                    # Pokemon, so Path to the Peak can't switch it off.
                    triples.append((ability.passive, pokemon, not ability.is_granted))
            for attachment in _descendants(pokemon):
                if isinstance(attachment, PokemonEntity):
                    continue  # tucked pre-evolutions contribute nothing
                definition = def_for(attachment.archetype_id)
                passive = getattr(definition, "passive", None)
                if passive is not None:
                    triples.append((passive, attachment, False))
    stadium_area = board.find_global_area("activeStadium")
    for stadium in (stadium_area.children if stadium_area else []):
        face = stadium_face(board, stadium)
        passive = face.get("passive")
        if passive is not None:
            triples.append((passive, stadium, False))
    # Effect-granted temporary passives; dead carriers are silently skipped.
    for temp in getattr(board, "temporary_passives", None) or []:
        carrier = board.get_entity(temp.carrier_entity_id)
        if carrier is None or not _carrier_in_play(carrier):
            continue
        triples.append((temp.passive, carrier, False))
    return triples


def _carrier_in_play(entity: BoardEntity) -> bool:
    """Whether an entity (or the stack it is attached under) sits in play."""
    node = entity
    while isinstance(getattr(node, "parent", None), CardEntity):
        node = node.parent
    parent = getattr(node, "parent", None)
    return parent is not None \
        and parent.get_attribute(AttrID.NAME) in _IN_PLAY_AREAS


_POKE_POWER_TYPES = ("poké-power", "poke-power", "pokémon power",
                     "pokemon power")


def has_poke_power(pokemon: PokemonEntity) -> bool:
    """Whether `pokemon` prints at least one Poke-Power.

    The vintage type is not in the scripts (no card sets `AbilityTypes`, and
    every ability defaults to POKE_ABILITY), so it is read from the set JSON
    beside the script, by ability title."""
    from ptcgo.game.data_utils import def_for
    from ptcgo.game.scripts.cards import printed_ability_type

    definition = def_for(getattr(pokemon, "archetype_id", None) or "")
    for ability in getattr(definition, "abilities", []) or []:
        printed = printed_ability_type(definition, getattr(ability, "title", "") or "")
        if printed.strip().lower() in _POKE_POWER_TYPES:
            return True
    return False


def poke_powers_locked(board: BoardState) -> bool:
    """Whether a card has switched every Poke-Power off (Goop Gas Attack).

    The flag is cleared by `TurnState.begin_turn` once its window passes."""
    return bool(getattr(board, "poke_power_lock_through", 0))


async def fire_active_switched(board: BoardState, ctx, player_id: str,
                                outgoing: PokemonEntity,
                                incoming: PokemonEntity,
                                outgoing_conditions: List[str],
                                via_trainer: bool) -> None:
    """Runs every passive's `on_active_switched` after an Active swap."""
    for passive, carrier in active_passives(board):
        await passive.on_active_switched(
            ctx, player_id, outgoing, incoming, outgoing_conditions,
            via_trainer, carrier)


def ability_locked(board: BoardState, pokemon: PokemonEntity) -> bool:
    """Whether a passive (Path to the Peak) is disabling `pokemon`'s Abilities.

    Evaluated on the UNFILTERED set: a lock contributed by a Pokemon ability
    is never itself disabled by another lock (Garbotoxin-style recursion is
    out of scope -- Path to the Peak rides a Stadium so this is safe).
    """
    if poke_powers_locked(board) and has_poke_power(pokemon):
        return True
    return any(p.blocks_abilities(pokemon, c) for p, c, _ in _collect_passives(board))


def _suppressed_special_energy(
    triples: List[Tuple[Passive, BoardEntity, bool]], entity: BoardEntity
) -> bool:
    """Whether `entity` is a Special Energy neutralized by a suppression
    passive (evaluated on the UNFILTERED set, like ability locks)."""
    if not entity.get_attribute(AttrID.IS_SPECIAL_ENERGY):
        return False
    return any(p.suppresses_special_energy(entity, c) for p, c, _ in triples)


def _suppressed_tool(
    triples: List[Tuple[Passive, BoardEntity, bool]], entity: BoardEntity
) -> bool:
    """Whether `entity` is an attached Pokemon Tool neutralized by a
    suppression passive (Tool Jammer), evaluated on the UNFILTERED set."""
    if entity.get_attribute(AttrID.TRAINER_TYPE) != TrainerType.POKEMON_TOOL.value:
        return False
    return any(p.suppresses_tool(entity, c) for p, c, _ in triples)


def active_passives(board: BoardState) -> List[Tuple[Passive, BoardEntity]]:
    """All (passive, carrier) pairs currently switched on by board position.

    Ability passives count only for top-level in-play Pokemon (a tucked
    pre-evolution's ability is off); tool/energy/stadium passives count
    anywhere in an in-play stack. Ability-contributed passives on a Pokemon
    whose own Abilities are locked (Path to the Peak) are excluded, as are
    passives riding a suppressed Special Energy (Temple of Sinnoh).
    """
    triples = _collect_passives(board)

    def blocked(pokemon: PokemonEntity) -> bool:
        return any(p.blocks_abilities(pokemon, c) for p, c, _ in triples)

    return [(p, c) for p, c, is_ability in triples
            if not (is_ability and blocked(c))
            and not _suppressed_special_energy(triples, c)
            and not _suppressed_tool(triples, c)]


def tool_suppressed(board: BoardState, tool: BoardEntity) -> bool:
    """Whether an attached Tool is neutralized (Tool Jammer): gates its
    granted_abilities in PIE_ABILITIES, not just its passive hooks."""
    return _suppressed_tool(_collect_passives(board), tool)


def granted_extra_attacks(board: BoardState, pokemon: PokemonEntity) -> List[Any]:
    """All passive-granted extra attacks for `pokemon`, deduped by ability_id."""
    out: List[Any] = []
    seen = set()
    for passive, carrier in active_passives(board):
        for attack in passive.granted_attacks(board, pokemon, carrier) or []:
            if attack.ability_id and attack.ability_id not in seen:
                seen.add(attack.ability_id)
                out.append(attack)
    return out


def attacks_of(entity: BoardEntity) -> List[Any]:
    """The attacks printed on another entity, as registered Attack objects.

    The lookup behind every "this Pokemon can use the attacks of X" card:
    "the attacks of any Pokemon in play" (Mew-EX's Versatile, Mew ex's
    Memory Helix), "the attacks of any Basic Pokemon in your discard pile"
    (Marshadow-GX's Shadow Hunt), "the attacks of its previous evolutions"
    (previous_evolution_attacks). The returned objects are the live
    definitions, so their ability_id still resolves the offered panel row
    back to the printed attack and its effect; `entity` itself is never
    filtered out here, the caller decides the source set.
    """
    return [
        ability
        for ability in (getattr(def_for(entity.archetype_id), "abilities", None) or [])
        if isinstance(ability, Attack)
    ]


def previous_evolution_attacks(pokemon: PokemonEntity) -> List[Any]:
    """The attacks of the Pokemon tucked underneath `pokemon` (its previous
    Evolutions): "this Pokemon can use the attacks of its previous
    evolutions" -- Memory Capsule, and the Stadium/Ability variants."""
    out: List[Any] = []
    for child in pokemon.children:
        if isinstance(child, PokemonEntity):
            out.extend(attacks_of(child))
    return out


def ability_granting_card(board: BoardState, pokemon: PokemonEntity,
                          ability: Any) -> Optional[BoardEntity]:
    """The card that grants `ability` to `pokemon`: the attached Tool that
    prints it (a Technical-Machine-style tool's attack, Forest Seal Stone's
    Star Alchemy, Memory Capsule's borrowed attacks), else the Pokemon itself
    when the ability is printed on it.

    Card text served: "Discard this card after using this attack" and any tool
    effect that has to act on its own card rather than on the holder -- the
    card scripts read it as ctx.ability_source.
    """
    if ability is None:
        return pokemon
    ability_id = getattr(ability, "ability_id", None)
    for child in pokemon.children:
        definition = def_for(child.archetype_id)
        for granted in getattr(definition, "granted_abilities", None) or []:
            if granted is ability:
                return child
            if ability_id and getattr(granted, "ability_id", None) == ability_id:
                return child
    return pokemon


def _descendants(entity: BoardEntity) -> List[BoardEntity]:
    out: List[BoardEntity] = []
    for child in entity.children:
        out.append(child)
        out.extend(_descendants(child))
    return out


def compute_damage(
    board: BoardState,
    attacker: Optional[BoardEntity],
    target: PokemonEntity,
    base: int,
    is_attack: bool = True,
    apply_modifiers: bool = True,
    ignore_target_effects: bool = False,
    ignore_weakness: bool = False,
    ignore_resistance: bool = False,
    attack_title: Optional[str] = None,
) -> DamageCalc:
    """Runs the full damage pipeline: dealt-modifiers, W/R, taken-modifiers,
    prevention. Returns the finished DamageCalc.

    ignore_weakness (Cramorant's Spit Innocently) skips the Weakness stage but
    keeps Resistance -- distinct from apply_modifiers, which gates both;
    ignore_resistance (Gallade V's Buster Swing) is the exact mirror.
    """
    calc = DamageCalc(board, attacker, target, base,
                      is_attack=is_attack, apply_modifiers=apply_modifiers,
                      ignore_target_effects=ignore_target_effects,
                      attack_title=attack_title)
    if ignore_weakness:
        calc.weakness_applies = False
    if ignore_resistance:
        calc.resistance_applies = False
    passives = active_passives(board)

    if calc.is_attack:
        for passive, carrier in passives:
            passive.modify_damage_dealt(calc, carrier)
        calc.amount = max(0, calc.amount)
        turn_state = getattr(board, "turn_state", None)
        for mod in (turn_state.damage_modifiers if turn_state else []):
            if attacker is None or attacker.owning_player_id != mod.player_id:
                continue
            if mod.requires_subtype \
                    and not has_subtype(board, attacker, mod.requires_subtype):
                continue
            if mod.source_entity_id and attacker.entity_id != mod.source_entity_id:
                continue
            if mod.attack_title and calc.attack_title != mod.attack_title:
                continue
            if mod.source_predicate is not None and not mod.source_predicate(attacker):
                continue
            if mod.opposing_active_only and not (calc.is_opposing and calc.to_active):
                continue
            calc.amount += mod.amount
        calc.amount = max(0, calc.amount)

    applies_wr = calc.apply_modifiers
    if not applies_wr and calc.is_attack and calc.to_bench and attacker is not None:
        # Wide Lens: the holder's attacks are affected by W/R on the Bench too.
        applies_wr = any(passive.wr_applies_to_bench(calc, carrier)
                         for passive, carrier in passives)
    if applies_wr and attacker is not None:
        for passive, carrier in passives:
            passive.modify_weakness(calc, carrier)
            passive.modify_resistance(calc, carrier)
        attacker_types = list(attacker.get_attribute(AttrID.POKEMON_TYPES) or [])
        for passive, carrier in passives:
            attacker_types = passive.modify_pokemon_types(attacker_types, attacker, carrier)
        if calc.weakness_applies and any(t in calc.weak_types for t in attacker_types):
            calc.weakness_hit = True
            calc.amount *= calc.weakness_multiplier
        # A single resistance is stored as a bare value; a delta or a rewrite
        # may leave a list, so accept both rather than silently miss.
        resist_types = target.get_attribute(AttrID.RESISTANCE_TYPES) or []
        if not isinstance(resist_types, (list, tuple, set)):
            resist_types = [resist_types]
        if calc.resistance_applies and any(t in attacker_types for t in resist_types):
            calc.resistance_hit = True
            reduction = RESISTANCE_REDUCTION
            for passive, carrier in passives:
                reduction = passive.modify_resistance_amount(reduction, calc, carrier)
            calc.amount = max(0, calc.amount - max(0, reduction))

    # Defender-side modifiers ("takes N more/less damage from attacks (after
    # applying Weakness and Resistance)"): one flat step, summed, before the
    # continuous taken-damage passives and before prevention.
    turn_state = getattr(board, "turn_state", None)
    target_mods = getattr(turn_state, "target_damage_modifiers", None) or ()
    if target_mods:
        delta = sum(m.amount for m in target_mods if m.applies_to(calc))
        if delta:
            calc.amount = max(0, calc.amount + delta)

    for passive, carrier in passives:
        if calc.ignore_target_effects and carrier_pokemon(carrier) is calc.target:
            continue
        passive.modify_damage_taken(calc, carrier)
    calc.amount = max(0, calc.amount)

    for passive, carrier in passives:
        if calc.ignore_target_effects and carrier_pokemon(carrier) is calc.target:
            continue
        if calc.to_bench and passive.blocks_bench_damage(calc, carrier):
            calc.prevented = True
            calc.amount = 0
            break
        if passive.prevents_damage(calc, carrier):
            calc.prevented = True
            calc.amount = 0
            break
    return calc


def effective_attack_cost(
    board: BoardState, pokemon: PokemonEntity, cost: Dict[str, int]
) -> Dict[str, int]:
    """An attack's cost after cost-modifying passives (e.g. Excited Heart)."""
    for passive, carrier in active_passives(board):
        cost = passive.modify_attack_cost(dict(cost), pokemon, carrier, board)
    return cost


def effective_retreat_cost(board: BoardState, pokemon: PokemonEntity) -> int:
    """A Pokemon's retreat cost after cost-modifying passives (Air Balloon's -2)."""
    cost = int(pokemon.get_attribute(AttrID.RETREAT_COST) or 0)
    for passive, carrier in active_passives(board):
        cost = passive.modify_retreat_cost(cost, pokemon, carrier, board)
    return max(0, cost)


def effective_max_hp(board: BoardState, pokemon: PokemonEntity) -> int:
    """Printed max HP plus every max-HP bonus riding the Pokemon's stack;
    passives sharing a stacking_key count once (Abomasnow)."""
    printed = pokemon.attribute_originals.get(
        AttrID.HP.value, pokemon.get_attribute(AttrID.HP, 0)
    )
    bonus = 0
    seen_keys: Set[str] = set()
    for passive, carrier in active_passives(board):
        key = passive.stacking_key
        if key is not None and key in seen_keys:
            continue
        gained = passive.max_hp_bonus(pokemon, carrier, board)
        if gained and key is not None:
            seen_keys.add(key)
        bonus += gained
    return printed + bonus


def attack_effects_blocked(board: BoardState, target: PokemonEntity,
                           attacker: Optional[PokemonEntity] = None) -> bool:
    """Whether a passive shields `target` from opposing attack effects.
    `attacker` scopes the answer for a shield that only answers some attackers."""
    return any(
        passive.blocks_attack_effects(target, carrier, attacker)
        for passive, carrier in active_passives(board)
    )


def retreat_blocked(board: BoardState, pokemon: PokemonEntity) -> bool:
    """Whether a passive forbids `pokemon` from retreating."""
    return any(
        passive.blocks_retreat(pokemon, carrier)
        for passive, carrier in active_passives(board)
    )


def can_retreat_despite_conditions(board: BoardState, player_id: str) -> bool:
    """Whether the player's Active may retreat while Asleep or Paralyzed.

    Only retreat: `can_attack_despite_conditions` is the attack-side twin, and
    a carrier that grants one does not grant the other."""
    active = board.active_pokemon(player_id)
    if active is None:
        return False
    return any(
        passive.permits_retreat_while_immobilized(active, carrier)
        for passive, carrier in active_passives(board)
    )


def can_attack_despite_conditions(board: BoardState, pokemon: PokemonEntity) -> bool:
    """Whether a passive lets `pokemon` attack while Asleep/Paralyzed."""
    return any(
        passive.attacks_despite_conditions(pokemon, carrier)
        for passive, carrier in active_passives(board)
    )


def conditions_blocked(board: BoardState, target: PokemonEntity, condition: Any) -> bool:
    """Whether a passive shields `target` from the given Special Condition."""
    return any(
        passive.blocks_special_conditions(target, condition, carrier)
        for passive, carrier in active_passives(board)
    )


def healing_blocked(board: BoardState, target: PokemonEntity) -> bool:
    """Whether a passive prevents healing damage from `target`."""
    return any(
        passive.prevents_healing(target, carrier)
        for passive, carrier in active_passives(board)
    )


def ability_effects_blocked(board: BoardState, target: PokemonEntity) -> bool:
    """Whether a passive shields `target` from opposing Ability effects."""
    return any(
        passive.blocks_ability_effects(target, carrier)
        for passive, carrier in active_passives(board)
    )


def trainer_play_blocked(board: BoardState, player_id: str, card: BoardEntity) -> bool:
    """Whether a continuous passive forbids playing `card` from hand."""
    return any(
        passive.blocks_trainer_play(card, player_id, carrier, board)
        for passive, carrier in active_passives(board)
    )


def discard_blocked(board: BoardState, card: BoardEntity) -> bool:
    """Whether a passive protects `card` from an opponent-caused discard."""
    return any(
        passive.blocks_discard(card, carrier)
        for passive, carrier in active_passives(board)
    )


def modified_heal_amount(board: BoardState, pokemon: PokemonEntity,
                         amount: int) -> int:
    """How much a heal of `amount` on `pokemon` actually heals."""
    for passive, carrier in active_passives(board):
        amount = passive.modify_heal_amount(pokemon, carrier, amount)
    return amount


def energy_discard_destination(board: BoardState, energy: BoardEntity,
                               pokemon: Optional[PokemonEntity] = None,
                               discarder_id: Optional[str] = None
                               ) -> Optional[str]:
    """The area a discarded Energy goes to instead of the discard pile."""
    for passive, carrier in active_passives(board):
        destination = passive.energy_discard_destination(
            energy, pokemon, discarder_id, carrier)
        if destination:
            return destination
    return None


def discard_to_hand_blocked(board: BoardState, card: BoardEntity) -> bool:
    """Whether a Stadium keeps `card` in the discard pile instead of its hand.

    Only a card already in a discard pile is covered; a card coming from the
    deck, the prizes or play is not."""
    source = getattr(card, "parent", None)
    if source is None or source.get_attribute(AttrID.NAME) != "discard":
        return False
    return any(passive.discard_to_hand_blocked(card, carrier)
               for passive, carrier in active_passives(board))


def trainer_play_flips(board: BoardState, card: BoardEntity, player_id: str) -> bool:
    """Whether a Trainer play must be coin-flipped first (Chaos Gym)."""
    return any(passive.trainer_play_flips(card, player_id, carrier)
               for passive, carrier in active_passives(board))


def retreat_flips(board: BoardState, pokemon: PokemonEntity) -> bool:
    """Whether a retreat attempt must be coin-flipped first (Mirage Stadium)."""
    return any(passive.retreat_flips(pokemon, carrier)
               for passive, carrier in active_passives(board))


def attacks_blocked(board: BoardState, pokemon: PokemonEntity) -> bool:
    """Whether a passive forbids `pokemon` from attacking (Blizzard Town)."""
    return any(passive.blocks_attack(pokemon, carrier)
               for passive, carrier in active_passives(board))


def conditions_kept_on_evolve(board: BoardState, pokemon: PokemonEntity,
                              conditions: List[str]) -> List[str]:
    """Which of `conditions` survive an evolution/devolution of `pokemon`."""
    if not conditions:
        return []
    kept = []
    for condition in conditions:
        if any(passive.keeps_condition_on_evolve(condition, pokemon, carrier)
               for passive, carrier in active_passives(board)):
            kept.append(condition)
    return kept


def poison_checkup_counters(board: BoardState, pokemon: PokemonEntity,
                            counters: int = 1) -> int:
    """Poison tick size after every passive's say (Virbank City Gym)."""
    for passive, carrier in active_passives(board):
        counters = passive.poison_checkup_counters(pokemon, carrier, counters)
    return counters


def stadium_face(board: BoardState, stadium: BoardEntity) -> Dict[str, Any]:
    """The Stadium's effective face: {passive, ability, on_leave_play}.

    A facing Stadium (Chaos Tower, Parallel City) stores its chosen label on
    the board; a plain one reads the definition's own slots."""
    definition = def_for(stadium.archetype_id)
    if definition is None:
        return {}
    faces = getattr(definition, "faces", None)
    if faces:
        chosen = (getattr(board, "stadium_facings", None) or {}).get(stadium.entity_id)
        return faces.get(chosen) or next(iter(faces.values()))
    return {
        "passive": getattr(definition, "passive", None),
        "ability": getattr(definition, "ability", None),
        "on_leave_play": getattr(definition, "on_leave_play", None),
    }


def plays_blocked(board: BoardState, player_id: str, card: BoardEntity) -> bool:
    """Whether a continuous passive forbids `player_id` playing `card` from
    hand (the always-on twin of TurnState.play_locked's scoped locks)."""
    return any(
        passive.blocks_play(player_id, card, carrier, board=board)
        for passive, carrier in active_passives(board)
    )


def trainer_effects_blocked(board: BoardState, affected_player_id: str,
                            trainer_card: BoardEntity,
                            affected_entity: Optional[BoardEntity] = None) -> bool:
    """Whether a passive shields `affected_player_id` from `trainer_card`'s
    effects (Dew Guard); callers scope this to cross-player effects."""
    trainer_type = trainer_card.get_attribute(AttrID.TRAINER_TYPE)
    return any(
        passive.blocks_trainer_effects(
            affected_player_id, trainer_card, trainer_type, carrier,
            affected_entity=affected_entity, board=board)
        for passive, carrier in active_passives(board)
    )


def supporter_effect_replacement(board: BoardState, card: BoardEntity,
                                 player_id: str) -> Optional[Any]:
    """First replacement coroutine a passive offers for this Supporter play
    (Shifty Substitution), or None."""
    for passive, carrier in active_passives(board):
        replacement = passive.replace_supporter_effect(card, player_id, carrier)
        if replacement is not None:
            return replacement
    return None


def active_to_bench_counters(board: BoardState, pokemon: PokemonEntity) -> int:
    """Damage counters for an Active that moved to its owner's Bench during
    the owner's turn (Spikemuth); callers gate on whose turn it is."""
    return sum(
        passive.counters_on_active_to_bench(pokemon, carrier)
        for passive, carrier in active_passives(board)
    )


def evolve_heal_amount(board: BoardState, evolved: PokemonEntity,
                       pre_evolution: BoardEntity, player_id: str) -> int:
    """Damage healed from a Pokemon just evolved from hand (Wyndon Stadium)."""
    return sum(
        passive.heal_on_evolve(evolved, pre_evolution, player_id, carrier)
        for passive, carrier in active_passives(board)
    )


def attack_coin_reroll_offered(board: BoardState, player_id: str) -> bool:
    """Whether a passive lets `player_id` re-flip attack coins (Glimwood Tangle)."""
    return any(
        passive.offers_attack_coin_reroll(player_id, carrier)
        for passive, carrier in active_passives(board)
    )


def energy_attach_taxer(board: BoardState, attaching_player_id: str,
                        energy: BoardEntity, target: PokemonEntity) -> Optional[BoardEntity]:
    """The carrier taxing this manual energy attach (Slimy Room), or None."""
    for passive, carrier in active_passives(board):
        if passive.taxes_energy_attach(attaching_player_id, energy, target, carrier):
            return carrier
    return None


def retreat_energy_destination(board: BoardState, pokemon: PokemonEntity,
                               energy: BoardEntity) -> Optional[str]:
    """First non-None area a passive redirects a retreat-cost energy to
    (Skaters' Park), or None for the normal discard."""
    for passive, carrier in active_passives(board):
        dest = passive.retreat_cost_destination(pokemon, energy, carrier)
        if dest is not None:
            return dest
    return None


def evolution_blocked(board: BoardState, player_id: str, target: PokemonEntity) -> bool:
    """Whether a passive forbids `player_id` evolving `target` (Dracovish)."""
    return any(
        passive.blocks_evolution(player_id, target, carrier)
        for passive, carrier in active_passives(board)
    )


def can_evolve_early(board: BoardState, pokemon: PokemonEntity) -> bool:
    """Whether a passive exempts `pokemon` from the evolution turn gates."""
    return any(
        passive.may_evolve_early(pokemon, carrier)
        for passive, carrier in active_passives(board)
    )


def burn_recovery_blocked(board: BoardState, pokemon: PokemonEntity) -> bool:
    """Whether a passive skips the Burn recovery flip for `pokemon`."""
    return any(
        passive.blocks_burn_recovery(pokemon, carrier)
        for passive, carrier in active_passives(board)
    )


def special_energy_suppressed(board: BoardState, energy: BoardEntity) -> bool:
    """Whether `energy` is a Special Energy neutralized by a passive."""
    return _suppressed_special_energy(_collect_passives(board), energy)


def effective_pokemon_types(board: BoardState, pokemon: BoardEntity) -> List[Any]:
    """A Pokemon's live type list after type-rewriting passives (Chromashift)."""
    types = list(pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])
    for passive, carrier in active_passives(board):
        types = passive.modify_pokemon_types(types, pokemon, carrier)
    return types


def energy_removal_blocked(board: BoardState, mover_player_id: str,
                           card: BoardEntity) -> bool:
    """Whether a passive keeps this attached Energy from being moved to
    hand/deck/discard by `mover_player_id`'s trainer effect (Brazen Tail)."""
    return any(
        passive.blocks_energy_removal(card, mover_player_id, carrier)
        for passive, carrier in active_passives(board)
    )


def effective_subtypes(board: Optional[BoardState],
                       pokemon: PokemonEntity) -> List[str]:
    """A Pokemon's live subtypes: its printed ones, then type-rewriting
    passives, then effect-created overrides (ctx.add_subtype) that have not
    expired. Order is printed-first and deduped, so a caller that only cares
    about membership can use `has_subtype`."""
    subtypes = list(subtypes_for(pokemon.archetype_id))
    if board is None:
        return subtypes
    for passive, carrier in active_passives(board):
        subtypes = passive.modify_subtypes(subtypes, pokemon, carrier)
    turn = getattr(getattr(board, "turn_state", None), "turn_number", 0)
    for subtype, through_turn in (getattr(board, "subtype_overrides", None) or {}).get(
            pokemon.entity_id, []):
        if through_turn is not None and turn > through_turn:
            continue
        if subtype not in subtypes:
            subtypes.append(subtype)
    return subtypes


def has_subtype(board: Optional[BoardState], pokemon: PokemonEntity,
                subtype: str) -> bool:
    """Whether `pokemon` counts as `subtype` right now (printed or granted)."""
    return subtype in effective_subtypes(board, pokemon)


def effective_stage(board: Optional[BoardState],
                    pokemon: PokemonEntity) -> Any:
    """A Pokemon's live stage: an effect-created override ("treat this Pokemon
    as a Stage 1") when one is in force, else its printed stage."""
    if board is not None:
        entry = (getattr(board, "stage_overrides", None) or {}).get(pokemon.entity_id)
        turn = getattr(getattr(board, "turn_state", None), "turn_number", 0)
        if entry is not None:
            stage, through_turn = entry
            if through_turn is None or turn <= through_turn:
                return stage
    return pokemon.get_attribute(AttrID.STAGE)


def energy_provided_options(board: Optional[BoardState], energy: BoardEntity) -> List[List[int]]:
    """An energy card's provided-type options after suppression (a suppressed
    Special Energy provides only Colorless) and modify_energy_provided hooks."""
    info = energy.get_attribute(AttrID.ENERGY_INFO) or {}
    options = [list(option) for option in info.get("options", [])]
    if board is None:
        return options
    if special_energy_suppressed(board, energy):
        options = [[PokemonTypes.COLORLESS.value]]
    holder = carrier_pokemon(energy)
    for passive, carrier in active_passives(board):
        options = passive.modify_energy_provided(options, energy, holder, board)
    for rewrite in (getattr(board, "energy_type_overrides", None) or []):
        options = rewrite.apply(options, energy, holder, board)
    return options


def trainer_play_cost(board: BoardState, card: BoardEntity, player_id: str) -> int:
    """Total other-hand-cards cost of playing `card`: its printed `play_cost`
    plus whatever a passive in play charges (No Removal Gym)."""
    printed = int(getattr(def_for(getattr(card, "archetype_id", "") or ""),
                          "play_cost", 0) or 0)
    extra = 0
    for passive, carrier in active_passives(board):
        extra += passive.trainer_play_cost(card, player_id, carrier)
    return printed + extra


def stadium_play_voided(board: BoardState) -> bool:
    """True when a Stadium played from hand is discarded on arrival instead of
    replacing the one in play (Chaotic Swell)."""
    return any(passive.voids_stadium_play(carrier)
               for passive, carrier in active_passives(board))


def bench_trim_area(board: BoardState, player_id: str) -> str:
    """Where an over-capacity bench stack goes: "hand" when the capacity
    passive in force asks for it (Narrow Gym), else "discard" (Collapsed
    Stadium's ruling)."""
    for passive, carrier in active_passives(board):
        if passive.bench_capacity(player_id, carrier) is None:
            continue
        area = passive.bench_trim_area(player_id, carrier)
        if area:
            return area
    return "discard"


def sleep_recovery_coins(board: BoardState, pokemon: PokemonEntity,
                         default: int = 1) -> int:
    """Coins `pokemon` flips to wake from Asleep; the highest passive wins, so
    a Thumping Snore rider (already in `default`) is never lowered."""
    coins = default
    for passive, carrier in active_passives(board):
        value = passive.sleep_recovery_coins(pokemon, carrier)
        if value is not None:
            coins = max(coins, value)
    return coins


def effective_bench_capacity(board: BoardState, player_id: str) -> int:
    """Bench size for `player_id`: a game-long override when one was set
    (bench_limit_overrides, "for the rest of the game your Bench is 6"), then
    capacity passives, smallest winning (Collapsed Stadium caps an Eternatus
    board at 4). An override only replaces the printed default -- a passive
    that caps lower still caps, so the two compose as "the tighter wins"."""
    overrides = getattr(board, "bench_limit_overrides", None) or {}
    base = overrides.get(player_id, BENCH_SLOT_COUNT)
    raises = [
        v for passive, carrier in active_passives(board)
        for v in [passive.bench_capacity_raise(player_id, carrier, board)]
        if v is not None
    ]
    if raises:
        base = max(base, max(raises))
    values = [
        v for passive, carrier in active_passives(board)
        for v in [passive.bench_capacity(player_id, carrier)] if v is not None
    ]
    return max(1, min(values)) if values else base


def tool_slots_free(board: Optional[BoardState], pokemon: PokemonEntity) -> int:
    """Open Pokemon Tool slots on `pokemon` (default capacity 1; the highest
    tool_capacity passive wins)."""
    capacity = 1
    if board is not None:
        for passive, carrier in active_passives(board):
            capacity = max(capacity, passive.tool_capacity(pokemon, carrier))
    attached = sum(
        1 for child in pokemon.children
        if child.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.POKEMON_TOOL.value
    )
    return capacity - attached
