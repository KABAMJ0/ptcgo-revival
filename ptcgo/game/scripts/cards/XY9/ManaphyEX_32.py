from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def _heal_own_bench(ctx):
    await ctx.deal_damage()
    for pokemon in ctx.my_bench():
        await ctx.heal(30, pokemon)


card = PokemonCardDef(
    guid="376194e2-8ffa-59aa-97c9-cf87d13861ce",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ManaphyEX.Name",
    display_name="Manaphy-EX",
    searchable_by=["Manaphy-EX", "Basic", "EX", "ManaphyEX"],
    subtypes=["Basic", "EX"],
    collector_number=32,
    set_code="XY9",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=490,
    abilities=[
        Ability(
            title="Aqua Tube",
            game_text="Each of your Pok\u00e9mon that has any Water Energy attached to it has no Retreat Cost.",
            effect=unimplemented,
        ),
        Attack(
            title="Mineral Pump",
            game_text="Heal 30 damage from each of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2},
            damage=60,
            effect=_heal_own_bench,
        ),
    ],
)