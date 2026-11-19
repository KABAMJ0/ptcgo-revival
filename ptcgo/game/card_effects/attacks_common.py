"""Reusable attack-effect factories: flips, scaling, snipes, conditions,
energy-discard costs, locks, counter placement.

Every factory returns an `async def effect(ctx)` for Attack(effect=...);
damage/base None = the attack's printed damage; `also=` chains a follow-up
coroutine run after the factory's own work.
"""

import random
from typing import Optional

from ptcgo.game.attributes import (
    AbilityTypes,
    AttrID,
    CLIENT_SPECIAL_CONDITION_NAMES,
    PokemonStage,
    PokemonTypes,
    SpecialConditions,
    TrainerType,
)
from ptcgo.game.data_utils import Attack, def_for, has_rule_box, is_pokemon_v, subtypes_for
from ptcgo.game.card_effects.passives_common import (
    condition_immunity_passive,
    no_weakness_passive,
    weakens_own_attacks_passive,
)
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.session.effects import is_special_energy
from ptcgo.game.session.legal_actions import energy_provided_count

_TOOL_TYPES = (TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value)
_ENERGY_SCOPES = ("self", "attacker", "defender", "opponent_active", "my_active",
                  "mine", "opponent", "both")


# ----------------------------------------------------------------------
# Shared internals
# ----------------------------------------------------------------------

def _printed(ctx) -> int:
    return getattr(ctx.ability, "damage", 0) or 0


def _title(ctx) -> str:
    return ctx.ability.title if ctx.ability else ""


def _resolve_count(ctx, count_or_fn) -> int:
    return count_or_fn(ctx) if callable(count_or_fn) else int(count_or_fn)


def _in_play(ctx, side: str) -> list:
    if side == "both":
        return ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play()
    if side in ("opponent", "theirs"):
        return ctx.opponent_pokemon_in_play()
    return ctx.my_pokemon_in_play()


def _bench_of(ctx, side: str) -> list:
    if side == "both":
        return ctx.my_bench() + ctx.opponent_bench()
    return ctx.opponent_bench() if side in ("opponent", "theirs") else ctx.my_bench()


def _side_pid(ctx, side: str) -> str:
    return ctx.opponent_id if side in ("opponent", "theirs") else ctx.player_id


def _resolve_target(ctx, target_fn):
    if callable(target_fn):
        return target_fn(ctx)
    return ctx.attacker if target_fn == "self" else ctx.defender


async def _finish(ctx, self_damage: int, also):
    if self_damage:
        await ctx.deal_damage(self_damage, target=ctx.attacker, apply_modifiers=False)
    if also is not None:
        await also(ctx)


def _attack_ability_entries(pokemon) -> list:
    return [e for e in (pokemon.get_attribute(AttrID.PIE_ABILITIES) or [])
            if isinstance(e, dict) and e.get("abilityType") == "Attack"
            and e.get("abilityID")]


def _provided_of_type(energy, type_value: int) -> int:
    info = energy.get_attribute(AttrID.ENERGY_INFO) or {}
    best = max((option.count(type_value)
                for option in info.get("options", [])), default=0)
    return best or 1


# ----------------------------------------------------------------------
# Count helpers (each returns count_fn(ctx) -> int, or a card predicate)
# ----------------------------------------------------------------------

def count_energy(scope: str = "self", energy_type=None, cards: bool = False):
    """Attached Energy on a scope; counts PROVIDED amounts (Double Turbo = 2)
    unless cards=True. energy_type filters/counts one type (Aurora matches)."""
    if scope not in _ENERGY_SCOPES:
        raise ValueError(f"count_energy: unknown scope '{scope}'")
    type_value = getattr(energy_type, "value", energy_type)

    def count(ctx) -> int:
        if scope in ("self", "attacker"):
            pool = [ctx.attacker]
        elif scope in ("defender", "opponent_active"):
            pool = [ctx.opponent_active()]
        elif scope == "my_active":
            pool = [ctx.my_active()]
        else:
            pool = _in_play(ctx, scope)
        total = 0
        for pokemon in pool:
            if pokemon is None:
                continue
            for energy in ctx.attached_energies(pokemon):
                if type_value is None:
                    total += 1 if cards else energy_provided_count(energy)
                elif energy_provides_type(energy, type_value):
                    total += 1 if cards else _provided_of_type(energy, type_value)
        return total
    return count


def count_bench(side: str = "mine", pred=None):
    """Benched Pokemon on a side ('mine'|'opponent'|'both'), optionally filtered."""
    def count(ctx) -> int:
        return sum(1 for p in _bench_of(ctx, side) if pred is None or pred(p))
    return count


def count_discard(side: str = "mine", pred=None):
    """Cards in a discard pile ('mine'|'opponent'|'both'), optionally filtered."""
    def count(ctx) -> int:
        piles = [ctx.player_id, ctx.opponent_id] if side == "both" \
            else [_side_pid(ctx, side)]
        return sum(1 for pid in piles for c in ctx.discard_pile(pid)
                   if pred is None or pred(c))
    return count


def count_prizes_taken(side: str = "mine"):
    def count(ctx) -> int:
        return ctx.prizes_taken(_side_pid(ctx, side))
    return count


def count_prizes_remaining(side: str = "mine"):
    def count(ctx) -> int:
        area = ctx.board.find_player_area(_side_pid(ctx, side), "prizePile")
        return len(area.children) if area else 0
    return count


