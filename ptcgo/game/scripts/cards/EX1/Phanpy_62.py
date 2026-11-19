from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def trembler(ctx):
    """Heads: 10 to the Defending Pokemon and it is now Paralyzed."""
    results = await ctx.flip_coins(1, "Trembler")
    if not (results and results[0]):
        return
    await ctx.deal_damage(10, apply_modifiers=None)
    await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)

card = PokemonCardDef(
    guid="9750173e-0783-5898-a10c-6c8d73ae628b",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Phanpy.Name",
    display_name="Phanpy",
    searchable_by=["Phanpy", "Basic", "Phanpy"],
    subtypes=["Basic"],
    collector_number=62,
    set_code="EX1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=231,
    abilities=[
        Attack(
            title="Stampede",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Trembler",
            game_text="Flip a coin. If heads, this attack does 10 damage to each Defending Pok\u00e9mon, and each Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            effect=trembler,
        ),
    ],
)