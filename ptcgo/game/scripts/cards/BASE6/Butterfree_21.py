from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import gust_attack


async def _half_drain(ctx, heal_target):
    """Printed damage, then remove half of it (rounded up to the nearest 10)
    worth of damage counters from `heal_target`; a heal clamps to the damage
    actually on it ("if it has fewer, remove all of them")."""
    dealt = await ctx.deal_damage()
    if heal_target is None or dealt <= 0:
        return
    half = (dealt + 1) // 2
    await ctx.heal(((half + 9) // 10) * 10, heal_target)


async def mega_drain(ctx):
    await _half_drain(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="380a017e-d722-58a6-b55a-7ba2ff77e230",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Butterfree.Name",
    display_name="Butterfree",
    searchable_by=["Butterfree", "Stage 2", "Butterfree"],
    subtypes=["Stage 2"],
    collector_number=21,
    set_code="BASE6",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Metapod.Name",
    family_id=10,
    abilities=[
        Attack(
            title="Whirlwind",
            game_text="Your opponent switches the Defending Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon, if any. (Do the damage before switching the Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=gust_attack(opponent_chooses=True),
        ),
        Attack(
            title="Mega Drain",
            game_text="Remove a number of damage counters from Butterfree equal of half the damage done to the Defending Pok\u00e9mon (after applying Weakness and Resistance) (rounded up to the nearest 10). If Butterfree has fewer damage counters that that, remove all of them.",
            cost={PokemonTypes.GRASS: 4},
            damage=40,
            effect=mega_drain,
        ),
    ],
)