def damage_counters_on(target_fn="self"):
    """Damage counters on a Pokemon ('self'|'defender'|callable(ctx)->pokemon)."""
    def count(ctx) -> int:
        target = _resolve_target(ctx, target_fn)
        if target is None:
            return 0
        return max(0, (ctx.max_hp(target) - target.get_attribute(AttrID.HP, 0)) // 10)
    return count


def count_hand(side: str = "mine"):
    def count(ctx) -> int:
        return ctx.hand_size(_side_pid(ctx, side))
    return count


def count_in_play(side: str = "mine", pred=None):
    """In-play Pokemon (Active + Bench) on a side, optionally filtered."""
    def count(ctx) -> int:
        return sum(1 for p in _in_play(ctx, side) if pred is None or pred(p))
    return count


def has_attack_titled(title: str):
    """Card predicate: the card's definition carries an attack named `title`
    (Mad Party / Let's All Rollout counting)."""
    def pred(card) -> bool:
        definition = def_for(getattr(card, "archetype_id", None) or "")
        for ability in getattr(definition, "abilities", None) or []:
            if getattr(ability, "title", None) != title:
                continue
            if isinstance(ability, Attack) or getattr(ability, "ability_type", None) \
                    in (AbilityTypes.ATTACK, AbilityTypes.NON_DAMAGING_ATTACK):
                return True
        return False
    return pred


# ----------------------------------------------------------------------
# Flip family
# ----------------------------------------------------------------------

def flip_damage(coins: int = 1, per_heads: int = 0, base: Optional[int] = None,
                bonus: int = 0, bonus_per_heads: int = 0,
                until_tails: bool = False, coins_from=None,
                require_all: bool = False, tails_self_damage: int = 0,
                self_damage: int = 0, also=None):
    """Coin-flip damage: heads*per_heads (base defaults 0), or printed base +
    heads*bonus_per_heads, or base+bonus gated on ALL heads (require_all;
    without a bonus the whole base needs all heads). coins_from=count_fn
    flips one coin per counted thing; until_tails uses one coin screen.
    tails_self_damage hits the attacker once when any coin lands tails."""
    async def effect(ctx):
        if until_tails:
            heads = await ctx.flip_until_tails(_title(ctx))
            total, tails = heads + 1, 1
        else:
            total = _resolve_count(ctx, coins_from) if coins_from is not None else coins
            results = await ctx.flip_coins(total, _title(ctx)) if total > 0 else []
            heads = sum(1 for r in results if r)
            tails = total - heads
        base_val = (base or 0) if per_heads \
            else (base if base is not None else _printed(ctx))
        if require_all:
            success = total > 0 and tails == 0
            # The per-heads term still lands on an all-heads run ("30 plus 10
            # more for each heads, if all of them are heads" paid nothing for
            # the heads before this).
            amount = base_val + heads * per_heads + bonus if success \
                else (base_val if bonus else 0)
        else:
            amount = base_val + heads * (per_heads + bonus_per_heads) \
                + (bonus if heads else 0)
        if amount > 0:
            await ctx.deal_damage(amount)
        if tails_self_damage and tails > 0:
            await ctx.deal_damage(tails_self_damage, target=ctx.attacker,
                                  apply_modifiers=False)
        await _finish(ctx, self_damage, also)
    return effect


def flip_damage_condition(coins: int = 1, per_heads: int = 0,
                          base: Optional[int] = None, min_heads: int = 1,
                          condition=None, self_condition=None, also=None):
    """"Flip N coins. This attack does X damage for each heads. If <min_heads>
    of them are heads, the Defending Pokemon is now <condition>."

    One flip feeds both halves: the damage and the condition read the SAME
    coins, which flip_damage + condition_attack cannot do (each flips)."""
    async def effect(ctx):
        results = await ctx.flip_coins(coins, _title(ctx)) if coins > 0 else []
        heads = sum(1 for r in results if r)
        base_val = (base or 0) if per_heads \
            else (base if base is not None else _printed(ctx))
        amount = base_val + heads * per_heads
        if amount > 0:
            await ctx.deal_damage(amount)
        if heads >= min_heads:
            if condition is not None:
                await ctx.apply_special_condition(ctx.defender, condition)
            if self_condition is not None:
                await ctx.apply_special_condition(ctx.attacker, self_condition)
        if also is not None:
            await also(ctx)
    return effect


def flip_damage_table(steps: dict, coins: int = 3, base: Optional[int] = None):
    """"Flip 3 coins. If 1 is heads, 10 more; if 2, 30 more; if all, 60 more."

    `steps` maps head count -> extra damage; a count it does not name adds
    nothing. `base` defaults to the printed damage."""
    async def effect(ctx):
        results = await ctx.flip_coins(coins, _title(ctx))
        heads = sum(1 for r in results if r)
        base_val = base if base is not None else _printed(ctx)
        amount = base_val + steps.get(heads, 0)
        if amount > 0:
            await ctx.deal_damage(amount)
    return effect


def flip_or_nothing(coins: int = 1, then=None):
    """"Flip a coin. If tails, this attack does nothing." — any tails is an
    early return; all heads runs `then(ctx)` (default: printed damage)."""
    async def effect(ctx):
        results = await ctx.flip_coins(coins, _title(ctx))
        if not results or not all(results):
            return
        if then is None:
            await ctx.deal_damage()
        else:
            await then(ctx)
    return effect


def flip_bonus(bonus: int, coins: int = 1):
    """Printed damage, +bonus when every flipped coin is heads."""
    return flip_damage(coins=coins, bonus=bonus, require_all=True)


# ----------------------------------------------------------------------
# Scaling damage
# ----------------------------------------------------------------------

def damage_per(count_fn, per: int, base: int = 0, cap: Optional[int] = None,
               self_damage: int = 0, also=None):
    """base + per * count_fn(ctx) damage to the opponent's Active (cap optional)."""
    async def effect(ctx):
        amount = base + per * max(0, count_fn(ctx))
        if cap is not None:
            amount = min(amount, cap)
        if amount > 0:
            await ctx.deal_damage(amount)
        await _finish(ctx, self_damage, also)
    return effect


# ----------------------------------------------------------------------
# Snipe / spread
# ----------------------------------------------------------------------

def snipe_attack(amount, pool="bench", count: int = 1,
                 side: str = "opponent", also_base: bool = False,
                 apply_modifiers: Optional[bool] = None, optional: bool = False,
                 self_damage: int = 0, also=None, prompt: Optional[str] = None):
    """Deal `amount` to `count` chosen Pokemon (pool 'bench'|'any'|predicate).
    apply_modifiers None = engine auto (W/R only when the target is the
    opponent's Active); also_base deals printed damage to the Active first.

    `amount` may be a callable taking the ctx, for the printings whose snipe
    scales with a count ("this attack does 30 damage for each Energy attached to
    that Pokemon"): it is evaluated once per resolution, like `damage_per`."""

    def _amount(ctx):
        return amount(ctx) if callable(amount) else amount

    async def effect(ctx):
        if pool == "any":
            candidates = _in_play(ctx, side)
        elif pool == "bench":
            candidates = _bench_of(ctx, side)
        else:
            candidates = [p for p in _in_play(ctx, side) if pool(p)]
        picks = []
        if candidates:
            value = _amount(ctx)
            if len(candidates) <= count and not optional:
                picks = candidates
            else:
                text = prompt or (f"Choose a Pokémon to take {value} damage"
                                  if count == 1 else
                                  f"Choose {count} Pokémon to take {value} damage")
                picks = await ctx.choose_cards(
                    candidates, count, minimum=0 if optional else None, prompt=text)
        queue_shield = len(picks) + int(also_base) == 1
        if also_base:
            await ctx.deal_damage(queue_shield=queue_shield)
        for target in picks:
            await ctx.deal_damage(_amount(ctx), target=target,
                                    apply_modifiers=apply_modifiers,
                                    queue_shield=queue_shield)
        await _finish(ctx, self_damage, also)
    return effect


def spread_damage(amount: int, side: str = "opponent",
                  include_active: bool = False, own_bench: bool = False,
                  also_base: bool = False, also=None):
    """Deal `amount` to every Benched Pokemon on `side` ('opponent'|'mine'|
    'both'); include_active adds that side's Active(s), own_bench adds your
    bench to an opponent-side spread. Bench damage takes no W/R (engine auto)."""
    async def effect(ctx):
        targets = {p.entity_id: p for p in _bench_of(ctx, side)}
        if own_bench and side != "mine":
            targets.update((p.entity_id, p) for p in ctx.my_bench())
        if include_active:
            actives = []
            if side in ("opponent", "theirs", "both"):
                actives.append(ctx.opponent_active())
            if side in ("mine", "both"):
                actives.append(ctx.my_active())
            targets.update((p.entity_id, p) for p in actives if p is not None)
        queue_shield = len(targets) + int(also_base) == 1
        if also_base:
            await ctx.deal_damage(queue_shield=queue_shield)
        for target in targets.values():
            await ctx.deal_damage(amount, target=target, apply_modifiers=None,
                                  queue_shield=queue_shield)
        if also is not None:
            await also(ctx)
    return effect


def damage_all_opponents(amount: int, also=None):
    """Deal `amount` to each of the opponent's Pokemon (Active included)."""
    return spread_damage(amount, side="opponent", include_active=True, also=also)


# ----------------------------------------------------------------------
# Conditional bonus + predicates
# ----------------------------------------------------------------------

def bonus_if(cond_fn, bonus: int, base: Optional[int] = None,
             else_nothing: bool = False, self_damage: int = 0, also=None):
    """Printed (or base) damage, +bonus when cond_fn(ctx) holds; else_nothing
    makes the whole attack deal 0 when the condition fails."""
    async def effect(ctx):
        base_val = base if base is not None else _printed(ctx)
        met = bool(cond_fn(ctx))
        amount = base_val + bonus if met else (0 if else_nothing else base_val)
        if amount > 0:
            await ctx.deal_damage(amount)
        await _finish(ctx, self_damage, also)
    return effect


def active_is(pred):
    """cond_fn: the opponent's Active exists and matches `pred(pokemon)`."""
    def cond(ctx) -> bool:
        active = ctx.opponent_active()
        return active is not None and bool(pred(active))
    return cond


def defender_is_v(ctx) -> bool:
    d = ctx.defender
    return d is not None and is_pokemon_v(d.archetype_id)


def defender_is_gx(ctx) -> bool:
    d = ctx.defender
    return d is not None and "GX" in subtypes_for(d.archetype_id)


def defender_is_vmax(ctx) -> bool:
    d = ctx.defender
    return d is not None and "VMAX" in subtypes_for(d.archetype_id)


def defender_has_rule_box(ctx) -> bool:
    d = ctx.defender
    return d is not None and has_rule_box(d.archetype_id)


def defender_has_condition(condition):
    """cond_fn: the opponent's Active already has the Special Condition."""
    name = CLIENT_SPECIAL_CONDITION_NAMES[condition]

    def cond(ctx) -> bool:
        d = ctx.defender
        return d is not None and \
            name in (d.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])
    return cond


