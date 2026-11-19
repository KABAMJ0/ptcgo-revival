from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions


async def horrid_pollen(ctx):
    await ctx.deal_damage()
    heads = sum(await ctx.flip_coins(2))
    if heads == 2:
        conditions = (SpecialConditions.CONFUSED, SpecialConditions.POISONED)
    elif heads == 1:
        conditions = (SpecialConditions.ASLEEP, SpecialConditions.POISONED)
    else:
        conditions = (SpecialConditions.PARALYZED, SpecialConditions.POISONED)
    for condition in conditions:
        await ctx.apply_special_condition(ctx.defender, condition)


card = PokemonCardDef(
    guid="d09d8f6c-5049-5124-859d-448e691a3069",
    key="BP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkVenusaur.Name",
    display_name="Dark Venusaur",
    searchable_by=["Dark Venusaur", "Stage 2", "DarkVenusaur"],
    subtypes=["Stage 2"],
    collector_number=7,
    set_code="BP",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DarkIvysaur.Name",
    family_id=2,
    abilities=[
        Attack(
            title="Horrid Pollen",
            game_text="Flip 2 coins. If 1 is heads, the Defending Pok\u00e9mon is now Asleep and Poisoned. If both are heads, the Defending Pok\u00e9mon is now Confused and Poisoned. If both are tails, the Defending Pok\u00e9mon is now Paralyzed and Poisoned.",
            cost={PokemonTypes.GRASS: 3},
            damage=30,
            effect=horrid_pollen,
        ),
    ],
)
