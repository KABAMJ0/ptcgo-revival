"""Reusable Passive factories and temporary-shield effect factories.

GROUP A builds configured Passive instances for Ability(passive=)/Tool/
Stadium/Energy definitions. GROUP B builds complete attack effects (printed
damage first, then the rider) around expiring temp passives; the apply_*
helpers are the damage-free riders for composition inside bespoke effects.

Predicate conventions: `protects` is 'carrier' | 'team' | callable(target,
carrier). Side/holder gates are built into each factory, so refining preds
(attacker_pred / target_pred / holder_pred) take just the entity; block-hook
preds (no_retreat / ability_lock / healing_block / retreat_free) take
(target, carrier).
"""

from typing import Any, Callable, Optional

from ptcgo.game.attributes import (
    AttrID, CLIENT_SPECIAL_CONDITION_NAMES, PokemonStage, PokemonTypes,
    TrainerType,
)
from ptcgo.game.data_utils import def_for
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.session.passives import (
    EnergyTypeOverride,
    Passive,
    TurnDamageModifier,
    attacks_of,
    carrier_pokemon,
    effective_max_hp,
    effective_pokemon_types,
    previous_evolution_attacks,
)


# ----------------------------------------------------------------------
# Shared predicate plumbing
# ----------------------------------------------------------------------

def _protects_pred(protects) -> Callable[[Any, Any], bool]:
    """Resolves the 'carrier' | 'team' | 'each' | callable(target, carrier)
    tri-form; 'each' covers every Pokemon on both sides (Legendary Trench)."""
    if callable(protects):
        return protects
    if protects == "each":
        return lambda target, carrier: True
    if protects == "team":
        return lambda target, carrier: (
            target.owning_player_id == carrier.owning_player_id
        )
    if protects in (None, "carrier"):
        return lambda target, carrier: carrier_pokemon(carrier) is target
    raise ValueError(f"protects must be 'carrier', 'team' or a callable: {protects!r}")


def is_in_active_spot(pokemon) -> bool:
    """Whether a top-level Pokemon sits in its owner's Active spot."""
    parent = getattr(pokemon, "parent", None)
    return bool(parent) and parent.get_attribute(AttrID.NAME) == "activePokemonArea"


def opposing_pokemon(target, carrier) -> bool:
    """(target, carrier) pred: target belongs to the other player."""
    return target.owning_player_id != carrier.owning_player_id


def opposing_active(target, carrier) -> bool:
    """(target, carrier) pred: target is the opposing Active Pokemon."""
    return opposing_pokemon(target, carrier) and is_in_active_spot(target)


def unafflicted(board, player_id, pokemon) -> bool:
    """Board-level Ability.condition: the Pokemon carries no Special Condition
    ("This power can't be used if <name> is affected by a Special Condition")."""
    return not (pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])


def empty_hand(board, player_id, pokemon) -> bool:
    """Board-level Ability.condition: the player has no cards in hand ("you
    can't use this power if you have any cards in your hand")."""
    hand = board.find_player_area(player_id, "hand")
    return hand is not None and not hand.children


_PLAY_KIND_TESTS = {
    "item": lambda card: card.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.ITEM.value,
    "supporter": lambda card: card.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.SUPPORTER.value,
    "stadium": lambda card: card.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.STADIUM.value,
    "tool": lambda card: card.get_attribute(AttrID.TRAINER_TYPE) in (
        TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value),
    "special_energy": lambda card: bool(card.get_attribute(AttrID.IS_SPECIAL_ENERGY)),
    "trainer": lambda card: card.get_attribute(AttrID.TRAINER_TYPE) is not None,
}


class PlayLockPassive(Passive):
    """A continuous lock on the opponent's hand: "As long as this Pokemon is
    your Active Pokemon, your opponent can't play any Item cards from his or
    her hand" (Gothitelle, Vileplume, Kabutops).

    `matches` is the kind test over a hand card; the two hooks are the two
    places the offer consults a passive -- blocks_trainer_play for Trainer
    cards, blocks_play for Energy.
    """

    def __init__(self, matches, while_active=True, opponents_only=True,
                 condition=None):
        self.matches = matches
        self.while_active = while_active
        self.opponents_only = opponents_only
        self.condition = condition

    def _locks(self, player_id, card, carrier, board) -> bool:
        if not self.matches(card):
            return False
        if self.opponents_only and player_id == carrier.owning_player_id:
            return False
        if self.while_active and not is_in_active_spot(carrier_pokemon(carrier)):
            return False
        if self.condition is not None and not self.condition(board, player_id, carrier):
            return False
        return True

    def blocks_trainer_play(self, card, player_id, carrier, board=None) -> bool:
        return self._locks(player_id, card, carrier, board)

    def blocks_play(self, player_id, card, carrier, board=None) -> bool:
        return self._locks(player_id, card, carrier, board)


def fewer_pokemon_in_play(board, player_id, carrier) -> bool:
    """Condition for `play_lock_passive`: the carrier's owner has fewer Pokemon
    in play than the opponent (Omastar's Fossil Bind).

    `player_id` is the player the lock would stop, so when the carrier carries
    no owner id the locked player is the one who is not the owner."""
    if board is None:
        return False
    owner = carrier.owning_player_id
    ids = list(getattr(board, "player_ids", None) or [])
    if owner is not None:
        opponent = next((pid for pid in ids if pid != owner), None)
        mine = owner
    else:
        opponent, mine = player_id, next((pid for pid in ids if pid != player_id), None)
    if mine is None or opponent is None:
        return False
    return len(board.pokemon_in_play(mine)) < len(board.pokemon_in_play(opponent))


def play_lock_passive(*kinds, excluding=None, while_active: bool = True,
                      opponents_only: bool = True, condition=None) -> Passive:
    """"Your opponent can't play any <kinds> cards from his or her hand" while
    this Pokemon is Active (Gothitelle, Vileplume, Kabutops, Trevenant).

    `kinds` are "item", "supporter", "stadium", "tool", "trainer",
    "special_energy" or "all"; `excluding` drops one, which spells the
    "Trainer cards (except for Supporter cards)" wording."""
    selected = set(kinds)
    if "all" in selected:
        selected |= set(_PLAY_KIND_TESTS)
    if excluding:
        selected.discard(excluding)
    if not selected:
        raise ValueError(f"play_lock_passive: no kinds in {kinds!r}")
    tests = [_PLAY_KIND_TESTS[kind] for kind in selected]

    def matches(card) -> bool:
        return any(test(card) for test in tests)

    matches.plays = tuple(sorted(selected))
    return PlayLockPassive(matches, while_active=while_active,
                           opponents_only=opponents_only, condition=condition)


# ======================================================================
# GROUP A -- continuous Passive factories
# ======================================================================