def named_in_play(*names, side: str = "mine", require_all: bool = False):
    """cond_fn: Pokemon with these names (EVOLUTION_LOGIC_NAME) are in play."""
    def cond(ctx) -> bool:
        present = {p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
                   for p in _in_play(ctx, side)}
        wanted = set(names)
        return wanted <= present if require_all else bool(wanted & present)
    return cond


def has_tool(pokemon) -> bool:
    """Card predicate: a Tool is attached (compose: active_is(has_tool))."""
    return any(c.get_attribute(AttrID.TRAINER_TYPE) in _TOOL_TYPES
               for c in pokemon.children)


def has_damage(target_fn="defender"):
    """cond_fn: the target ('self'|'defender'|callable) has damage on it."""
    def cond(ctx) -> bool:
        target = _resolve_target(ctx, target_fn)
        return target is not None and \
            target.get_attribute(AttrID.HP, 0) < ctx.max_hp(target)
    return cond


def opponent_prizes_taken_at_least(n: int):
    def cond(ctx) -> bool:
        return ctx.prizes_taken(ctx.opponent_id) >= n
    return cond


# ----------------------------------------------------------------------
# Energy-discard costs
# ----------------------------------------------------------------------

def self_energy_discard_attack(count: Optional[int] = None,
                               all_energy: bool = False, energy_type=None,
                               before_damage: bool = False,
                               then_damage: Optional[int] = None, also=None):
    """Discard own attached Energy (count, or all_energy=True) around the
    printed (or then_damage) damage; before_damage follows the printed order."""
    if count is None and not all_energy:
        raise ValueError("self_energy_discard_attack: pass count= or all_energy=True")
    type_value = getattr(energy_type, "value", energy_type)
    pred = (lambda c: energy_provides_type(c, type_value)) \
        if type_value is not None else None

    async def _discard(ctx):
        await ctx.discard_energy_from(
            ctx.attacker, 99 if all_energy else count, predicate=pred,
            prompt="Choose Energy to discard from this Pokémon")

    async def effect(ctx):
        if before_damage:
            await _discard(ctx)
            await ctx.deal_damage(then_damage)
        else:
            await ctx.deal_damage(then_damage)
            await _discard(ctx)
        if also is not None:
            await also(ctx)
    return effect


def discard_opponent_energy_attack(count: int = 1, special_only: bool = False,
                                   after_damage: bool = True,
                                   damage: Optional[int] = None, also=None):
    """Printed (or damage) damage + discard Energy from the opponent's Active;
    the discard no-ops when the target is shielded from attack effects."""
    pred = is_special_energy if special_only else None

    async def _discard(ctx):
        target = ctx.opponent_active()
        if target is None or ctx.effects_blocked(target):
            return
        await ctx.discard_energy_from(
            target, count, predicate=pred,
            prompt="Choose Energy to discard from the Defending Pokémon")

    async def effect(ctx):
        if after_damage:
            await ctx.deal_damage(damage)
            await _discard(ctx)
        else:
            await _discard(ctx)
            await ctx.deal_damage(damage)
        if also is not None:
            await also(ctx)
    return effect


# ----------------------------------------------------------------------
# Special-condition attacks (supersedes card_effects.pokemon.condition_attack)
# ----------------------------------------------------------------------

def condition_attack(*conditions, flip: bool = False, coins: int = 1,
                     min_heads: int = 1, tails_conditions=(),
                     tails_self_conditions=(), always_conditions=(),
                     heads_bonus_damage: int = 0, self_conditions=(),
                     both_actives: bool = False, no_retreat: bool = False,
                     counters: int = 1, checkup_coins: int = 1,
                     damage: Optional[int] = None, also=None):
    """Printed damage + Special Conditions on the Defending Pokemon; flip=True
    gates `conditions`/self_conditions/no_retreat/heads_bonus_damage on
    min_heads heads (tails_conditions on failure, always_conditions always).

    `tails_self_conditions` is the mirror wording "if tails, YOUR Active
    Pokemon is now X": those land on the attacker, not the defender."""
    async def effect(ctx):
        success = True
        if flip:
            results = await ctx.flip_coins(coins, _title(ctx))
            success = sum(1 for r in results if r) >= min_heads
        base_val = damage if damage is not None else _printed(ctx)
        amount = base_val + (heads_bonus_damage if success else 0)
        if amount > 0:
            await ctx.deal_damage(amount)
        applied = list(always_conditions) + \
            (list(conditions) if success else list(tails_conditions))
        for condition in applied:
            await ctx.apply_special_condition(
                ctx.defender, condition,
                checkup_coins=checkup_coins, poison_counters=counters)
            if both_actives:
                await ctx.apply_special_condition(
                    ctx.attacker, condition,
                    checkup_coins=checkup_coins, poison_counters=counters)
        if not success:
            for condition in tails_self_conditions:
                await ctx.apply_special_condition(
                    ctx.attacker, condition,
                    checkup_coins=checkup_coins, poison_counters=counters)
        if success:
            for condition in self_conditions:
                await ctx.apply_special_condition(
                    ctx.attacker, condition,
                    checkup_coins=checkup_coins, poison_counters=counters)
            if no_retreat:
                defender = ctx.defender
                if defender is not None and not ctx.effects_blocked(defender):
                    ctx.lock_retreat(defender)
        if also is not None:
            await also(ctx)
    return effect


