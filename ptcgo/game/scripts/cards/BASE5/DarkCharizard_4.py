from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.attacks_common import (
    damage_counters_on, damage_per, damage_per_extra_energy, flip_gate)
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.attributes import AttrID


def _fire_energy(card):
    return energy_provides_type(card, PokemonTypes.FIRE.value)


async def continuous_fireball(ctx):
    """One coin per Fire Energy on Dark Charizard: 50 per heads, then discard
    that many Fire Energy."""
    fire = [e for e in ctx.attached_energies(ctx.attacker) if _fire_energy(e)]
    if not fire:
        await ctx.deal_damage(0)
        return
    flips = await ctx.flip_coins(len(fire), "Continuous Fireball")
    heads = sum(1 for flip in flips if flip)
    if heads:
        await ctx.deal_damage(50 * heads)
    discarded = 0
    for _ in range(min(heads, len(fire))):
        gone = await ctx.discard_energy_from(ctx.attacker, 1, predicate=_fire_energy,
                                             prompt="Discard a Fire Energy")
        if not gone:
            break
        discarded += 1


async def fireball(ctx):
    """Only usable with a Fire Energy attached; on heads discard one for the
    printed 70, on tails the attack does nothing at all."""
    if not any(_fire_energy(e) for e in ctx.attached_energies(ctx.attacker)):
        return
    heads = await ctx.flip_coins(1, "Fireball")
    if not (heads and heads[0]):
        return
    await ctx.discard_energy_from(ctx.attacker, 1, predicate=_fire_energy,
                                  prompt="Discard a Fire Energy")
    await ctx.deal_damage()


async def playing_with_fire(ctx):
    """Only usable with a Fire Energy attached: heads discards one and does 30
    plus 20 more, tails the attack does nothing."""
    if not any(_fire_energy(e) for e in ctx.attached_energies(ctx.attacker)):
        return
    heads = await ctx.flip_coins(1, "Playing with Fire")
    if not (heads and heads[0]):
        return
    gone = await ctx.discard_energy_from(ctx.attacker, 1, predicate=_fire_energy,
                                         prompt="Discard a Fire Energy")
    await ctx.deal_damage(50 if gone else 30)

card = PokemonCardDef(
    guid="f4a35e33-60e1-5d5f-a907-c61b4fccb2ac",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkCharizard.Name",
    display_name="Dark Charizard",
    searchable_by=["Dark Charizard", "Stage 2", "DarkCharizard"],
    subtypes=["Stage 2"],
    collector_number=4,
    set_code="BASE5",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DarkCharmeleon.Name",
    family_id=4,
    abilities=[
        Attack(
            title="Nail Flick",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Continuous Fireball",
            game_text="Flip a number of coins equal to the number of Fire Energy cards attached to Dark Charizard. This attack does 50 damage times the number of heads. Discard a number of Fire Energy cards attached to Dark Charizard equal to the number of heads.",
            cost={PokemonTypes.FIRE: 2},
            damage=50,
            damage_operator="x",
            effect=continuous_fireball,
        ),
    ],
)