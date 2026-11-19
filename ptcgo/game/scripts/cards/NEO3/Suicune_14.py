from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.attributes import SpecialConditions


async def aurora_wave(ctx):
    """Printed 30; both heads Paralyzes, exactly one heads Asleeps."""
    await ctx.deal_damage()
    flips = await ctx.flip_coins(2, "Aurora Wave")
    heads = sum(1 for flip in flips if flip)
    if heads == 2:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)
    elif heads == 1:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.ASLEEP)

card = PokemonCardDef(
    guid="19403144-d856-5231-8f84-5105ce2c6b7b",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Suicune.Name",
    display_name="Suicune",
    searchable_by=["Suicune", "Basic", "Suicune"],
    subtypes=["Basic"],
    collector_number=14,
    set_code="NEO3",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=245,
    abilities=[
        Ability(
            title="Crystal Body",
            game_text="Prevent all effects of your opponent's attacks, other than damage, done to Suicune. This power stops working while Suicune is Asleep, Confused, or Paralyzed.",
            effect=unimplemented,
        ),
        Attack(
            title="Aurora Wave",
            game_text="Flip 2 coins. If both are heads, the Defending Pok\u00e9mon is now Paralyzed. If only 1 is heads, the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 3},
            damage=30,
            effect=aurora_wave,
        ),
    ],
)