def condition_if(cond_fn, *conditions, target: str = "defender",
                 damage: Optional[int] = None, checkup_coins: int = 1,
                 also=None):
    """"If <board or Pokemon condition>, the Defending Pokemon is now
    <conditions>" — applies the conditions only when `cond_fn(ctx)` holds.

    condition_attack applies unconditionally, so this is the gate it lacks
    ("if this Pokemon has any Plasma Energy attached", "if the Defending
    Pokemon is a Pokemon ex", "if Nidoran is on your bench"). Printed damage
    first; pass damage=0 for a pure rider."""
    async def effect(ctx):
        base_val = damage if damage is not None else _printed(ctx)
        if base_val > 0:
            await ctx.deal_damage(base_val)
        if cond_fn(ctx):
            holder = ctx.attacker if target in ("self", "attacker") else ctx.defender
            for condition in conditions:
                await ctx.apply_special_condition(
                    holder, condition, checkup_coins=checkup_coins)
        if also is not None:
            await also(ctx)
    return effect


def condition_bonus_attack(bonus: int, *required_conditions,
                           base: Optional[int] = None, also=None):
    """"If the Defending Pokemon is already <condition>, this attack does
    `bonus` more damage." Checks before the hit; applies nothing itself."""
    names = [CLIENT_SPECIAL_CONDITION_NAMES[c] for c in required_conditions]

    async def effect(ctx):
        base_val = base if base is not None else _printed(ctx)
        defender = ctx.defender
        current = (defender.get_attribute(AttrID.SPECIAL_CONDITIONS) or []) \
            if defender is not None else []
        met = bool(names) and all(n in current for n in names)
        amount = base_val + (bonus if met else 0)
        if amount > 0:
            await ctx.deal_damage(amount)
        if also is not None:
            await also(ctx)
    return effect


def _energy_type_value(energy_type):
    """Normalizes a type given as a PokemonTypes member, its client value or a
    bare name ("Metal", "Fire"); None means any type."""
    if energy_type is None:
        return None
    if isinstance(energy_type, PokemonTypes):
        return energy_type.value
    if isinstance(energy_type, str):
        member = PokemonTypes.__members__.get(energy_type.upper())
        if member is not None:
            return member.value
        raise ValueError(f"unknown Energy type {energy_type!r}")
    return energy_type


def extra_energy_beyond_cost(ctx, energy_type=None) -> int:
    """"Extra Energy attached (in addition to this attack's cost)": the
    attacker's attached Energy of `energy_type` minus what this attack costs in
    it (Colorless cost counts for any type)."""
    attacker = ctx.attacker
    if attacker is None:
        return 0
    type_value = _energy_type_value(energy_type)
    attached = sum(1 for energy in ctx.attached_energies(attacker)
                   if type_value is None or energy_provides_type(energy, type_value))
    cost = 0
    for cost_type, count in (getattr(ctx.ability, "cost", None) or {}).items():
        value = getattr(cost_type, "value", cost_type)
        if value in (PokemonTypes.COLORLESS.value, PokemonTypes.UNSET.value) \
                or value == type_value:
            cost += count
    return attached - cost


def extra_energy_attached(required: int, energy_type=None):
    """"If this Pokemon has at least N extra Energy attached ..." condition."""
    def cond(ctx) -> bool:
        return extra_energy_beyond_cost(ctx, energy_type) >= required
    return cond


def bonus_if_extra_energy(bonus: int, required: int = 1, energy_type=None,
                          base: Optional[int] = None, also=None):
    """"If this Pokemon has at least N extra Energy attached (in addition to
    this attack's cost), this attack does X more damage." """
    return bonus_if(extra_energy_attached(required, energy_type), bonus,
                    base=base, also=also)


def damage_per_extra_energy(per_energy: int, energy_type=None,
                            cap: Optional[int] = None, base: Optional[int] = None,
                            also=None):
    """"This attack does X more damage for each extra <type> Energy attached to
    this Pokemon (in addition to this attack's cost)" — `cap` caps the bonus,
    not the total."""
    async def effect(ctx):
        extra = max(0, extra_energy_beyond_cost(ctx, energy_type))
        bonus = extra * per_energy
        if cap is not None:
            bonus = min(bonus, cap)
        base_val = base if base is not None else _printed(ctx)
        amount = base_val + bonus
        if amount > 0:
            await ctx.deal_damage(amount)
        if also is not None:
            await also(ctx)
    return effect


def bonus_if_condition_then_cure(bonus: int, base: Optional[int] = None,
                                target: str = "defender", also=None):
    """"If the Defending Pokemon is affected by a Special Condition, this attack
    does N more damage. Then, remove all Special Conditions from it."
    target="self" is the "if this Pokemon is affected ... from this Pokemon"."""
    async def effect(ctx):
        holder = ctx.attacker if target == "self" else ctx.defender
        if holder is None:
            return
        afflicted = bool(holder.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])
        base_val = base if base is not None else _printed(ctx)
        amount = base_val + (bonus if afflicted else 0)
        if amount > 0:
            await ctx.deal_damage(amount)
        if afflicted:
            await ctx.cure_all_conditions(holder)
        if also is not None:
            await also(ctx)
    return effect


def move_counters_attack(count: Optional[int] = None, dest: str = "defender",
                         damage: Optional[int] = None):
    """"Move [all] N damage counters from any of your Pokemon to the Defending
    Pokemon" — printed damage first, then the relocation."""
    async def effect(ctx):
        await ctx.deal_damage(damage)
        sources = [p for p in ctx.my_pokemon_in_play()
                   if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)]
        if not sources:
            return
        source = sources[0] if len(sources) == 1 else await ctx.choose_pokemon(
            sources, "Choose a Pokémon to move the damage counters from")
        if source is None:
            return
        if dest == "defender":
            target_pokemon = ctx.defender
        else:
            target_pokemon = await ctx.choose_pokemon(
                ctx.opponent_pokemon_in_play(),
                "Choose a Pokémon to move the damage counters to")
        if target_pokemon is None:
            return
        await ctx.move_damage_counters(source, target_pokemon, max_count=count)
    return effect


# ----------------------------------------------------------------------
# Recoil / mill
# ----------------------------------------------------------------------

def recoil_attack(self_damage: int, damage: Optional[int] = None, also=None):
    """Printed (or damage) damage; the attacker then damages itself (no W/R)."""
    async def effect(ctx):
        await ctx.deal_damage(damage)
        await ctx.deal_damage(self_damage, target=ctx.attacker,
                              apply_modifiers=False)
        if also is not None:
            await also(ctx)
    return effect


def mill_attack(count: int, opponent: bool = True,
                then_damage: Optional[int] = None, also=None):
    """Printed (or then_damage) damage, then discard the top `count` cards of
    a deck (opponent's by default)."""
    async def effect(ctx):
        await ctx.deal_damage(then_damage)
        pid = ctx.opponent_id if opponent else ctx.player_id
        milled = ctx.deck_top(count, player_id=pid)
        if milled:
            await ctx.discard_cards(milled)
        if also is not None:
            await also(ctx)
        # The milled cards are the signal for "if any of those are Energy, ...".
        return milled
    return effect


def mill_scaled_damage(mill_count: int, per: int, pred=None, base: int = 0,
                       also=None):
    """Discard the top `mill_count` of YOUR deck; damage = base + per for each
    discarded card matching `pred`."""
    async def effect(ctx):
        cards = ctx.deck_top(mill_count)
        await ctx.discard_cards(cards)
        matched = sum(1 for c in cards if pred is None or pred(c))
        amount = base + per * matched
        if amount > 0:
            await ctx.deal_damage(amount)
        if also is not None:
            await also(ctx)
    return effect