class TakesLessPassive(Passive):
    """Protected Pokemon take N less damage from opposing attacks (after W/R).

    `attacker_side="team"` additionally requires the attacker to belong to the
    passive's own side, which is the Stadium wording "attacks from this
    down-arrow player's Grass, Fire or Water Pokemon do 20 less"
    (Parallel City); the plain form is every opposing attacker."""

    def __init__(self, amount, protects="carrier", attacker_pred=None,
                 stack_key=None, attacker_side=None):
        self.amount = amount
        self.protects = _protects_pred(protects)
        self.attacker_pred = attacker_pred
        self.stack_key = stack_key
        self.attacker_side = attacker_side

    def modify_damage_taken(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return
        if not self.protects(calc.target, carrier):
            return
        if self.attacker_pred is not None and (
                calc.attacker is None or not self.attacker_pred(calc.attacker)):
            return
        if self.attacker_side == "team" and (
                calc.attacker is None
                or calc.attacker.owning_player_id != carrier.owning_player_id):
            return
        if self.stack_key:
            if self.stack_key in calc.applied_once:
                return
            calc.applied_once.add(self.stack_key)
        calc.amount = max(0, calc.amount - self.amount)


def takes_less_passive(amount, protects="carrier", attacker_pred=None,
                       stack_key=None, attacker_side=None) -> Passive:
    """"Takes N less damage from attacks" (Lesson in Zeal shape); a stack_key
    dedups multiple copies within one damage calc. `attacker_side="team"` is
    the Stadium shape, where the cut applies only to the passive's own side's
    attackers (Parallel City), and `protects="each"` covers both boards."""
    return TakesLessPassive(amount, protects, attacker_pred, stack_key,
                            attacker_side)


def pokemon_of_types(*types) -> Callable[[Any], bool]:
    """Predicate: a Pokemon (or card) has at least one of `types`."""
    wanted = set(types)

    def pred(any_card, *_rest) -> bool:
        # Tolerant of the (pokemon, board) call shape some hooks use.
        current = set(any_card.get_attribute(AttrID.POKEMON_TYPES) or [])
        return bool(current & wanted)

    return pred


def team_of_types(*types, protects="team") -> Callable[[Any, Any], bool]:
    """(target, carrier) pred for `protects`: the target is on the passive's own
    side AND is one of `types` ("this down-arrow player's Metal Pokemon")."""
    typed = pokemon_of_types(*types)
    side = _protects_pred(protects)

    def pred(target, carrier) -> bool:
        return side(target, carrier) and typed(target)

    return pred


class TeamDamageBoostPassive(Passive):
    """Matching friendly attackers' attacks do +N (before W/R)."""

    def __init__(self, amount, attacker_pred=None, target_pred=None,
                 once_key=None, to_active_only=True):
        self.amount = amount
        self.attacker_pred = attacker_pred
        self.target_pred = target_pred
        self.once_key = once_key
        self.to_active_only = to_active_only

    def modify_damage_dealt(self, calc, carrier):
        attacker = calc.attacker
        if not (calc.is_attack and calc.is_opposing and attacker is not None):
            return
        if attacker.owning_player_id != carrier.owning_player_id:
            return
        if self.attacker_pred is not None and not self.attacker_pred(attacker):
            return
        # A callable amount is the wording whose number depends on the board at
        # resolution ("40 instead of 10 if the attacking player has more Prize
        # cards remaining" -- Martial Arts Dojo).
        amount = self.amount(calc, carrier) if callable(self.amount) else self.amount
        if not amount:
            return
        if self.to_active_only and not calc.to_active:
            return
        if self.target_pred is not None and not self.target_pred(calc.target):
            return
        if self.once_key:
            if self.once_key in calc.applied_once:
                return
            calc.applied_once.add(self.once_key)
        calc.amount += amount


class ReducesOwnAttacksPassive(Passive):
    """The carrier's own attacks do N less ("during your opponent's next turn,
    any damage done by attacks from the Defending Pokemon is reduced by N")."""

    def __init__(self, amount):
        self.amount = amount

    def modify_damage_dealt(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return
        if calc.attacker is not carrier_pokemon(carrier):
            return
        calc.amount = max(0, calc.amount - self.amount)


def weakens_own_attacks_passive(amount: int) -> Passive:
    return ReducesOwnAttacksPassive(amount)


def team_damage_boost_passive(amount, attacker_pred=None, target_pred=None,
                              once_key=None, to_active_only=True) -> Passive:
    """"Your <matching> Pokemon's attacks do +N to the opponent's Active"
    (pass to_active_only=False for boosts with no Active clause)."""
    return TeamDamageBoostPassive(amount, attacker_pred, target_pred,
                                  once_key, to_active_only)


class PredicatePreventionPassive(Passive):
    """prevents_damage generic: pred(calc, carrier) decides the block."""

    def __init__(self, pred, attacks_only=True, any_side=False):
        self.pred = pred
        self.attacks_only = attacks_only
        self.any_side = any_side

    def prevents_damage(self, calc, carrier):
        if self.attacks_only and not (
                calc.is_attack and (self.any_side or calc.is_opposing)):
            return False
        return bool(self.pred(calc, carrier))


def prevent_damage_when(pred, attacks_only=True, any_side=False) -> Passive:
    """Full damage prevention whenever pred(calc, carrier) holds; by default
    only versus opposing attacks (Wave Veil discipline). any_side lifts the
    "opposing" half so attacks from either player are covered."""
    return PredicatePreventionPassive(pred, attacks_only, any_side)


class AttackShieldPassive(Passive):
    """A continuous shield against opposing attacks, spoken in two halves.

    "Prevent all damage done to this Pokemon by attacks from <X>" is the
    DAMAGE half; "prevent all effects of attacks ... done to this Pokemon" is
    the EFFECT half. A card prints one or both: "including damage" is both,
    "(damage is not an effect)" is the effect half alone, and a bare "prevent
    all damage" is the damage half alone.

    `attacker_pred(attacker)` is the printed scope, and it gates BOTH halves so
    the shield answers the same attackers in each ("by attacks from
    Pokemon-EX", "from a Pokemon that has any Special Energy attached").
    None means every opposing attacker, which is the plain wording.
    """

    def __init__(self, attacker_pred=None, protects="carrier", damage=True,
                 effects_too=False):
        self.attacker_pred = attacker_pred
        self.protects = _protects_pred(protects)
        self.damage = damage
        self.effects_too = effects_too

    def _covers(self, target, carrier, attacker) -> bool:
        if not self.protects(target, carrier):
            return False
        if self.attacker_pred is None:
            return True
        return attacker is not None and bool(self.attacker_pred(attacker))

    def prevents_damage(self, calc, carrier):
        return bool(self.damage and calc.is_attack and calc.is_opposing
                    and self._covers(calc.target, carrier, calc.attacker))

    def blocks_attack_effects(self, target, carrier, attacker=None):
        return bool(self.effects_too and self._covers(target, carrier, attacker))


def attack_shield_from(attacker_pred=None, protects="carrier", damage=True,
                       effects_too=False) -> Passive:
    """"Prevent all [effects of] attacks[, including damage], done to <protects>
    by attacks from <attacker_pred>". `damage=False` is the effects-only
    wording; `effects_too=True` adds the effect half, which the damage path
    can never express on its own."""
    return AttackShieldPassive(attacker_pred, protects, damage, effects_too)


def damage_shield_from(pred, protects="carrier") -> Passive:
    """"Prevent all damage done to this Pokemon by attacks from <X>": full
    prevention gated on the ATTACKER, not the target. `pred` takes the
    attacking Pokemon -- `attacker_is_gx_or_ex()`, `attacker_of_types("Darkness")`,
    `attacker_has_ability()`, or any callable of your own."""
    return attack_shield_from(pred, protects)


class TypedDamageBoostPassive(Passive):
    """The holder's attacks do +N to opposing targets matching a type/pred."""

    def __init__(self, type_or_pred, amount, to_active_only=True):
        if callable(type_or_pred):
            self.target_match = type_or_pred
        else:
            type_value = getattr(type_or_pred, "value", type_or_pred)
            self.target_match = lambda target: type_value in (
                target.get_attribute(AttrID.POKEMON_TYPES) or []
            )
        self.amount = amount
        self.to_active_only = to_active_only

    def modify_damage_dealt(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return
        if carrier_pokemon(carrier) is not calc.attacker:
            return
        if self.to_active_only and not calc.to_active:
            return
        if self.target_match(calc.target):
            calc.amount += self.amount


def typed_damage_boost_tool(type_or_pred, amount, to_active_only=True) -> Passive:
    """Gloves shape: the holder's attacks do +N versus opposing Active
    targets of the given PokemonTypes (or matching target_pred(target))."""
    return TypedDamageBoostPassive(type_or_pred, amount, to_active_only)


class HpBonusPassive(Passive):
    """The holder gets +N max HP (Cape of Toughness shape)."""

    def __init__(self, amount, holder_pred=None):
        self.amount = amount
        self.holder_pred = holder_pred

    def max_hp_bonus(self, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return 0
        if self.holder_pred is not None and not self.holder_pred(pokemon):
            return 0
        return self.amount


def hp_bonus_tool(amount, holder_pred=None) -> Passive:
    """+N max HP on the holder; holder_pred gates eligibility (e.g. Basic
    only for Cape of Toughness). Engine keeps damage-taken constant."""
    return HpBonusPassive(amount, holder_pred)


class RetreatDiscountPassive(Passive):
    """Matching Pokemon's retreat cost is N less."""

    def __init__(self, amount, target_pred=None):
        self.amount = amount
        self.protects = _protects_pred(target_pred)

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if not self.protects(pokemon, carrier):
            return cost
        return max(0, cost - self.amount)


def retreat_discount(amount, target_pred=None) -> Passive:
    """Retreat cost -N (Air Balloon shape); target_pred defaults to the
    carrier's holder, or 'team' / callable(pokemon, carrier)."""
    return RetreatDiscountPassive(amount, target_pred)


class RetreatFreeWhenPassive(Passive):
    """Retreat cost becomes 0 whenever pred(pokemon, carrier) holds."""

    def __init__(self, pred):
        self.pred = pred

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        return 0 if self.pred(pokemon, carrier) else cost


def retreat_free_when(pred) -> Passive:
    """Free retreat while pred(pokemon, carrier) holds."""
    return RetreatFreeWhenPassive(pred)


class OpponentRetreatTaxPassive(Passive):
    """Every opposing Pokemon's (or only the opposing Active's) retreat cost
    is N more."""

    def __init__(self, amount=1, active_only=False):
        self.amount = amount
        self.active_only = active_only

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if pokemon.owning_player_id == carrier.owning_player_id:
            return cost
        if self.active_only and not is_in_active_spot(pokemon):
            return cost
        return cost + self.amount


def opponent_retreat_tax_passive(amount=1, active_only=False) -> Passive:
    """"The retreat cost of each of your opponent's Pokemon in play is [C]
    more"; active_only for "your opponent's Active Pokemon's retreat cost"."""
    return OpponentRetreatTaxPassive(amount, active_only)


class NoEnergyFreeRetreatPassive(Passive):
    """"If this Pokemon has no Energy attached, it has no Retreat Cost"; with
    inverted=True, "if this Pokemon has any Energy attached ..."."""

    def __init__(self, inverted=False):
        self.inverted = inverted

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if pokemon is not carrier_pokemon(carrier):
            return cost
        has_energy = bool(board.attached_energies(pokemon))
        free = has_energy if self.inverted else not has_energy
        return 0 if free else cost


def no_energy_free_retreat_passive() -> Passive:
    return NoEnergyFreeRetreatPassive()


class TypedEnergyFreeRetreatPassive(Passive):
    """"If this Pokemon has any [type] Energy attached, it has no Retreat
    Cost" (team=True: each of your Pokemon with that Energy); amount overrides
    the cost set instead of zero."""

    def __init__(self, type_value, team=False, amount=0):
        self.type_value = type_value
        self.team = team
        self.amount = amount

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if self.team:
            if pokemon.owning_player_id != carrier.owning_player_id:
                return cost
        elif pokemon is not carrier_pokemon(carrier):
            return cost
        from ptcgo.game.card_effects.pokemon import energy_provides_type
        for energy in board.attached_energies(pokemon):
            if energy_provides_type(energy, self.type_value):
                return self.amount
        return cost


def typed_energy_free_retreat_passive(type_value, team=False,
                                      amount=0) -> Passive:
    return TypedEnergyFreeRetreatPassive(type_value, team, amount)


class HpPerTypedEnergyPassive(Passive):
    """"This Pokemon gets +N HP for each [type] Energy attached to it"."""

    def __init__(self, amount, type_value=None):
        self.amount = amount
        self.type_value = type_value

    def max_hp_bonus(self, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return 0
        from ptcgo.game.card_effects.pokemon import energy_provides_type
        count = 0
        for child in pokemon.children or []:
            if self.type_value is None or energy_provides_type(
                    child, self.type_value):
                count += 1
        return self.amount * count


def hp_per_typed_energy_passive(amount, type_value=None) -> Passive:
    return HpPerTypedEnergyPassive(amount, type_value)


class NoEnergyFreeRetreatPassive(Passive):
    """"If this Pokemon has no Energy attached, it has no Retreat Cost"; with
    inverted=True, "if this Pokemon has any Energy attached ..."."""

    def __init__(self, inverted=False):
        self.inverted = inverted

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if pokemon is not carrier_pokemon(carrier):
            return cost
        has_energy = bool(board.attached_energies(pokemon))
        free = has_energy if self.inverted else not has_energy
        return 0 if free else cost


def no_energy_free_retreat_passive(inverted=False) -> Passive:
    return NoEnergyFreeRetreatPassive(inverted)


class ActiveVsActiveDebuffPassive(Passive):
    """"As long as this Pokemon is in the Active Spot, attacks used by your
    opponent's Active Pokemon do N less damage (before W/R)"."""

    def __init__(self, amount):
        self.amount = amount

    def modify_damage_dealt(self, calc, carrier):
        attacker = calc.attacker
        holder = carrier_pokemon(carrier)
        if not calc.is_attack or attacker is None or holder is None:
            return
        if attacker.owning_player_id == holder.owning_player_id:
            return
        if is_in_active_spot(holder) and is_in_active_spot(attacker):
            calc.amount = max(0, calc.amount - self.amount)


def active_vs_active_debuff_passive(amount) -> Passive:
    return ActiveVsActiveDebuffPassive(amount)


class AdditiveDamageTakenPassive(Passive):
    """"During your next turn, the Defending Pokemon takes N more damage from
    attacks (after W/R)" -- a target-side rider for one turn."""

    def __init__(self, amount):
        self.amount = amount

    def modify_damage_taken(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        if not calc.is_attack or holder is None or calc.target is not holder:
            return
        if calc.attacker is not None and \
                calc.attacker.owning_player_id == holder.owning_player_id:
            return
        calc.amount += self.amount


def additive_damage_taken_passive(amount) -> Passive:
    return AdditiveDamageTakenPassive(amount)


class BenchedFullShieldPassive(Passive):
    """"As long as this Pokemon is on your Bench, prevent all damage from and
    effects of attacks from your opponent's Pokemon done to this Pokemon"."""

    def _benched(self, target, carrier):
        holder = carrier_pokemon(carrier)
        return holder is target and not is_in_active_spot(holder)

    def prevents_damage(self, calc, carrier):
        return bool(calc.is_attack and calc.is_opposing
                    and self._benched(calc.target, carrier))

    def blocks_attack_effects(self, target, carrier, attacker=None):
        return self._benched(target, carrier)


def benched_full_shield_passive() -> Passive:
    return BenchedFullShieldPassive()


class OpponentAttackTaxPassive(Passive):
    """Opposing Pokemon's attacks cost [C] N more."""

    def __init__(self, extra, target_pred=None):
        self.extra = extra
        self.target_pred = target_pred

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if pokemon.owning_player_id == carrier.owning_player_id:
            return cost
        if self.target_pred is not None and not self.target_pred(pokemon):
            return cost
        cost["Colorless"] = cost.get("Colorless", 0) + self.extra
        return cost


def opponent_attack_tax(extra_cost_count, target_pred=None) -> Passive:
    """Opposing (vs the carrier's owner) Pokemon's attacks cost [C] N more;
    target_pred(pokemon) refines which opposing Pokemon are taxed."""
    return OpponentAttackTaxPassive(extra_cost_count, target_pred)


class AttackDiscountPassive(Passive):
    """Attacks cost [C] N less (Colorless removed first, Excited Heart shape)."""

    def __init__(self, count, self_only=True, pred=None):
        self.count = count
        self.self_only = self_only
        self.pred = pred

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if self.self_only:
            if carrier_pokemon(carrier) is not pokemon:
                return cost
        elif pokemon.owning_player_id != carrier.owning_player_id:
            return cost
        if self.pred is not None and not self.pred(pokemon):
            return cost
        if "Colorless" not in cost:
            return cost
        remaining = cost["Colorless"] - self.count
        if remaining > 0:
            cost["Colorless"] = remaining
        else:
            del cost["Colorless"]
        return cost


def attack_discount_passive(count, self_only=True, pred=None) -> Passive:
    """Attacks cost [C] N less; self_only=False widens to the carrier
    owner's whole team, pred(pokemon) refines further."""
    return AttackDiscountPassive(count, self_only, pred)


class FreeAttackCostPassive(Passive):
    """The carrier's attacks cost nothing while `condition` holds: "ignore all
    Energy in this Pokemon's attack costs" (Cramorant's Lost Provisions),
    "... in the attack cost of each of this Pokemon's attacks" (Yanmega,
    the Rotom forms), "if you have Nidoqueen in play, ignore all Energy in
    the costs of attacks used by this Pokemon" (Nidoking)."""

    def __init__(self, condition=None, protects="carrier"):
        self.condition = condition
        self.protects = _protects_pred(protects)

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if not self.protects(pokemon, carrier):
            return cost
        if self.condition is not None and not self.condition(board, pokemon, carrier):
            return cost
        return {}


def free_attack_cost_passive(condition=None, protects="carrier") -> Passive:
    """"Ignore all Energy in <Pokemon>'s attack costs": a continuous grant for
    the named card texts in FreeAttackCostPassive; `condition(board, pokemon,
    carrier)` gates it on board state, `protects` is 'carrier' | 'team' |
    callable(pokemon, carrier). Example::

        Ability("Ancient Roar", game_text="...",
                passive=free_attack_cost_passive(
                    condition=lambda board, p, c: has_nidoqueen(board, c)))
    """
    return FreeAttackCostPassive(condition, protects)


class AttackGrantPassive(Passive):
    """"This Pokemon can use the attacks of <sources> as its own."

    `sources(board, pokemon, carrier)` returns the entities whose printed
    attacks the holder may use -- any Pokemon in play, the holder's Benched
    Pokemon, Basics in the discard pile, the opponent's Active. The attacks
    keep their printed cost and ability_id, so the panel offers each one and
    an attack lock still applies per the attacking entity.
    """

    def __init__(self, sources):
        self.sources = sources

    def granted_attacks(self, board, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return []
        out = []
        for source in self.sources(board, pokemon, carrier) or []:
            if source is pokemon:
                continue  # the holder's own attacks are already offered
            out.extend(attacks_of(source))
        return out


def attack_grant_passive(sources) -> Passive:
    """May use the attacks of the entities `sources(board, pokemon, carrier)`
    returns: "This Pokemon can use the attacks of any Pokemon in play (both
    yours and your opponent's)" (Mew-EX's Versatile), "... of any of your
    Benched Pokemon" (Mew ex's Memory Helix), "... of any Basic Pokemon in
    your discard pile" (Marshadow-GX's Shadow Hunt), "... of its previous
    evolutions" (Memory Capsule -- see previous_evolution_grant_passive).

    Example (card script)::

        Ability("Versatile", game_text="...",
                passive=attack_grant_passive(lambda board, pokemon, carrier: [
                    p for pid in board.player_ids
                    for p in board.pokemon_in_play(pid) if p is not pokemon]))
    """
    return AttackGrantPassive(sources)


class PreviousEvolutionAttacksPassive(Passive):
    """"This Pokemon can use the attacks of its previous evolutions" --
    the attacks of the stack tucked underneath the holder (Memory Capsule).
    `extra_sources(board, pokemon, carrier)` widens the grant."""

    def __init__(self, extra_sources=None):
        self.extra_sources = extra_sources

    def granted_attacks(self, board, pokemon, carrier):
        holder = carrier_pokemon(carrier)
        # A Stadium (or any global carrier) has no carrier_pokemon, and its
        # wording is board-wide: "each player's evolved Pokemon can use any
        # attack from its previous Evolutions" (Shrine of Memories, Meteor
        # Falls). A Pokemon/Tool carrier still grants only to itself.
        if holder is not None and holder is not pokemon:
            return []
        out = previous_evolution_attacks(pokemon)
        for source in (self.extra_sources(board, pokemon, carrier) or []
                       if self.extra_sources is not None else []):
            if source is not pokemon:
                out.extend(attacks_of(source))
        return out


def previous_evolution_grant_passive(extra_sources=None) -> Passive:
    """May use the attacks of the Pokemon tucked underneath it: "this Pokemon
    can use the attacks of its previous evolutions" (Memory Capsule and its
    Stadium/Ability variants); `extra_sources` widens the grant."""
    return PreviousEvolutionAttacksPassive(extra_sources)


class BurnCountersPassive(Passive):
    """Burn checkup puts `counters` damage counters instead of the usual two:
    "Put 4 damage counters instead of 2 on your opponent's Burned Pokemon
    between turns"."""

    def __init__(self, counters):
        self.counters = counters

    def modify_burn_counters(self, counters, pokemon, carrier):
        return max(counters, self.counters)


class NoWeaknessPassive(Passive):
    """Protected Pokemon have no Weakness."""

    def __init__(self, protects="carrier"):
        self.protects = _protects_pred(protects)

    def modify_weakness(self, calc, carrier):
        if self.protects(calc.target, carrier):
            calc.weakness_applies = False


def no_weakness_passive(protects="carrier") -> Passive:
    """"... has no Weakness" (Mysterious Nest shape via a protects pred)."""
    return NoWeaknessPassive(protects)


class WeaknessMultiplierPassive(Passive):
    """Weakness applies xN instead of x2 (Supereffective Glasses shape)."""

    def __init__(self, mult, when=None):
        self.mult = mult
        self.when = when

    def modify_weakness(self, calc, carrier):
        if self.when is not None:
            if not self.when(calc, carrier):
                return
        elif carrier_pokemon(carrier) is not calc.attacker:
            return
        calc.weakness_multiplier = self.mult


def weakness_multiplier_passive(mult, when=None) -> Passive:
    """Rewrites the Weakness multiplier; defaults to the holder attacking,
    or gate with when(calc, carrier)."""
    return WeaknessMultiplierPassive(mult, when)


class NoResistancePassive(Passive):
    """Attacks from the carrier's side aren't affected by Resistance."""

    def __init__(self, when=None):
        self.when = when

    def modify_resistance(self, calc, carrier):
        if self.when is not None:
            if not self.when(calc, carrier):
                return
        elif not (calc.attacker is not None
                  and calc.attacker.owning_player_id == carrier.owning_player_id):
            return
        calc.resistance_applies = False


def no_resistance_passive(when=None) -> Passive:
    """"... isn't affected by Resistance" (Pinsir team shape); defaults to
    the carrier owner's attackers, or gate with when(calc, carrier)."""
    return NoResistancePassive(when)


class ConditionImmunityPassive(Passive):
    """Protected Pokemon can't be affected by the given Special Conditions."""

    def __init__(self, conditions=None, protects="carrier"):
        if conditions is None:
            self.conditions = None  # None = immune to ALL conditions
        elif isinstance(conditions, (list, tuple, set, frozenset)):
            self.conditions = set(conditions)
        else:
            self.conditions = {conditions}
        self.protects = _protects_pred(protects)

    def blocks_special_conditions(self, target, condition, carrier):
        if self.conditions is not None and condition not in self.conditions:
            return False
        return bool(self.protects(target, carrier))


def condition_immunity_passive(conditions=None, protects="carrier") -> Passive:
    """Condition immunity (Galarian Rapidash shape); conditions=None means
    ALL, else a SpecialConditions member or iterable of them."""
    return ConditionImmunityPassive(conditions, protects)


class NoRetreatPassive(Passive):
    """Matching Pokemon can't retreat."""

    def __init__(self, target_pred):
        self.target_pred = target_pred

    def blocks_retreat(self, pokemon, carrier):
        return bool(self.target_pred(pokemon, carrier))


def condition_retreat_lock_passive(conditions=None, carrier_conditions=None,
                                  carrier_clear: bool = False,
                                  while_active: bool = True) -> Passive:
    """"As long as this Pokemon is your Active Pokemon, your opponent's
    <Confused/Poisoned/...> Pokemon can't retreat" (Poliwrath, Dragalge,
    Snorlax).

    `conditions` is one SpecialConditions member, an iterable of them, or
    "any" for "affected by Special Conditions"; `carrier_conditions` gate the
    lock on the CARRIER being affected (PL2 Snorlax's "as long as Snorlax is
    Asleep"), and `carrier_clear` on the carrier being unaffected (BASEP
    Snorlax's "this power stops working when Snorlax is affected")."""
    def _as_names(spec):
        if spec is None:
            return ()
        if spec == "any":
            return ("any",)
        if isinstance(spec, (list, tuple, set)):
            return tuple(CLIENT_SPECIAL_CONDITION_NAMES[c] for c in spec)
        return (CLIENT_SPECIAL_CONDITION_NAMES[spec],)

    required = _as_names(conditions)
    carrier_required = _as_names(carrier_conditions)

    def predicate(pokemon, carrier) -> bool:
        if not opposing_pokemon(pokemon, carrier):
            return False
        if while_active and not is_in_active_spot(carrier):
            return False
        carrier_now = set(carrier.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])
        if carrier_clear and carrier_now:
            return False
        if carrier_required and not all(name in carrier_now
                                        for name in carrier_required):
            return False
        current = set(pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])
        if not required:
            return True
        if required == ("any",):
            return bool(current)
        return all(name in current for name in required)

    return no_retreat_passive(predicate)


def no_retreat_passive(target_pred) -> Passive:
    """Blocks retreat while target_pred(pokemon, carrier) holds (Flygon:
    `lambda p, c: opposing_active(p, c) and is_in_active_spot(c)`)."""
    return NoRetreatPassive(target_pred)


class AbilityLockPassive(Passive):
    """Matching Pokemon have no Abilities."""

    def __init__(self, target_pred):
        self.target_pred = target_pred

    def blocks_abilities(self, pokemon, carrier):
        return bool(self.target_pred(pokemon, carrier))


def ability_lock_passive(target_pred) -> Passive:
    """Turns off Abilities while target_pred(pokemon, carrier) holds (Path
    to the Peak: `lambda p, c: has_rule_box(p.archetype_id)`)."""
    return AbilityLockPassive(target_pred)


class HealingBlockPassive(Passive):
    """Matching Pokemon can't have damage healed."""

    def __init__(self, target_pred):
        self.target_pred = target_pred

    def prevents_healing(self, target, carrier):
        return bool(self.target_pred(target, carrier))


def healing_block_passive(target_pred) -> Passive:
    """Blocks healing while target_pred(target, carrier) holds (Mimikyu)."""
    return HealingBlockPassive(target_pred)


class AttackEffectShieldPassive(Passive):
    """Protected Pokemon are shielded from opposing attack EFFECTS.

    `attacker_pred(attacker)` is the printed scope ("effects of attacks used by
    your opponent's Pokemon-EX"); None is every opposing attacker."""

    def __init__(self, protects="carrier", attacker_pred=None):
        self.protects = _protects_pred(protects)
        self.attacker_pred = attacker_pred

    def blocks_attack_effects(self, target, carrier, attacker=None):
        if not self.protects(target, carrier):
            return False
        if self.attacker_pred is None:
            return True
        return attacker is not None and bool(self.attacker_pred(attacker))


def attack_effect_shield_passive(protects="carrier", attacker_pred=None) -> Passive:
    """Unfazed Fat generalized: shields from attack effects, not damage
    (the engine already scopes the check to opposing attacks)."""
    return AttackEffectShieldPassive(protects, attacker_pred)


class FlipPreventDamagePassive(Passive):
    """"If any damage is done to this Pokemon by attacks, flip a coin. If
    heads, prevent that damage" (Infiltrator / Primate Dexterity)."""

    def __init__(self, title="", protects="carrier"):
        self.title = title
        self.protects = _protects_pred(protects)

    async def damage_interceptor(self, ctx, calc, target, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.amount > 0):
            return None
        if not self.protects(target, carrier):
            return None
        heads = await ctx.flip_coins(1, self.title,
                                     source=carrier_pokemon(carrier) or carrier)
        if heads and heads[0]:
            calc.prevented = True
            return 0
        return None


class RetaliateCountersPassive(Passive):
    """"During your opponent's next turn, if this Pokemon is damaged by an
    attack (even if it is Knocked Out), put N damage counters on the
    attacking Pokemon" (Counter Press shape, fixed counter count)."""

    def __init__(self, counters=1):
        self.counters = counters

    async def damage_interceptor(self, ctx, calc, target, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.amount > 0):
            return None
        if target is not carrier_pokemon(carrier):
            return None
        attacker = calc.attacker
        if attacker is not None:
            await ctx.deal_damage(self.counters * 10, target=attacker,
                                  apply_modifiers=False, as_counters=True)
        return None


def retaliate_counters_passive(counters=1) -> Passive:
    """Strike-back shield for the opponent's next turn: N counters on whoever
    damages this Pokemon (the damage itself still lands)."""
    return RetaliateCountersPassive(counters)


def flip_prevent_damage_passive(title="") -> Passive:
    """Flip-to-prevent shield: heads prevents the whole attack hit; the flip
    choreographs inside the attack bracket (queued on the attack ctx)."""
    return FlipPreventDamagePassive(title)


class GutsSurvivePassive(Passive):
    """"If this Pokemon would be Knocked Out by damage from an attack, [flip a
    coin -- if heads,] it is not Knocked Out and its remaining HP becomes
    `hp_floor`" (Guts; Sturdy with flip=False + require_full_hp=True)."""

    def __init__(self, hp_floor=10, title="Guts", flip=True,
                 require_full_hp=False, protects="carrier"):
        self.hp_floor = hp_floor
        self.title = title
        self.flip = flip
        self.require_full_hp = require_full_hp
        self.protects = _protects_pred(protects)

    async def damage_interceptor(self, ctx, calc, target, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.amount > 0):
            return None
        if not self.protects(target, carrier):
            return None
        current = target.get_attribute(AttrID.HP, 0)
        if calc.amount < current:
            return None  # would not Knock Out
        if self.require_full_hp and current < effective_max_hp(calc.board, target):
            return None
        if self.flip:
            heads = await ctx.flip_coins(1, self.title,
                                         source=carrier_pokemon(carrier) or carrier)
            if not (heads and heads[0]):
                return None
        return max(0, current - self.hp_floor)


def guts_survive_passive(hp_floor=10, title="Guts", flip=True,
                         require_full_hp=False) -> Passive:
    """KO-survive interceptor: only when the hit would KO; heads (or always
    with flip=False) rewrites the dealt amount so remaining HP = hp_floor."""
    return GutsSurvivePassive(hp_floor, title, flip, require_full_hp)


class TrainerEffectShieldPassive(Passive):
    """Shields the carrier's owner from opposing trainer-card effects
    (Dew Guard: "prevent all effects of that card done to you or your hand")."""

    def __init__(self, supporters_only=True, protects=None, while_active=False,
                 condition=None):
        self.supporters_only = supporters_only
        # protects(affected_entity_or_None, carrier): scopes the shield to
        # matching direct objects (None = the whole side, legacy behavior).
        self.protects = protects
        self.while_active = while_active
        self.condition = condition

    def blocks_trainer_effects(self, affected_player_id, trainer_card,
                               trainer_type, carrier, affected_entity=None,
                               board=None):
        if self.supporters_only and trainer_type != TrainerType.SUPPORTER.value:
            return False
        if affected_player_id != carrier.owning_player_id:
            return False
        if self.while_active \
                and not is_in_active_spot(carrier_pokemon(carrier) or carrier):
            return False
        if self.condition is not None and not self.condition(board, carrier):
            return False
        if self.protects is not None:
            return bool(self.protects(affected_entity, carrier))
        return True


def trainer_effect_shield_passive(supporters_only=True, protects=None,
                                  while_active=False, condition=None) -> Passive:
    """Dew Guard shape; the engine already scopes it to effects a DIFFERENT
    player's trainer card does to the shielded side. protects/while_active/
    condition(board, carrier) narrow the shield (Princess's Curtain, Baffling)."""
    return TrainerEffectShieldPassive(supporters_only, protects, while_active,
                                      condition)


class SupporterReplacementPassive(Passive):
    """Opposing Supporter cards resolve `replacement` instead of their own
    effect (Shifty Substitution: "each Supporter card in your opponent's hand
    has the effect 'Draw 3 cards.'")."""

    def __init__(self, replacement, opponents_only=True, while_active=True):
        self.replacement = replacement
        self.opponents_only = opponents_only
        self.while_active = while_active

    def replace_supporter_effect(self, card, player_id, carrier):
        if self.opponents_only and player_id == carrier.owning_player_id:
            return None
        if self.while_active:
            holder = carrier_pokemon(carrier) or carrier
            if not is_in_active_spot(holder):
                return None
        return self.replacement


def replace_opponent_supporters(replacement, while_active=True) -> Passive:
    """Shifty Substitution shape: `replacement` is an async def effect(ctx)
    run as the opponent's Supporter effect (trainer ctx, shields apply)."""
    return SupporterReplacementPassive(replacement, while_active=while_active)


class EnergyAttachTaxPassive(Passive):
    """Opposing manual energy attaches flip a coin; tails discards the energy
    instead of attaching (Slimy Room; per text the turn attachment is NOT
    used up)."""

    def __init__(self, opponents_only=True, while_active=True):
        self.opponents_only = opponents_only
        self.while_active = while_active

    def taxes_energy_attach(self, attaching_player_id, energy, target, carrier):
        if self.opponents_only \
                and attaching_player_id == carrier.owning_player_id:
            return False
        if self.while_active:
            holder = carrier_pokemon(carrier) or carrier
            if not is_in_active_spot(holder):
                return False
        return True


def energy_attach_tax_passive(opponents_only=True, while_active=True) -> Passive:
    """Slimy Room shape: taxes the opponent's manual attach with a coin flip."""
    return EnergyAttachTaxPassive(opponents_only, while_active)


# ======================================================================
# GROUP B -- temporary-shield effect factories (expiring temp passives)
# ======================================================================
# Factory forms are COMPLETE attack effects: printed damage first (a no-op
# at damage 0), then the rider. The apply_* helpers are riders only.

class TempShieldPassive(Passive):
    """reduce-N / prevent / effects_too shield on its carrier vs opposing attacks.

    `attacker_pred(attacker)` narrows WHICH attackers the shield answers
    ("damage from the Defending Pokemon", "prevent all damage from Basic
    Pokemon"), and `max_damage` caps it to hits of that size or smaller."""

    def __init__(self, reduce=None, prevent=False, effects_too=False,
                 attacker_pred=None, max_damage=None):
        self.reduce = reduce
        self.prevent = prevent
        self.effects_too = effects_too
        self.attacker_pred = attacker_pred
        self.max_damage = max_damage

    def _answers(self, calc, carrier) -> bool:
        if not (calc.is_attack and calc.is_opposing):
            return False
        if carrier_pokemon(carrier) is not calc.target:
            return False
        if self.attacker_pred is not None and not self.attacker_pred(calc.attacker):
            return False
        if self.max_damage is not None and calc.amount > self.max_damage:
            return False
        return True

    def modify_damage_taken(self, calc, carrier):
        if self.reduce and self._answers(calc, carrier):
            calc.amount = max(0, calc.amount - self.reduce)

    def prevents_damage(self, calc, carrier):
        return bool(self.prevent and self._answers(calc, carrier))

    def blocks_attack_effects(self, target, carrier, attacker=None):
        if not self.effects_too or carrier_pokemon(carrier) is not target:
            return False
        if self.attacker_pred is None:
            return True
        return attacker is not None and bool(self.attacker_pred(attacker))


async def apply_protection(ctx, target=None, reduce=None, prevent=False,
                           effects_too=False, through_own_next_turn=False,
                           attacker_pred=None, max_damage=None):
    """Rider: shield `target` (default the attack's user) through the
    opponent's next turn; the shield ends early if the carrier leaves the
    Active spot / play (clear_pokemon_effects).

    `attacker_pred(attacker)` scopes the shield to some attackers and
    `max_damage` to hits no bigger than that."""
    target = target if target is not None else ctx.attacker
    if target is None:
        return False
    shield = TempShieldPassive(reduce=reduce, prevent=prevent,
                               effects_too=effects_too,
                               attacker_pred=attacker_pred,
                               max_damage=max_damage)
    if through_own_next_turn:
        ctx.add_passive_through_own_next_turn(target, shield)
    else:
        ctx.add_passive_through_opponents_turn(target, shield)
    if target.entity_id not in ctx.visual_targets:
        ctx.visual_targets.append(target.entity_id)
    return True


def protect_next_turn(reduce=None, prevent=False, effects_too=False,
                      self_target=True, attacker_pred=None, max_damage=None):
    """Complete attack effect: printed damage, then shield the user (or the
    Defending Pokemon when self_target=False) during the opponent's next
    turn -- reduce=N takes-less, prevent=True full prevention, effects_too
    adds the attack-effect shield ("all effects ... including damage")."""
    async def effect(ctx):
        await ctx.deal_damage()
        target = ctx.attacker if self_target else ctx.defender
        await apply_protection(ctx, target=target, reduce=reduce,
                               prevent=prevent, effects_too=effects_too,
                               attacker_pred=attacker_pred,
                               max_damage=max_damage)
    return effect


def shield_from_defender_next_turn(reduce=None, prevent=False,
                                   effects_too=False, target="self"):
    """"During your opponent's next turn, any damage done by attacks from the
    Defending Pokemon is reduced by N" (Minun's Negative Ion): binds the shield
    to the Pokemon that WAS Defending when the ability was used, so it does not
    over-reach to the opponent's whole side the way a plain side shield does."""
    async def effect(ctx):
        defender = ctx.defender
        if defender is None:
            return
        await shield_source_next_turn(
            reduce=reduce, prevent=prevent, effects_too=effects_too,
            target=target, attacker_pred=lambda attacker: attacker is defender,
        )(ctx)
    return effect


def shield_source_next_turn(reduce=None, prevent=False, effects_too=False,
                            target="self", then=None, attacker_pred=None):
    """"During your opponent's next turn, prevent all damage done to this
    Pokemon by attacks" from an ABILITY or a Trainer rather than an attack:
    `protect_next_turn` is the attack twin and deals the printed damage first,
    which an ability must not. target: "self" (the source Pokemon) or a
    PokemonEntity/callable the caller already chose. `attacker_pred(attacker)`
    narrows the shield to some attackers ("damage done by attacks from THE
    DEFENDING Pokemon"), which a whole-side shield would over-reach on.
    `then(ctx, shielded)`."""
    async def effect(ctx):
        source = ctx.source
        if callable(target):
            picked = target(ctx)
        elif target == "self":
            picked = source
        else:
            picked = target
        shielded = await apply_protection(
            ctx, target=picked, reduce=reduce, prevent=prevent,
            effects_too=effects_too, attacker_pred=attacker_pred)
        if then is not None:
            await then(ctx, shielded)
    return effect


class HealAmountPassive(Passive):
    """Rewrites heals done to the carrier (or its side): "whenever you heal a
    Pokemon, heal 20 more" / a flat "heals 30 damage instead of 20" / a
    doubling ("double the amount of damage healed")."""

    def __init__(self, bonus=0, amount=None, protects="carrier", minimum=0,
                 multiply=1):
        self.bonus = bonus
        self.amount = amount
        self.protects = _protects_pred(protects)
        self.minimum = minimum
        self.multiply = multiply

    def modify_heal_amount(self, pokemon, carrier, amount):
        if not self.protects(pokemon, carrier):
            return amount
        if self.minimum and amount < self.minimum:
            return amount
        if self.amount is not None:
            return self.amount
        return amount * self.multiply + self.bonus


def heal_multiplier(bonus: int = 0, amount: Optional[int] = None,
                    protects="team", minimum: int = 0,
                    multiply: int = 1) -> Passive:
    """`bonus` adds to every heal ("heal 20 more"); `amount` replaces the heal
    outright ("heals 30 damage instead"), gated by `minimum` when given;
    `multiply=2` doubles it (Legendary Trench)."""
    return HealAmountPassive(bonus=bonus, amount=amount, protects=protects,
                             minimum=minimum, multiply=multiply)


class EnergyReturnPassive(Passive):
    """Ecogym: Energy discarded from a Pokemon goes to its owner's hand instead
    of the discard pile ("another player's non-Colorless Energy")."""

    def __init__(self, other_player_only=True, non_colorless=True):
        self.other_player_only = other_player_only
        self.non_colorless = non_colorless

    def energy_discard_destination(self, energy, pokemon, discarder_id, carrier):
        if pokemon is not None and self.other_player_only \
                and pokemon.owning_player_id == discarder_id:
            return None
        if self.non_colorless and energy_provides_type(
                energy, PokemonTypes.COLORLESS.value):
            return None
        return "hand"


def energy_return_on_discard_passive(other_player_only: bool = True,
                                    non_colorless: bool = True) -> Passive:
    return EnergyReturnPassive(other_player_only, non_colorless)


class NoDiscardReturnPassive(Passive):
    """Pokemon Tower: cards in a discard pile never return to a hand."""

    def discard_to_hand_blocked(self, card, carrier):
        return True


def no_discard_return_passive() -> Passive:
    return NoDiscardReturnPassive()


class TrainerPlayFlipPassive(Passive):
    """Chaos Gym: every non-Stadium Trainer play is coin-flipped; tails makes
    the card do nothing."""

    def trainer_play_flips(self, card, player_id, carrier):
        return card.get_attribute(AttrID.TRAINER_TYPE) != TrainerType.STADIUM.value


def trainer_play_flip_passive() -> Passive:
    return TrainerPlayFlipPassive()


class RetreatFlipPassive(Passive):
    """Mirage Stadium: each retreat attempt is coin-flipped; tails refuses it."""

    def retreat_flips(self, pokemon, carrier):
        return True


def retreat_flip_passive() -> Passive:
    return RetreatFlipPassive()


class WROnBenchPassive(Passive):
    """Wide Lens: the holder's attacks are affected by Weakness and Resistance
    on the opponent's Benched Pokemon too."""

    def wr_applies_to_bench(self, calc, carrier):
        return (calc.is_attack and calc.is_opposing
                and carrier_pokemon(carrier) is calc.attacker)


def wr_on_bench_passive() -> Passive:
    return WROnBenchPassive()


class ResistanceReducedPassive(Passive):
    """Resistance Gym: every Pokemon's Resistance is `amount` smaller."""

    def __init__(self, amount=20):
        self.amount = amount

    def modify_resistance_amount(self, amount, calc, carrier):
        return max(0, amount - self.amount)


def resistance_reduced_passive(amount: int = 20) -> Passive:
    return ResistanceReducedPassive(amount)


class NoAttackAtHPPassive(Passive):
    """Blizzard Town: a Pokemon with `max_remaining` HP or less remaining
    can't attack -- both sides."""

    def __init__(self, max_remaining=40, opponents_only=False):
        self.max_remaining = max_remaining
        self.opponents_only = opponents_only

    def blocks_attack(self, pokemon, carrier):
        if self.opponents_only and pokemon.owning_player_id == carrier.owning_player_id:
            return False
        return pokemon.get_attribute(AttrID.HP, 0) <= self.max_remaining


def no_attack_at_hp(max_remaining: int = 40, opponents_only: bool = False) -> Passive:
    return NoAttackAtHPPassive(max_remaining, opponents_only)


class ConditionsSurviveEvolutionPassive(Passive):
    """Sea of Nothingness ("Special Conditions are not removed when Pokemon
    evolve or devolve") and Dizzying Valley (Confused only)."""

    def __init__(self, conditions=None):
        # None = every condition.
        self.conditions = None if conditions is None else tuple(conditions)

    def keeps_condition_on_evolve(self, condition, pokemon, carrier):
        if self.conditions is None:
            return True
        return condition in self.conditions


def conditions_survive_evolution_passive(*conditions) -> Passive:
    """No `conditions` means all of them; pass client condition names or
    SpecialConditions members for the narrower wordings."""
    names = tuple(CLIENT_SPECIAL_CONDITION_NAMES[c] if c in CLIENT_SPECIAL_CONDITION_NAMES
                  else c for c in conditions) or None
    return ConditionsSurviveEvolutionPassive(names)


class ExtraPoisonCountersPassive(Passive):
    """Poisoned Pokemon take `amount` more damage counters at Checkup
    (Virbank City Gym: "each Pokemon affected by Poison now takes 2 damage
    from poison between turns")."""

    def __init__(self, amount=2, opponents_only=False, pred=None):
        self.amount = amount
        self.opponents_only = opponents_only
        self.pred = pred

    def poison_checkup_counters(self, pokemon, carrier, counters):
        if self.opponents_only and pokemon.owning_player_id == carrier.owning_player_id:
            return counters
        if self.pred is not None and not self.pred(pokemon, carrier):
            return counters
        return counters + self.amount


def extra_poison_counters(amount: int = 2, opponents_only: bool = False,
                          pred=None) -> Passive:
    """Stadium/passive factory for the Virbank wording; `pred(pokemon, carrier)`
    narrows it (Perilous Jungle: non-Darkness only)."""
    return ExtraPoisonCountersPassive(amount, opponents_only, pred)


def poison_not_of_type(*types) -> Callable[[Any, Any], bool]:
    """(pokemon, carrier) pred: the Poisoned Pokemon is not of these types."""
    wanted = set(types)

    def pred(pokemon, carrier):
        current = set(pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])
        return not (current & wanted)

    return pred


class BenchDamageShieldPassive(Passive):
    """Mountain Ring ("prevent all damage done to Benched Pokemon by attacks")
    and Sky Pillar (the same plus the attack's effects)."""

    def __init__(self, effects_too=False):
        self.effects_too = effects_too

    def blocks_bench_damage(self, calc, carrier):
        return True

    def blocks_attack_effects(self, target, carrier, attacker=None):
        if not self.effects_too:
            return False
        parent = getattr(target, "parent", None)
        return bool(parent) and parent.get_attribute(AttrID.NAME) == "bench"


def bench_damage_shield(effects_too: bool = False) -> Passive:
    """`effects_too=True` is Sky Pillar; the default is Mountain Ring."""
    return BenchDamageShieldPassive(effects_too)


class AttackCostModifierPassive(Passive):
    """Attacks of one group of Pokemon cost [C] more or less, on either side
    (Nighttime Mine: each Tera Pokemon's attacks; Wondrous Labyrinth: non-Fairy;
    Dimension Valley: each Psychic Pokemon's attacks cost [C] less)."""

    def __init__(self, delta, pred=None, side="both"):
        self.delta = delta
        self.pred = pred
        self.side = side

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if self.side == "team" and pokemon.owning_player_id != carrier.owning_player_id:
            return cost
        if self.side == "opposing" and pokemon.owning_player_id == carrier.owning_player_id:
            return cost
        if self.pred is not None and not self.pred(pokemon, board):
            return cost
        colored = cost.get("Colorless", 0) + self.delta
        if colored > 0:
            cost["Colorless"] = colored
        elif colored <= 0:
            cost.pop("Colorless", None)
        return cost


def attack_cost_modifier(delta: int, pred=None, side: str = "both") -> Passive:
    """`delta` +1 charges a Colorless more, -1 one less (dropping the entry at
    zero); `pred(pokemon, board)` narrows who it applies to, and `side` is
    "both", "team" or "opposing"."""
    return AttackCostModifierPassive(delta, pred, side)


class RetreatCostModifierPassive(Passive):
    """Retreat cost +/- N, optionally for one group of Pokemon ("each Pokemon
    without Team Aqua in its name pays [C] more", "Basic Pokemon pay [C]
    more") -- the Stadium wording base."""

    def __init__(self, delta, pred=None, active_only=False):
        self.delta = delta
        self.pred = pred
        self.active_only = active_only

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if self.active_only and not is_in_active_spot(pokemon):
            return cost
        if self.pred is not None and not self.pred(pokemon, board):
            return cost
        return max(0, cost + self.delta)


def retreat_cost_modifier(delta: int, pred=None,
                          active_only: bool = False) -> Passive:
    """`delta` +1 charges more, -1 pays less; `pred(pokemon, board)` narrows
    who it applies to and `active_only` is "your Active Pokemon"."""
    return RetreatCostModifierPassive(delta, pred, active_only)


class TeamHPBonusPassive(Passive):
    """Every Pokemon on the chosen side(s) gets `amount` more max HP (Aspertia
    City Gym's +20 to Colorless; Snowpoint Temple's +20 to the unevolved)."""

    def __init__(self, amount=20, protects="each", pred=None, stacking_key=None):
        self.amount = amount
        self.protects = _protects_pred(protects)
        self.pred = pred
        self.stacking_key = stacking_key

    def max_hp_bonus(self, pokemon, carrier):
        if not self.protects(pokemon, carrier):
            return 0
        if self.pred is not None and not self.pred(pokemon, carrier):
            return 0
        return self.amount


def team_hp_bonus(amount: int = 20, protects="each", pred=None,
                  stacking_key=None) -> Passive:
    """`protects='each'` covers both boards, `'team'` only the Stadium holder's
    side (Aspertia's wording names both). `pred(pokemon, carrier)` narrows it by
    type or stage."""
    return TeamHPBonusPassive(amount, protects, pred, stacking_key)


class BenchCapacityPassive(Passive):
    """Bench cap for both players (Collapsed Stadium 4, Narrow Gym 4) or for
    the carrier's own side alone (Parallel City's down-arrow face: 3)."""

    def __init__(self, limit=4, protects="each", trim_to="discard", mode="cap",
                 raise_pred=None):
        self.raise_pred = raise_pred
        self.limit = limit
        self.mode = mode
        if mode not in ("cap", "raise"):
            raise ValueError(f"bench capacity mode must be 'cap' or 'raise': {mode!r}")
        self.side_only = protects == "team"
        if protects not in ("each", "team"):
            raise ValueError(
                f"bench capacity protects must be 'each' or 'team': {protects!r}")
        self.trim_to = trim_to

    def _covers(self, player_id, carrier):
        return not self.side_only or player_id == carrier.owning_player_id

    def bench_capacity(self, player_id, carrier):
        if self.mode != "cap":
            return None
        return self.limit if self._covers(player_id, carrier) else None

    def bench_capacity_raise(self, player_id, carrier, board=None):
        if self.mode != "raise":
            return None
        if not self._covers(player_id, carrier):
            return None
        if self.raise_pred is not None and not self.raise_pred(player_id, board):
            return None
        return self.limit

    def bench_trim_area(self, player_id, carrier):
        return "hand" if self.trim_to == "hand" and self._covers(player_id, carrier) else None


def bench_capacity_passive(limit: int = 4, protects="each",
                           trim_to: str = "discard", mode: str = "cap",
                           raise_pred=None) -> Passive:
    """`protects='each'` caps both players (Narrow Gym, Collapsed Stadium);
    `'team'` caps only the Stadium holder's side (Parallel City's face).
    `trim_to='hand'` returns trimmed stacks to hand (Narrow Gym) instead of
    discarding them."""
    """`raise_pred(player_id, board)` gates a raise on board state (Area Zero
    Underdepths: only while the player has a Tera Pokemon in play)."""
    return BenchCapacityPassive(limit, protects, trim_to, mode, raise_pred)


class SuppressAllToolsPassive(Passive):
    """Jamming Tower: every attached Pokemon Tool has no effect."""

    def suppresses_tool(self, tool, carrier):
        return True


def suppress_all_tools() -> Passive:
    return SuppressAllToolsPassive()


def holder_has_energy_of(*types, holder_pred=None) -> Callable[[Any, Any], bool]:
    """(pokemon, carrier) pred: the Pokemon has an attached Energy of one of
    `types` (Shadow Circle, Plasma Frigate: "has any Darkness Energy attached
    to it"). Accepts basic and special Energy alike."""
    wanted = set(types)

    def pred(pokemon, carrier) -> bool:
        if holder_pred is not None and not holder_pred(pokemon):
            return False
        for child in getattr(pokemon, "children", []) or []:
            options = child.get_attribute(AttrID.ENERGY_INFO) or {}
            provided = set()
            for option in (options.get("options") or []):
                provided.update(option if isinstance(option, (list, tuple)) else [option])
            if provided & wanted:
                return True
        return False

    return pred


class NamedAttackerFlipRiderPassive(Passive):
    """Vermilion City Gym: after an attack by a Pokemon whose printed name
    contains `name`, flip a coin -- heads adds `heads_damage` to the Defending
    Pokemon, tails puts `tails_self_damage` on the attacker."""

    def __init__(self, name, heads_damage=10, tails_self_damage=10):
        self.name = (name or "").strip().lower()
        self.heads_damage = heads_damage
        self.tails_self_damage = tails_self_damage

    async def on_attack_resolved(self, ctx, attacker, defender, carrier):
        if attacker is None:
            return
        definition = def_for(getattr(attacker, "archetype_id", "") or "")
        if self.name not in (getattr(definition, "display_name", "") or "").lower():
            return
        results = await ctx.flip_coins(1, f"{self.name.title()} attack")
        heads = bool(results) and all(results)
        if heads and defender is not None and self.heads_damage:
            await ctx.deal_damage(self.heads_damage, target=defender,
                                  apply_modifiers=False)
        elif not heads and self.tails_self_damage:
            await ctx.deal_damage(self.tails_self_damage, target=attacker,
                                  apply_modifiers=False)


def named_attacker_flip_rider(name: str, heads_damage: int = 10,
                              tails_self_damage: int = 10) -> Passive:
    """`name` is matched against the attacker's printed name (Lt. Surge)."""
    return NamedAttackerFlipRiderPassive(name, heads_damage, tails_self_damage)


class TrainerPlayCostPassive(Passive):
    """No Removal Gym: playing one of `names` costs `cost` OTHER hand cards."""

    def __init__(self, cost=2, names=()):
        self.cost = cost
        self.names = tuple(n.strip().lower() for n in names)

    def trainer_play_cost(self, card, player_id, carrier):
        definition = def_for(getattr(card, "archetype_id", "") or "")
        name = (getattr(definition, "display_name", "") or "").strip().lower()
        return self.cost if name in self.names else 0


def trainer_play_cost_passive(cost: int = 2, *names: str) -> Passive:
    """`cost` other hand cards to play a card named in `names`."""
    return TrainerPlayCostPassive(cost, names)


class VoidsStadiumPlayPassive(Passive):
    """Chaotic Swell: a Stadium played from hand is discarded on arrival, and
    this one goes with it, so the new Stadium never takes effect."""

    def voids_stadium_play(self, carrier):
        return True


def voids_stadium_play() -> Passive:
    return VoidsStadiumPlayPassive()


class SleepRecoveryCoinsPassive(Passive):
    """Slumbering Forest: an Asleep Pokemon flips `coins` coins at Checkup and
    only wakes when every one is heads."""

    def __init__(self, coins=2):
        self.coins = coins

    def sleep_recovery_coins(self, pokemon, carrier):
        return self.coins


def sleep_recovery_coins(coins: int = 2) -> Passive:
    return SleepRecoveryCoinsPassive(coins)


class DiscardSelfOnRetreatPassive(Passive):
    """Balloon Berry: "when the Pokemon this card is attached to retreats,
    discard this card" (and pay no Energy for the retreat)."""

    async def on_retreat(self, ctx, pokemon, carrier) -> None:
        if carrier is pokemon:
            return
        await ctx.discard_cards([carrier])


def discard_self_on_retreat() -> Passive:
    """`on_retreat` half of Balloon Berry; compose with retreat_discount."""
    return DiscardSelfOnRetreatPassive()


def _wants_outcome(fn) -> bool:
    """Whether a follow-up takes the first part's outcome as a second argument
    (`async def then(ctx, outcome)`) rather than `then(ctx)`."""
    import inspect

    try:
        parameters = inspect.signature(fn).parameters.values()
    except (TypeError, ValueError):
        return False
    positional = [p for p in parameters
                  if p.kind in (p.POSITIONAL_ONLY, p.POSITIONAL_OR_KEYWORD)]
    if any(p.kind == p.VAR_POSITIONAL for p in parameters):
        return False
    return len(positional) >= 2


async def _run_step(ctx, fn, outcome=None):
    if outcome is None or not _wants_outcome(fn):
        return await fn(ctx)
    return await fn(ctx, outcome)


def composed(first, then=None, on_success=None, on_fail=None):
    """"body, then rider" for an ability, as HOME-13 specified it.

    `then` always runs after `first`; `on_success` runs only when `first`
    returned a truthy result and `on_fail` when it returned falsy. Each element
    is an ordinary `async def effect(ctx)` (a factory call already is one), and
    `ctx` carries through unchanged. A step without a signal (returns None)
    is treated as success; pass `first` through do_a_then_b directly for the
    strict "if you do" reading."""
    async def effect(ctx):
        outcome = await first(ctx)
        happened = True if outcome is None else bool(outcome)
        if then is not None:
            await _run_step(ctx, then, outcome)
        if happened and on_success is not None:
            await _run_step(ctx, on_success, outcome)
        if not happened and on_fail is not None:
            await _run_step(ctx, on_fail, outcome)
        return outcome
    return effect


async def do_a_then_b(first, then, ctx, on_none: bool = True):
    """"Do A. If you do, B" for an ability: runs `first`, and runs `then` only
    when `first` reports that something happened.

    The step reports through its return value, the way the engine's verbs do:
    an int is the amount it moved/placed/healed (0 = nothing), a list is what it
    chose (empty = nothing), False is an explicit "no". None means the step has
    no signal, and counts as success unless `on_none=False`."""
    outcome = await first(ctx)
    if outcome is None:
        happened = on_none
    elif isinstance(outcome, bool):
        happened = outcome
    elif isinstance(outcome, (int, float)):
        happened = outcome > 0
    else:
        happened = bool(outcome)
    if happened and then is not None:
        await _run_step(ctx, then, outcome)
    return happened


def ability_then(first, then, on_none: bool = True):
    """`Ability(effect=...)` wrapper for a two-part body; see do_a_then_b."""
    async def effect(ctx):
        await do_a_then_b(first, then, ctx, on_none=on_none)
    return effect


def discard_from_hand_then(predicate, count: int, then,
                           prompt: str = "Choose a card to discard"):
    """"Discard N cards from your hand. If you do, B" — B runs only for cards
    actually discarded (the discard verb reports nothing, so this counts)."""
    async def first(ctx):
        hand = ctx.hand()
        matches = [card for card in hand if predicate is None or predicate(card)]
        if not matches or count <= 0:
            return 0
        picks = matches if len(matches) <= count else await ctx.choose_cards(
            matches, count, minimum=0, prompt=prompt)
        if not picks:
            return 0
        await ctx.discard_cards(list(picks))
        return len(picks)

    async def effect(ctx):
        await do_a_then_b(first, then, ctx)
    return effect


def put_counters_then(count: int, then, candidates=None):
    """"Put N damage counters on <the opponent's Pokemon>. If you do, B" — B
    runs only when at least one counter landed."""
    async def first(ctx):
        return await ctx.place_damage_counters(count, candidates)

    async def effect(ctx):
        await do_a_then_b(first, then, ctx)
    return effect


async def self_knockout(ctx):
    """"This Pokemon is Knocked Out" as a rider; True when it happened."""
    holder = ctx.source
    if holder is None or ctx.effects_blocked(holder):
        return False
    await ctx.knock_out(holder)
    return True


def self_ko_rider():
    """`composed(..., then=self_ko_rider())` — the Cofagrigus shape."""
    async def effect(ctx):
        await self_knockout(ctx)
    return effect


def self_ko_ability(then=None):
    """"If you use this ability, this Pokemon is Knocked Out": runs the body,
    then Knocks Out the ability's Pokemon (Unown, Crobat)."""
    async def effect(ctx):
        if then is not None:
            await then(ctx)
        await self_knockout(ctx)
    return effect


def attacker_is_basic(include_colorless: bool = True):
    """"damage from Basic Pokemon" (include_colorless=False for "Basic
    non-Colorless Pokemon")."""
    def pred(attacker) -> bool:
        if attacker is None:
            return False
        if attacker.get_attribute(AttrID.STAGE) != PokemonStage.BASIC.value:
            return False
        if include_colorless:
            return True
        types = attacker.get_attribute(AttrID.POKEMON_TYPES) or []
        return PokemonTypes.COLORLESS.value not in types

    return pred


def attacker_is_evolution():
    """""damage from Evolution Pokemon"."""
    def pred(attacker) -> bool:
        return attacker is not None and attacker.get_attribute(AttrID.STAGE) in (
            PokemonStage.STAGE1.value, PokemonStage.STAGE2.value)

    return pred


def attacker_is_gx_or_ex():
    """"damage from Pokemon-GX and Pokemon-EX"."""
    from ptcgo.game.card_effects.pokemon import (
        is_pokemon_EX, is_pokemon_ex, is_pokemon_gx,
    )

    def pred(attacker) -> bool:
        return is_pokemon_gx(attacker) or is_pokemon_ex(attacker) \
            or is_pokemon_EX(attacker)

    return pred


def attacker_is_tag_team():
    """"damage from TAG TEAM Pokemon"."""
    from ptcgo.game.data_utils import subtypes_for

    def pred(attacker) -> bool:
        if attacker is None:
            return False
        return "TAG TEAM" in (subtypes_for(attacker.archetype_id) or [])

    return pred


def reorder_top(where: str = "top"):
    """Follow-up for a look-at body: "put them back on top of your deck in any
    order" (where="bottom" for "put the rest on the bottom"). Takes
    `(ctx, cards)` and prompts for the order -- the first card chosen ends on
    top, the way the deck reads."""
    async def effect(ctx, cards):
        looked = [card for card in (cards or []) if card is not None]
        if not looked:
            return []
        if len(looked) == 1:
            ordered = looked
        else:
            ordered = await ctx.choose_cards(
                looked, len(looked), minimum=len(looked), ordered=True,
                prompt=("Choose the order to put the cards back on top; the "
                        "first one chosen ends on top"))
            ordered = list(ordered) or looked
        place = (ctx.put_on_bottom_of_deck if where == "bottom"
                 else ctx.put_on_top_of_deck)
        for card in reversed(ordered):
            await place(card)
        return ordered
    return effect


def attach_energy_from_cards(target="choice", predicate=None,
                             distribute: bool = False):
    """Follow-up for a first part that produced cards: attach the Energy among
    them ("if any of those are Energy, attach them"). Takes
    `(ctx, cards)`, so it composes with `composed(..., on_success=...)` or
    with `mill_attack`/`look_at_top` through the outcome argument."""
    from ptcgo.game.card_effects.pokemon import is_energy_card

    def matches(card) -> bool:
        return (predicate or is_energy_card)(card)

    async def effect(ctx, cards):
        from ptcgo.game.card_effects.support_common import distribute_energy

        energies = [card for card in (cards or []) if matches(card)]
        if not energies:
            return []
        if distribute:
            # "attach them to your Pokemon in any way you like"
            return await distribute_energy(ctx, energies, ctx.my_pokemon_in_play())
        if target == "self":
            holder = ctx.source
        else:
            candidates = ctx.my_pokemon_in_play()
            if not candidates:
                return []
            holder = await ctx.choose_pokemon(
                candidates, "Choose a Pokémon to attach the Energy to")
            if holder is None:
                return []
        attached = []
        for energy in energies:
            await ctx.attach_energy(energy, holder)
            attached.append((energy, holder))
        return attached
    return effect


def move_counters_ability(count=1, side="mine", pred=None):
    """"As often as you like during your turn, you may move N damage counter(s)
    from 1 of your Pokemon to another of them" (Gengar, Alakazam).

    Returns `(effect, condition)`; the condition is the offer gate, so an
    UNLIMITED ability disappears while nothing can move. `side` is "mine" or
    "theirs"; `pred` narrows both pools."""
    def _pool(board, owner_id):
        if side == "mine":
            return board.pokemon_in_play(owner_id)
        return [pokemon for player_id in board.player_ids if player_id != owner_id
                for pokemon in board.pokemon_in_play(player_id)]

    def condition(board, player_id, pokemon) -> bool:
        owner_id = getattr(pokemon, "owning_player_id", None) or player_id
        matching = [p for p in _pool(board, owner_id) if pred is None or pred(p)]
        damaged = [p for p in matching
                   if p.get_attribute(AttrID.HP, 0) < effective_max_hp(board, p)]
        return bool(damaged) and len(matching) >= 2

    async def effect(ctx):
        pool = _pool(ctx.board, ctx.player_id)
        if side != "mine":
            pool = [p for pid in ctx.board.player_ids if pid != ctx.player_id
                    for p in ctx.board.pokemon_in_play(pid)]
        sources = [p for p in pool if (pred is None or pred(p))
                   and p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)]
        if not sources:
            return
        source = sources[0] if len(sources) == 1 else await ctx.choose_pokemon(
            sources, "Choose a Pokémon to move damage counters from")
        if source is None:
            return
        targets = [p for p in pool if p is not source
                   and (pred is None or pred(p))]
        if not targets:
            return
        dest = targets[0] if len(targets) == 1 else await ctx.choose_pokemon(
            targets, "Choose a Pokémon to move damage counters to")
        if dest is None:
            return
        await ctx.move_damage_counters(source, dest, max_count=count)

    return effect, condition


def heal_activation(amount, target_pred=None, flip=False,
                    requires_benched=False):
    """"Once during your turn, you may [flip a coin. If heads,] heal N damage
    from your Active Pokemon" (Healing Leaves, Softboiled, Victory Kiss).

    Returns `(effect, condition)`: the condition hides the offer while the
    Active has nothing to heal, so an ONCE_PER_TURN ability's slot disappears
    as soon as it is spent. `target_pred` narrows the Active (Water only,
    Evolution only); `requires_benched` is the "if this Pokemon is on your
    Bench" wording, which needs the carrier to stay off the Active spot."""
    def condition(board, player_id, pokemon) -> bool:
        if requires_benched and is_in_active_spot(pokemon):
            return False
        active = board.active_pokemon(player_id)
        return active is not None \
            and (target_pred is None or target_pred(active)) \
            and active.get_attribute(AttrID.HP, 0) < effective_max_hp(board, active)

    async def effect(ctx):
        if requires_benched and is_in_active_spot(ctx.source):
            return
        active = ctx.my_active()
        if active is None or (target_pred is not None and not target_pred(active)):
            return
        if flip:
            results = await ctx.flip_coins(1, ctx.ability.title if ctx.ability else "")
            if not (results and results[0]):
                return
        await ctx.heal(amount, active)

    return effect, condition


def on_ko_from_attack(then):
    """"If this Pokemon is Knocked Out by damage from an attack" wrapper for an
    ON_KNOCKED_OUT ability: runs `then(ctx)` only for attack damage, leaving
    ability/effect knockouts alone (Final Wish)."""
    async def effect(ctx):
        if not getattr(ctx, "ko_from_attack", False):
            return
        await then(ctx)
    return effect


def flip_protection(prevent=True, reduce=None, effects_too=False, title=None,
                    self_damage: int = 0):
    """Complete attack effect: printed damage, then flip a coin -- heads
    shields the user during the opponent's next turn. `self_damage` is the
    Rocket Tackle recoil, dealt before the flip with no W/R."""
    async def effect(ctx):
        await ctx.deal_damage()
        if self_damage:
            await ctx.deal_damage(self_damage, target=ctx.attacker,
                                  apply_modifiers=False)
        flip_title = title if title is not None else (
            ctx.ability.title if ctx.ability else "")
        results = await ctx.flip_coins(1, flip_title)
        if results and results[0]:
            await apply_protection(ctx, reduce=reduce, prevent=prevent,
                                   effects_too=effects_too)
    return effect


class AttackDebuffPassive(Passive):
    """The carrier's attacks do N less damage (dealt-side, before W/R)."""

    def __init__(self, amount):
        self.amount = amount

    def modify_damage_dealt(self, calc, carrier):
        if (calc.is_attack and calc.is_opposing
                and carrier_pokemon(carrier) is calc.attacker):
            calc.amount -= self.amount


async def apply_defender_debuff(ctx, amount, target=None):
    """Rider: `target`'s (default the Defending Pokemon) attacks do N less
    during the opponent's next turn; fizzles vs attack-effect shields."""
    target = target if target is not None else ctx.defender
    if target is None or ctx.effects_blocked(target):
        return False
    ctx.add_passive_through_opponents_turn(target, AttackDebuffPassive(amount))
    return True


def debuff_defender_attacks(amount):
    """Complete attack effect: printed damage, then "during your opponent's
    next turn, the Defending Pokemon's attacks do N less damage"."""
    async def effect(ctx):
        await ctx.deal_damage()
        await apply_defender_debuff(ctx, amount)
    return effect


async def apply_own_next_turn_boost(ctx, amount, attack_title=None,
                                    opposing_active_only=True):
    """Rider: during your next turn this Pokemon's attacks (optionally only
    `attack_title`) do +N; a turn guard keeps it off the current attack."""
    state = ctx.session.turn_state
    start = state.turn_number
    ctx.add_turn_damage_modifier(TurnDamageModifier(
        amount, ctx.player_id,
        opposing_active_only=opposing_active_only,
        expires_after_turn=start + 2,
        source_entity_id=ctx.attacker.entity_id,
        attack_title=attack_title,
        source_predicate=lambda _e: state.turn_number > start,
    ))


def boost_own_next_turn(amount, attack_title=None):
    """Complete attack effect: printed damage, then "during your next turn,
    this Pokemon's attacks do +N" (Fullmetal Impact rider when titled)."""
    async def effect(ctx):
        await ctx.deal_damage()
        await apply_own_next_turn_boost(ctx, amount, attack_title)
    return effect


class SelfAttackCostRaisePassive(Passive):
    """The carrier's attacks cost [C] N more."""

    def __init__(self, extra):
        self.extra = extra

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is not pokemon:
            return cost
        cost["Colorless"] = cost.get("Colorless", 0) + self.extra
        return cost


async def apply_defender_attack_cost_raise(ctx, extra=1, target=None):
    """Rider: `target`'s (default the Defending Pokemon) attacks cost [C]
    N more during the opponent's next turn; fizzles vs effect shields."""
    target = target if target is not None else ctx.defender
    if target is None or ctx.effects_blocked(target):
        return False
    ctx.add_passive_through_opponents_turn(
        target, SelfAttackCostRaisePassive(extra))
    return True


def raise_defender_attack_cost_next_turn(extra=1):
    """Complete attack effect: printed damage, then the Defending Pokemon's
    attacks cost [C] N more during your opponent's next turn."""
    async def effect(ctx):
        await ctx.deal_damage()
        await apply_defender_attack_cost_raise(ctx, extra)
    return effect


class SelfRetreatCostRaisePassive(Passive):
    """The carrier's retreat cost is [C] N more."""

    def __init__(self, extra):
        self.extra = extra

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is not pokemon:
            return cost
        return cost + self.extra


async def apply_defender_retreat_cost_raise(ctx, extra=1, target=None):
    """Rider: `target`'s (default the Defending Pokemon) retreat cost is N
    more during the opponent's next turn; fizzles vs effect shields."""
    target = target if target is not None else ctx.defender
    if target is None or ctx.effects_blocked(target):
        return False
    ctx.add_passive_through_opponents_turn(
        target, SelfRetreatCostRaisePassive(extra))
    return True


def raise_defender_retreat_cost_next_turn(extra=1):
    """Complete attack effect: printed damage, then the Defending Pokemon's
    retreat cost is [C] N more during your opponent's next turn."""
    async def effect(ctx):
        await ctx.deal_damage()
        await apply_defender_retreat_cost_raise(ctx, extra)
    return effect


class EnergyTypeRewritePassive(Passive):
    """"All [basic] Energy attached to <scope> provide <types> Energy instead
    of their usual types" (Steelix Rare Metal, Erika's Oddish Photosynthesis,
    Wild Growth, Chlorophyll). Read-time only: the attached cards never change.

    `modify_energy_provided` gets the Energy and its holder but not the
    Pokemon contributing the passive, and ability passives are shared
    singletons, so the carrier is recovered from the board: the in-play
    Pokemon whose ability list holds this exact passive object."""

    def __init__(self, types, protects="carrier", basic_only=False,
                 colorless_only=False, holder_types=None):
        self.types = [int(types)] if isinstance(types, int) else [int(t) for t in types]
        self.protects = protects
        self.basic_only = basic_only
        self.colorless_only = colorless_only
        self.holder_types = tuple(int(t) for t in holder_types or ())

    def _carrier(self, board):
        from ptcgo.game.content.definitions import ABILITIES_BY_ID
        for player_id in board.player_ids:
            for pokemon in board.pokemon_in_play(player_id):
                for entry in pokemon.get_attribute(AttrID.PIE_ABILITIES) or []:
                    if not isinstance(entry, dict):
                        continue
                    ability = ABILITIES_BY_ID.get(entry.get("abilityID"))
                    if ability is not None and ability.passive is self:
                        return pokemon
        return None

    def modify_energy_provided(self, options, energy, holder, board):
        if holder is None or board is None:
            return options
        carrier = self._carrier(board)
        if carrier is None or not _protects_pred(self.protects)(holder, carrier):
            return options
        if self.holder_types:
            types = {getattr(t, "value", t) for t in effective_pokemon_types(board, holder)}
            if not types.intersection(self.holder_types):
                return options
        record = EnergyTypeOverride(
            types=list(self.types),
            basic_only=self.basic_only,
            colorless_only=self.colorless_only,
        )
        return record.apply(options, energy, holder, board)


def rewrite_energy_types_passive(types, protects="carrier", basic_only=False,
                                 colorless_only=False, holder_types=None) -> Passive:
    """Continuous "all Energy attached to X provide <types> Energy instead".

    `types` is what they provide instead (repeat a type to double it);
    `protects` is 'carrier' (Energy on this Pokemon) | 'team' (Energy on any
    of your Pokemon) | callable(holder, carrier); `basic_only` drops Special
    Energy, `colorless_only` keeps cards currently providing only Colorless,
    `holder_types` keeps holders of one of those types. Example::

        Ability("Rare Metal", game_text="...",
                passive=rewrite_energy_types_passive(
                    PokemonTypes.METAL.value, basic_only=True))
    """
    return EnergyTypeRewritePassive(types, protects, basic_only=basic_only,
                                    colorless_only=colorless_only,
                                    holder_types=holder_types)


class RetreatDiscountDespiteConditionsPassive(Passive):
    """"The Retreat Cost of the Pokemon this card is attached to is C less,
    and it can retreat even if it's Asleep or Paralyzed" (Escape Board).

    Both halves are continuous, so this is one passive on the Tool: the
    discount through modify_retreat_cost, the permission through the
    retreat-only negator that legal_actions consults."""

    def __init__(self, amount=1, protects="carrier"):
        self.amount = amount
        self.protects = _protects_pred(protects)

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if not self.protects(pokemon, carrier):
            return cost
        return max(0, cost - self.amount)

    def permits_retreat_while_immobilized(self, pokemon, carrier):
        return self.protects(pokemon, carrier)


def retreat_discount_despite_conditions(amount=1, protects="carrier") -> Passive:
    """Retreat Cost -amount plus "may retreat while Asleep or Paralyzed"."""
    return RetreatDiscountDespiteConditionsPassive(amount, protects)


class RescueScarfPassive(Passive):
    """"If the Pokemon this card is attached to is Knocked Out by damage from
    an attack, put that Pokemon into your hand. (Discard all cards attached.)"
    Only the attack-damage knockout is redirected: a knockout from an effect
    still goes to the discard pile."""

    def knockout_destination(self, pokemon, carrier, from_attack=False):
        if not from_attack or carrier_pokemon(carrier) is not pokemon:
            return None
        return "hand"


def rescue_to_hand_on_attack_ko() -> Passive:
    """Rescue Scarf: the KO'd holder goes to its owner's hand."""
    return RescueScarfPassive()


def weakness_to_attacker_type(pokemon, attacker) -> bool:
    """Whether `pokemon`'s printed Weakness is one of `attacker`'s types."""
    if pokemon is None or attacker is None:
        return False
    weakness = pokemon.get_attribute(AttrID.WEAKNESS_TYPES)
    if isinstance(weakness, str):
        weakness = [int(part) for part in weakness.strip("[]").split(",") if part.strip()]
    attacker_types = attacker.get_attribute(AttrID.POKEMON_TYPES) or []
    if isinstance(attacker_types, str):
        attacker_types = [int(part) for part in attacker_types.strip("[]").split(",") if part.strip()]
    return bool(set(weakness or []) & set(attacker_types or []))


async def draw_when_damaged_with_weakness(ctx, count=3):
    """"If the Pokemon this card is attached to has Weakness to your
    opponent's Active Pokemon's type, is in the Active Spot, and is damaged by
    an attack from your opponent's Pokemon (even if it is Knocked Out), draw
    N cards" (Adversity Policy)."""
    pokemon = ctx.source
    if pokemon is None or not is_in_active_spot(pokemon):
        return
    attacker = ctx.damaged_by
    if attacker is None or attacker.owning_player_id == pokemon.owning_player_id:
        return
    if not weakness_to_attacker_type(pokemon, attacker):
        return
    await ctx.draw_cards(count)


class TeamPlasmaPassive(Passive):
    """"The Pokemon this card is attached to is a Team Plasma Pokemon"
    (Team Plasma Badge): the subtype is added while the Tool is attached, so
    it disappears with the card and never touches the printed state."""

    def __init__(self, subtype="Team Plasma"):
        self.subtype = subtype

    def modify_subtypes(self, subtypes, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon or self.subtype in subtypes:
            return subtypes
        return list(subtypes) + [self.subtype]


def team_plasma_passive(subtype="Team Plasma") -> Passive:
    """Makes the holder a Team Plasma Pokemon while attached."""
    return TeamPlasmaPassive(subtype)


def has_team_plasma(board, pokemon) -> bool:
    """Whether `pokemon` counts as a Team Plasma Pokemon right now, printed or
    granted by an attached Team Plasma Badge."""
    from ptcgo.game.session.passives import has_subtype
    return has_subtype(board, pokemon, "Team Plasma")


def cure_on_energy_attach(energy_type=None):
    """"Whenever you attach [a <type>] Energy from your hand to this Pokemon,
    remove all Special Conditions from it" (Natural Cure, Water Veil). The
    typed variants filter the trigger's attached Energy."""
    type_value = getattr(energy_type, "value", energy_type)

    async def effect(ctx):
        if ctx.energy_receiver is not ctx.source:
            return
        if type_value is not None and ctx.attached_energy is not None \
                and not energy_provides_type(ctx.attached_energy, type_value):
            return
        await ctx.cure_all_conditions(ctx.source)

    return effect


class EvolutionLockPassive(Passive):
    """"Your opponent can't evolve their <Active> Pokemon during their next
    turn" (Evolution Lock): a turn-scoped passive on the attacker.

    blocks_evolution returns True to BLOCK. The earlier version returned False
    for the opponent, so it blocked its own owner's evolutions and let the
    opponent evolve."""

    def __init__(self, opponent_id=None, only=None, active_only=False,
                 opponents_only: bool = True):
        self.opponent_id = opponent_id
        self.only = only
        self.active_only = active_only
        self.opponents_only = opponents_only

    def blocks_evolution(self, player_id, target, carrier):
        if self.opponents_only and player_id == carrier.owning_player_id:
            return False
        if self.opponent_id is not None and player_id != self.opponent_id:
            return False
        if self.active_only and not is_in_active_spot(target):
            return False
        if self.only is not None and target is not self.only:
            return False
        return True


def evolution_lock_passive(active_only=False, opponent_id=None, only=None,
                           opponents_only: bool = True) -> Passive:
    """Blocks the opponent's evolutions for the passive's lifetime."""
    return EvolutionLockPassive(opponent_id=opponent_id, only=only,
                                active_only=active_only,
                                opponents_only=opponents_only)


class SpiritLinkPassive(Passive):
    """"Your turn does not end if the Pokemon this card is attached to becomes
    M <name> ex" (Spirit Link): the one clause every Spirit Link prints."""

    def permits_turn_continue_after_mega(self, pokemon, carrier):
        return carrier_pokemon(carrier) is pokemon


def spirit_link_passive() -> Passive:
    """Keeps the turn alive through the holder's Mega Evolution."""
    return SpiritLinkPassive()
