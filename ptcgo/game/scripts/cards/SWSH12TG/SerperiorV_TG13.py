from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def noble_light(ctx):
    for pokemon in ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play():
        await ctx.heal(30, pokemon)

card = PokemonCardDef(
    guid="7aba9597-78bc-5b20-a354-6ac74d5ca20f",
    key="SWSH12TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SerperiorV.Name",
    display_name="Serperior V",
    searchable_by=["Serperior V", "Basic", "V", "SerperiorV"],
    subtypes=["Basic", "V"],
    collector_number=13,
    set_code="SWSH12TG",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=497,
    abilities=[
        Attack(
            title="Noble Light",
            game_text="Heal 30 damage from each Pok\u00e9mon (both yours and your opponent's).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=noble_light,
        ),
        Attack(
            title="Solar Beam",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
        ),
    ],
)