# ----------------------------------------------------------------------
# Attack-lock helpers (runtime helpers, not factories)
# ----------------------------------------------------------------------

def lock_all_attacks(ctx, pokemon):
    """Locks every printed attack on own `pokemon` through its user's next
    turn (Cross Fusion Strike's blanket self-lock)."""
    for entry in _attack_ability_entries(pokemon):
        ctx.session.turn_state.lock_attack(pokemon.entity_id, entry["abilityID"])


def choose_attack_lock(damage: Optional[int] = None, through: str = "opponent"):
    """Printed (or `damage`) damage, then the opponent picks one of their
    Active's attacks and that attack is locked for their next turn ("Choose 1
    of your opponent's Active Pokemon's attacks. That Pokemon can't use that
    attack during your opponent's next turn.")."""
    async def effect(ctx):
        await ctx.deal_damage(damage)
        defender = ctx.defender
        if defender is None or ctx.effects_blocked(defender):
            return
        from ptcgo.game.session.passives import attacks_of

        candidates = [(defender, attack) for attack in attacks_of(defender)
                      if getattr(attack, "ability_id", None)]
        if not candidates:
            return
        chosen = await ctx.choose_attack_to_copy(
            candidates,
            "Choose 1 of your opponent's Active Pokémon's attacks")
        if chosen is None:
            return
        attack = chosen[1]
        state = ctx.session.turn_state
        window = 1 if through == "opponent" else 0
        state.attack_locks[(defender.entity_id, attack.ability_id)] = \
            state.turn_number + window
    return effect


def lock_defender_attacks(ctx, defender=None) -> bool:
    """"The Defending Pokemon can't attack during your opponent's next turn";
    no-ops (False) on an effect-shielded target."""
    target = defender if defender is not None else ctx.defender
    if target is None or ctx.effects_blocked(target):
        return False
    state = ctx.session.turn_state
    for entry in _attack_ability_entries(target):
        state.attack_locks[(target.entity_id, entry["abilityID"])] = \
            state.turn_number + 1
    return True


# ----------------------------------------------------------------------
# Damage-counter placement
# ----------------------------------------------------------------------

def place_counters(count_or_fn, target: str = "opponent_active", also=None):
    """Put damage counters (raw, no W/R; effect-shield gated by the engine):
    target 'opponent_active'|'choose_any_opponent'|'each_opponent'|'self'|
    'choose_own'; count_or_fn is an int or count_fn(ctx)."""
    if target not in ("opponent_active", "choose_any_opponent", "each_opponent",
                      "self", "choose_own"):
        raise ValueError(f"place_counters: unknown target '{target}'")

    async def effect(ctx):
        count = _resolve_count(ctx, count_or_fn)
        placed = 0
        if count > 0:
            if target == "opponent_active":
                if ctx.defender is not None:
                    await ctx.deal_damage(count * 10, target=ctx.defender,
                                          as_counters=True)
                    placed = count
            elif target == "choose_any_opponent":
                placed = await ctx.place_damage_counters(
                    count, ctx.opponent_pokemon_in_play())
            elif target == "each_opponent":
                for pokemon in ctx.opponent_pokemon_in_play():
                    await ctx.deal_damage(count * 10, target=pokemon,
                                          as_counters=True)
                    placed += count
            elif target == "self":
                await ctx.deal_damage(count * 10, target=ctx.attacker,
                                      as_counters=True)
                placed = count
            else:  # choose_own
                placed = await ctx.place_damage_counters(
                    count, ctx.my_pokemon_in_play())
        if also is not None:
            await also(ctx)
        # Counters that actually landed are the "if you placed any" signal.
        return placed
    return effect


# ----------------------------------------------------------------------
# Discard-for-bonus + misc
# ----------------------------------------------------------------------

def discard_for_bonus(source: str = "hand", predicate=None, max_count: int = 1,
                      per: int = 0, flat: int = 0, optional: bool = True,
                      base: Optional[int] = None, also=None,
                      prompt: Optional[str] = None):
    """Discard up to `max_count` cards (from 'hand' or 'self-energy'), then
    deal printed (or base) + per*discarded + (flat if any discarded)."""
    if source not in ("hand", "self-energy"):
        raise ValueError(f"discard_for_bonus: unknown source '{source}'")

    async def effect(ctx):
        if source == "hand":
            pool = [c for c in ctx.hand() if predicate is None or predicate(c)]
        else:
            pool = [c for c in ctx.attached_energies(ctx.attacker)
                    if predicate is None or predicate(c)]
        picked = await ctx.choose_cards(
            pool, max_count, minimum=0 if optional else None,
            prompt=prompt or "Choose cards to discard") if pool else []
        await ctx.discard_cards(picked)
        base_val = base if base is not None else _printed(ctx)
        amount = base_val + per * len(picked) + (flat if picked else 0)
        if amount > 0:
            await ctx.deal_damage(amount)
        if also is not None:
            await also(ctx)
    return effect


def smokescreen_attack(damage: Optional[int] = None, also=None):
    """Printed (or damage) damage; "during your opponent's next turn, if the
    Defending Pokemon tries to attack, your opponent flips a coin. If tails,
    that attack doesn't happen" (Smokescreen / Sand Attack / Blinding Beam).
    The rider no-ops versus an attack-effect-shielded target."""
    async def effect(ctx):
        await ctx.deal_damage(damage)
        defender = ctx.defender
        if defender is not None and not ctx.effects_blocked(defender):
            ctx.require_attack_flip(defender)
        if also is not None:
            await also(ctx)
    return effect


def reduce_defender_attacks(amount: int, damage: Optional[int] = None):
    """Printed (or `damage`) damage, then the Defending Pokemon's own attacks do
    `amount` less during the opponent's next turn ("any damage done by attacks
    from the Defending Pokemon is reduced by N").

    `protect_next_turn` is the opposite direction: it shields the target from
    incoming hits, while this one weakens the hits the target throws."""
    async def effect(ctx):
        await ctx.deal_damage(damage)
        defender = ctx.defender
        if defender is None:
            return
        ctx.add_passive_through_opponents_turn(
            defender, weakens_own_attacks_passive(amount))
    return effect


def discard_defender_tools_then_damage(damage: Optional[int] = None):
    """"Before doing damage, discard all Pokemon Tools from your opponent's
    Active Pokemon": the order matters, so the tools leave first and the
    printed damage lands on a defender that no longer holds them."""
    async def effect(ctx):
        defender = ctx.defender
        if defender is not None:
            tools = [child for child in defender.children
                     if child.get_attribute(AttrID.TRAINER_TYPE) is not None]
            if tools:
                await ctx.discard_cards(tools)
        await ctx.deal_damage(damage)
    return effect


def no_weakness_next_turn(damage: Optional[int] = None):
    """Printed (or `damage`) damage, then the attacker has no Weakness during
    the opponent's next turn ("During your opponent's next turn, this Pokemon
    has no Weakness"). The shield is a temporary passive, so it ends with the
    turn window the same way a protection rider does."""
    async def effect(ctx):
        await ctx.deal_damage(damage)
        if ctx.attacker is None:
            return
        ctx.add_passive_through_opponents_turn(
            ctx.attacker, no_weakness_passive())
    return effect


