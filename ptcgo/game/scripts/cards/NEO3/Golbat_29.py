from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def screech(ctx):
    """Until the end of your next turn the Defending Pokemon takes 20 more from
    attacks."""
    if ctx.defender is not None:
        ctx.add_damage_taken_modifier(20, target=ctx.defender)


async def poison_bite(ctx):
    """Printed 10; the Defending Pokemon is Poisoned and Golbat heals half the
    damage it dealt, rounded up to a counter."""
    import math
    from ptcgo.game.attributes import SpecialConditions
    dealt = await ctx.deal_damage()
    await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED)
    if dealt > 0 and ctx.attacker is not None:
        counters = math.ceil(math.ceil(dealt / 2) / 10)
        await ctx.heal(10 * counters, ctx.attacker)

card = PokemonCardDef(
    guid="9d39b880-3ba6-5f54-ba67-bc52661792d7",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golbat.Name",
    display_name="Golbat",
    searchable_by=["Golbat", "Stage 1", "Golbat"],
    subtypes=["Stage 1"],
    collector_number=29,
    set_code="NEO3",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zubat.Name",
    family_id=41,
    abilities=[
        Attack(
            title="Screech",
            game_text="Until the end of your next turn, if an attack damages the Defending Pok\u00e9mon (after applying Weakness and Resistance), that attack does 20 more damage to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=screech,
        ),
        Attack(
            title="Poison Bite",
            game_text="If this attack damages the Defending Pok\u00e9mon, the Defending Pok\u00e9mon is now Poisoned and you remove a number of damage counters from Golbat equal to half that damage (rounded up to the nearest 10). If Golbat has fewer damage counters than that, remove all of them. Either way, the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=poison_bite,
        ),
    ],
)