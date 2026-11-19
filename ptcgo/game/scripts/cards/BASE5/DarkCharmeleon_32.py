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
    guid="bb99756f-bc23-5bf6-a16b-bfb9333fcf47",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkCharmeleon.Name",
    display_name="Dark Charmeleon",
    searchable_by=["Dark Charmeleon", "Stage 1", "DarkCharmeleon"],
    subtypes=["Stage 1"],
    collector_number=32,
    set_code="BASE5",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmander.Name",
    family_id=4,
    abilities=[
        Attack(
            title="Tail Slap",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Fireball",
            game_text="Use this attack only if there are any Fire Energy cards attached to Dark Charmeleon. Flip a coin. If heads, discard 1 of those Energy cards. If tails, this attack does nothing (not even damage).",
            cost={PokemonTypes.FIRE: 3},
            damage=70,
            effect=fireball,
        ),
    ],
)