def identity_swap_from_deck(named: str, prompt: str = ""):
    """Search your deck for another `<named>` and switch it with this Pokemon,
    keeping everything on it ("Any cards attached to Ditto, damage counters,
    Special Conditions, and effects on it are now on the new Pokemon").

    The swap itself is `ctx.identity_swap`, the same one Nanu and Ogre's Mask
    use, so attachments, damage, conditions and turn stamps all transfer."""
    want = named.strip().lower()

    def matches(card) -> bool:
        definition = def_for(getattr(card, "archetype_id", "") or "")
        return (getattr(definition, "display_name", "") or "").strip().lower() == want

    async def effect(ctx):
        pool = [card for card in ctx.deck() if matches(card)]
        if not pool:
            return
        picked = await ctx.choose_cards(
            pool, 1, minimum=1,
            prompt=prompt or f"Choose another {named} from your deck")
        if not picked or ctx.source is None:
            return
        await ctx.identity_swap(ctx.source, picked[0])
        await ctx.shuffle_deck()

    return effect


def heal_self_damage_dealt(damage: Optional[int] = None,
                           cap: Optional[int] = None):
    """Printed (or `damage`) damage, then heal the attacker for the damage it
    actually dealt ("Heal from this Pokemon the same amount of damage you did
    to your opponent's Active Pokemon"). Deal_damage returns the final amount
    after Weakness/Resistance and interception, which is exactly that."""
    async def effect(ctx):
        dealt = await ctx.deal_damage(damage)
        if ctx.attacker is None or dealt <= 0:
            return
        await ctx.heal(min(dealt, cap) if cap is not None else dealt,
                       target=ctx.attacker)
    return effect


def random_card_to_deck(damage: Optional[int] = None, destination: str = "deck",
                        reveal: bool = True, count: int = 1):
    """Printed (or `damage`) damage, then `count` random cards leave the
    opponent's hand for their deck, revealed ("Choose a random card from your
    opponent's hand. Your opponent reveals that card and shuffles it into his
    or her deck"). `count` is for the "for each heads" printings; the pick is
    always random, never chosen.

    `destination` is part of the signature the queue asked for and every
    printing in the corpus says "deck", so any other value is refused rather
    than guessed at."""
    if destination != "deck":
        raise ValueError(
            f"random_card_to_deck: only destination='deck' exists in the corpus, "
            f"got {destination!r}")

    async def effect(ctx):
        await ctx.deal_damage(damage)
        hand = ctx.hand(ctx.opponent_id)
        if not hand or count <= 0:
            return
        cards = random.sample(hand, min(count, len(hand)))
        if reveal:
            await ctx.reveal_cards(cards)
        await ctx.shuffle_into_deck(cards, ctx.opponent_id)
    return effect


async def discard_random_from_hand(ctx, player_id: Optional[str] = None,
                                   count: int = 1) -> list:
    """Discards `count` random cards from a player's hand (reveals via the
    public-pile discard bracket); returns the discarded cards."""
    pid = player_id or ctx.player_id
    hand = ctx.hand(pid)
    if not hand or count <= 0:
        return []
    picks = random.sample(hand, min(count, len(hand)))
    await ctx.discard_cards(picks)
    return picks


# ----------------------------------------------------------------------
# Damage-pipeline riders (need their own deal_damage flags)
# ----------------------------------------------------------------------

def ignore_modifier_attack(ignore_weakness: bool = False,
                           ignore_resistance: bool = False,
                           ignore_target_effects: bool = False,
                           damage: Optional[int] = None):
    """"This attack's damage isn't affected by <weakness/resistance/effects>":
    printed (or damage) damage with the named pipeline stages skipped."""
    async def effect(ctx):
        await ctx.deal_damage(damage, ignore_weakness=ignore_weakness,
                              ignore_resistance=ignore_resistance,
                              ignore_target_effects=ignore_target_effects)
    return effect


def lock_self_attack(damage: Optional[int] = None):
    """"During your next turn, this Pokemon can't attack" (also "can't use
    attacks"): printed damage, then every printed attack on the user locks."""
    async def effect(ctx):
        await ctx.deal_damage(damage)
        if ctx.attacker is not None:
            lock_all_attacks(ctx, ctx.attacker)
    return effect


def no_retreat_attack(damage: Optional[int] = None, also=None):
    """"The Defending Pokemon can't retreat during your opponent's next
    turn": printed damage plus the retreat lock."""
    async def effect(ctx):
        await ctx.deal_damage(damage)
        defender = ctx.defender
        if defender is not None and not ctx.effects_blocked(defender):
            ctx.lock_retreat(defender)
        if also is not None:
            await also(ctx)
    return effect


def flip_defender_lock_attack(damage: Optional[int] = None, coins: int = 1):
    """Printed damage; flip -- all heads locks the Defending Pokemon's
    attacks through its next turn."""
    async def effect(ctx):
        await ctx.deal_damage(damage)
        results = await ctx.flip_coins(coins, _title(ctx))
        if results and all(results):
            lock_defender_attacks(ctx)
    return effect


def flip_attack_and_retreat_lock(damage: Optional[int] = None, coins: int = 1):
    """"Flip a coin. If heads, until the end of your opponent's next turn the
    Defending Pokemon can't attack or retreat" — the flip-gated twin of the
    non-flip _lock_defender_attacks_and_retreat."""
    async def effect(ctx):
        await ctx.deal_damage(damage)
        results = await ctx.flip_coins(coins, _title(ctx))
        if not (results and all(results)):
            return
        lock_defender_attacks(ctx)
        defender = ctx.defender
        if defender is not None and not ctx.effects_blocked(defender):
            ctx.lock_retreat(defender)
    return effect


def flip_endure_attack(damage: Optional[int] = None, through: str = "opponent",
                       hp_floor: int = 10):
    """"Flip a coin. If heads, during your opponent's next turn, if this
    Pokemon would be Knocked Out by damage from an attack, it is not Knocked
    Out and its remaining HP becomes 10."

    through="own" is the "until the end of your next turn" wording."""
    from ptcgo.game.card_effects.passives_common import guts_survive_passive

    async def effect(ctx):
        await ctx.deal_damage(damage)
        results = await ctx.flip_coins(1, _title(ctx))
        if not (results and results[0]):
            return
        attacker = ctx.attacker
        if attacker is None:
            return
        passive = guts_survive_passive(hp_floor=hp_floor, flip=False)
        if through == "own":
            ctx.add_passive_through_own_next_turn(attacker, passive)
        else:
            ctx.add_passive_through_opponents_turn(attacker, passive)
    return effect


def heal_dealt_attack(damage: Optional[int] = None):
    """"Heal from this Pokemon the same amount of damage you did to your
    opponent's Active Pokemon"."""
    async def effect(ctx):
        dealt = await ctx.deal_damage(damage)
        if dealt > 0 and ctx.attacker is not None:
            await ctx.heal(dealt, ctx.attacker)
    return effect


def energy_move_attack(count: int = 1, energy_type=None,
                       damage: Optional[int] = None):
    """"Move an Energy from this Pokemon to N of your Benched Pokemon":
    printed damage, then relocate up to `count` attached Energy."""
    type_value = getattr(energy_type, "value", energy_type)

    async def effect(ctx):
        await ctx.deal_damage(damage)
        attacker = ctx.attacker
        if attacker is None:
            return
        pool = [energy for energy in ctx.attached_energies(attacker)
                if type_value is None or energy_provides_type(energy, type_value)]
        if not pool:
            return
        picks = pool if len(pool) <= count else await ctx.choose_cards(
            pool, count, prompt="Choose Energy to move to your Benched Pokémon")
        moved = []
        for energy in picks:
            bench = ctx.my_bench()
            if not bench:
                break
            target = await ctx.choose_pokemon(
                bench, "Choose a Pokémon to move the Energy to")
            if target is not None:
                await ctx.move_energy(energy, target)
                moved.append(energy)
        # The moved Energy is the signal for a second move gated on the first.
        return moved
    return effect


def flip_discard_opponent_energy(damage: Optional[int] = None, count: int = 1,
                                 scope: str = "active", coins: int = 1,
                                 energy_pred=None):
    """"Flip a coin. If heads, discard an Energy from your opponent's Active
    Pokemon" — printed (or `damage`) damage, one coin, then the discard.

    The body is `trainers.discard_energy_opponent`, shared with the Trainer
    cards of the same wording."""
    from ptcgo.game.card_effects.trainers import discard_energy_opponent

    async def effect(ctx):
        results = await ctx.flip_coins(coins, _title(ctx))
        if not (results and all(results)):
            if damage is not None:
                await ctx.deal_damage(damage)
            return
        await discard_energy_opponent(
            count=count, scope=scope, energy_pred=energy_pred, damage=damage)(ctx)
    return effect


def discard_random_hand_attack(count: int = 1, opponent: bool = True,
                               damage: Optional[int] = None):
    """Printed damage, then discard `count` random cards from a hand."""
    async def effect(ctx):
        await ctx.deal_damage(damage)
        pid = ctx.opponent_id if opponent else ctx.player_id
        await discard_random_from_hand(ctx, pid, count)
    return effect


# ----------------------------------------------------------------------
# Flip gates (riders with no damage of their own)
# ----------------------------------------------------------------------

def flip_gate(then, coins: int = 1):
    """Flip `coins`; on all heads run `then(ctx)` (a following rider)."""
    async def effect(ctx):
        results = await ctx.flip_coins(coins, _title(ctx))
        if results and all(results):
            await then(ctx)
    return effect


def flip_choice(heads: int, tails: int):
    """Flip a coin: heads deals `heads`, tails deals `tails`."""
    async def effect(ctx):
        results = await ctx.flip_coins(1, _title(ctx))
        amount = heads if (results and results[0]) else tails
        if amount > 0:
            await ctx.deal_damage(amount)
    return effect


# ----------------------------------------------------------------------
# Extra predicates for conditional bonuses
# ----------------------------------------------------------------------

def stadium_in_play_cond(ctx) -> bool:
    return ctx.stadium_in_play() is not None


def hand_sizes_equal(ctx) -> bool:
    return ctx.hand_size(ctx.player_id) == ctx.hand_size(ctx.opponent_id)


def defender_has_any_condition(ctx) -> bool:
    defender = ctx.defender
    return defender is not None and \
        bool(defender.get_attribute(AttrID.SPECIAL_CONDITIONS))


def defender_is_ex(ctx) -> bool:
    defender = ctx.defender
    if defender is None:
        return False
    return any(subtype.lower() == "ex"
               for subtype in subtypes_for(defender.archetype_id))


def defender_is_ex_or_v(ctx) -> bool:
    return defender_is_v(ctx) or defender_is_ex(ctx)


def self_has_energy_of_type(energy_type):
    """cond_fn: the attacker has an attached Energy providing that type."""
    type_value = getattr(energy_type, "value", energy_type)

    def cond(ctx) -> bool:
        attacker = ctx.attacker
        if attacker is None:
            return False
        return any(energy_provides_type(energy, type_value)
                   for energy in ctx.attached_energies(attacker))
    return cond


def defender_is_evolved(ctx) -> bool:
    defender = ctx.defender
    if defender is None:
        return False
    return any(subtype in ("Stage 1", "Stage 2", "VMAX", "BREAK")
               for subtype in subtypes_for(defender.archetype_id))


def defender_retreat_cost(ctx) -> int:
    from ptcgo.game.session.passives import effective_retreat_cost
    defender = ctx.defender
    return effective_retreat_cost(ctx.board, defender) if defender else 0


def bench_has_damage_counters(ctx) -> bool:
    return any(ctx.max_hp(pokemon) - pokemon.get_attribute(AttrID.HP, 0) > 0
               for pokemon in ctx.my_bench())


# ----------------------------------------------------------------------
# Deck / discard utility riders
# ----------------------------------------------------------------------

def evolve_from_deck_attack(damage: Optional[int] = None):
    """"Search your deck for a card that evolves from this Pokemon and put it
    onto this Pokemon to evolve it. Then, shuffle your deck." """
    async def effect(ctx):
        await ctx.deal_damage(damage)
        attacker = ctx.attacker
        if attacker is None:
            return
        candidates = _evolve_from_deck_candidates(ctx, attacker, None)
        picks = await ctx.search_deck(
            (lambda card: card in candidates), count=1, minimum=0,
            prompt="Choose an Evolution card for this Pokémon",
        )
        if picks:
            await ctx.evolve_pokemon(attacker, picks[0])
        await ctx.shuffle_deck()
    return effect


def reveal_hand_attack(damage: Optional[int] = None, opponent: bool = True):
    """"Your opponent reveals their hand"; printed damage, then the reveal."""
    async def effect(ctx):
        await ctx.deal_damage(damage)
        await ctx.reveal_hand(ctx.opponent_id if opponent else ctx.player_id)
    return effect


def discard_stadium_attack(damage: Optional[int] = None, optional: bool = False,
                           bonus: int = 0):
    """"Discard a Stadium in play" as an attack rider; optional gates it on a
    yes/no and `bonus` is extra damage when the discard happened."""
    async def effect(ctx):
        if ctx.stadium_in_play() is None:
            await ctx.deal_damage(damage)
            return
        if optional and not await ctx.ask_yes_no("Discard the Stadium in play?"):
            await ctx.deal_damage(damage)
            return
        await ctx.discard_stadium()
        await ctx.deal_damage((damage or 0) + bonus if bonus else damage)
    return effect


def lock_chosen_defender_attack(damage: Optional[int] = None):
    """"Choose 1 of the Defending Pokemon's attacks. That Pokemon can't use
    that attack during your opponent's next turn." """
    async def effect(ctx):
        await ctx.deal_damage(damage)
        defender = ctx.defender
        if defender is None or ctx.effects_blocked(defender):
            return
        entries = [entry for entry in _attack_ability_entries(defender)
                   if entry.get("abilityID")]
        if not entries:
            return
        from ptcgo.game.content.definitions import ABILITIES_BY_ID
        choices = [ABILITIES_BY_ID.get(entry["abilityID"]) for entry in entries]
        choices = [ability for ability in choices if ability is not None]
        if not choices:
            return
        chosen = choices[0] if len(choices) == 1 else \
            await ctx.choose_attack_to_copy(choices, "Choose an attack to lock")
        if chosen is None:
            return
        state = ctx.session.turn_state
        state.attack_locks[(defender.entity_id, chosen.ability_id)] = \
            state.turn_number + 1
    return effect


def search_bench_as_basic(names, count, prompt):
    """"Search your deck for <names> and put up to `count` of them onto your
    Bench. Shuffle your deck afterward. Treat the new Benched Pokemon as
    Basic Pokemon." (Anorith, Omanyte, Ninjask)

    The stage override covers Benched evolutions put out this way, so
    Basic-only effects (Fossil-style searches, Curse Powder) see them as
    Basic until they leave play."""
    wanted = {name.lower() for name in names}

    async def effect(ctx):
        picks = await ctx.search_deck(
            lambda card: (getattr(def_for(card.archetype_id), "display_name", "") or "").lower() in wanted,
            count=count, minimum=0, prompt=prompt, slot_prompt="Your Bench",
        )
        existing = {pokemon.entity_id for pokemon in ctx.my_bench()}
        benched = False
        for card in picks:
            benched = await ctx.bench_pokemon(card) or benched
        if benched:
            for pokemon in ctx.my_bench():
                if pokemon.entity_id not in existing:
                    ctx.set_pokemon_stage(pokemon, PokemonStage.BASIC)
        if picks:
            await ctx.shuffle_deck()
    return effect


def poison_defender_on_evolve(counters=1):
    """"When you play this Pokemon from your hand to evolve 1 of your Pokemon,
    you may choose 1 of the Defending Pokemon. That Pokemon is now Poisoned.
    Put N damage counters instead of 1 on it between turns" (Crobat)."""
    async def effect(ctx):
        defender = ctx.defender
        if defender is None:
            return
        if not await ctx.ask_yes_no("Poison your opponent's Active Pokémon?"):
            return
        await ctx.apply_special_condition(
            defender, SpecialConditions.POISONED, poison_counters=counters)
    return effect


def condition_immunity_pollen_shield(conditions=None):
    """"During your opponent's next turn, this Pokemon can't become <conditions>":
    printed damage, then a condition-immunity passive through the opponent's turn."""
    async def effect(ctx):
        await ctx.deal_damage()
        ctx.add_passive_through_opponents_turn(
            ctx.attacker, condition_immunity_passive(conditions))
    return effect


def _evolve_from_deck_candidates(ctx, pokemon, predicate):
    """Deck cards that evolve directly from `pokemon`.

    `evolves_from` matches anything in the evolution family (a Stage 2 counts
    as evolving from the Basic), which is right for "evolves from" wording but
    wrong here: the card goes ONTO this Pokemon, so only the direct next stage
    qualifies -- matched by stage, since the corpus does not carry a printed
    `evolves_from` for every era."""
    from ptcgo.game.content.definitions import evolves_from
    logic_name = pokemon.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
    if not logic_name:
        return []
    stage = pokemon.get_attribute(AttrID.STAGE)
    matches = [card for card in ctx.deck()
               if evolves_from(getattr(card, "archetype_id", None) or "", logic_name)
               and (stage is None or card.get_attribute(AttrID.STAGE) == stage + 1)]
    if predicate is not None:
        matches = [card for card in matches if predicate(card)]
    return matches


def evolve_from_deck(predicate=None, target="chosen", bench_only=False,
                     damage=None):
    """"Search your deck for a card that evolves from <one of your Pokemon>
    and put it onto that Pokemon to evolve it. Then, shuffle your deck."

    `target="self"` evolves the source Pokemon (evolve_from_deck_attack's
    shape without the attacker assumption); `target="chosen"` picks one of
    your Pokemon in play, `bench_only=True` narrowing to the Bench.
    `predicate` narrows the evolution card itself (a named evolution)."""
    async def effect(ctx):
        await ctx.deal_damage(damage)
        if target == "self":
            pokemon = ctx.source if isinstance(ctx.source, PokemonEntity) else ctx.attacker
        else:
            pool = ctx.my_bench() if bench_only else ctx.my_pokemon_in_play()
            # Offer only Pokemon whose evolution is actually in the deck: a
            # pick with nothing to find is a wasted action, and the AI takes
            # the first option.
            pool = [pokemon for pokemon in pool
                    if _evolve_from_deck_candidates(ctx, pokemon, predicate)]
            if not pool:
                return
            pokemon = pool[0] if len(pool) == 1 else await ctx.choose_pokemon(
                pool, "Choose a Pokémon to evolve")
        if pokemon is None:
            return
        picks = await ctx.search_deck(
            (lambda card: card in _evolve_from_deck_candidates(ctx, pokemon, predicate)),
            count=1, minimum=0, prompt="Choose an Evolution card",
        )
        if picks:
            await ctx.evolve_pokemon(pokemon, picks[0])
        await ctx.shuffle_deck()
    return effect


def evolve_each_from_deck(predicate=None, target_pred=None, max_targets=None,
                          damage=None):
    """"For each of your Benched Basic Pokemon, search your deck for a card
    that evolves from that Pokemon and put it onto that Pokemon to evolve it.
    Then, shuffle your deck." One search per target, one shuffle at the end."""
    async def effect(ctx):
        await ctx.deal_damage(damage)
        targets = [pokemon for pokemon in ctx.my_bench()
                   if target_pred is None or target_pred(pokemon)]
        if max_targets is not None:
            targets = targets[:max_targets]
        for pokemon in targets:
            candidates = _evolve_from_deck_candidates(ctx, pokemon, predicate)
            if not candidates:
                continue
            picks = await ctx.choose_cards(
                candidates, 1, minimum=0, prompt="Choose an Evolution card")
            if picks:
                await ctx.evolve_pokemon(pokemon, picks[0])
        await ctx.shuffle_deck()
    return effect


def _play_kind_predicate(kinds):
    from ptcgo.game.card_effects.trainers import (
        is_item_card, is_special_energy, is_stadium_card, is_supporter_card,
        is_tool_card, is_trainer_card,
    )
    table = {
        "item": is_item_card,
        "supporter": is_supporter_card,
        "stadium": is_stadium_card,
        "tool": is_tool_card,
        "trainer": is_trainer_card,
        "special_energy": is_special_energy,
        "energy": lambda card: card.get_attribute(AttrID.CARD_TYPE) == CardType.ENERGY.value,
    }
    chosen = [table[kind] for kind in kinds if kind in table]
    if "all" in kinds:
        return lambda card: True
    return lambda card: any(predicate(card) for predicate in chosen)


def lock_opponent_plays(*kinds, damage=None, flip=False, coins=1):
    """"Your opponent can't play any <kinds> cards from their hand during their
    next turn" (Disconnect, Pitch-Dark, Chaos Wheel).

    `kinds` are "item", "supporter", "stadium", "tool", "trainer",
    "special_energy", "energy" or "all"."""
    async def effect(ctx):
        # flip_coins returns a LIST of results; `not [False]` is False, so the
        # gate has to read the coins rather than the coroutine's truthiness.
        results = await ctx.flip_coins(coins) if flip else []
        await ctx.deal_damage(damage)
        if flip and not all(results):
            return
        ctx.lock_plays(ctx.opponent_id, _play_kind_predicate(kinds))

    return effect


def lock_opponent_evolutions(damage=None, defending_only=False):
    """"During your opponent's next turn, they can't evolve their <Active>
    Pokemon" — a turn-scoped passive on the attacker carried through the
    opponent's turn."""
    from ptcgo.game.card_effects.passives_common import evolution_lock_passive

    async def effect(ctx):
        await ctx.deal_damage(damage)
        ctx.add_passive_through_opponents_turn(
            ctx.attacker,
            evolution_lock_passive(
                opponent_id=ctx.opponent_id,
                only=ctx.defender if defending_only else None,
            ),
        )

    return effect
