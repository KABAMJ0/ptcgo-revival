from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ad6d4894-96c9-5f47-a32b-5a9635e703e3",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rotom.Name",
    display_name="Rotom",
    searchable_by=["Rotom", "Basic", "Rotom"],
    subtypes=["Basic"],
    collector_number=13,
    set_code="DP5",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.COLORLESS,
    family_id=479,
    abilities=[
        Attack(
            title="Dual Trans",
            game_text="Search your discard pile for up to 2 basic Energy cards and attach them to 1 of your Pok\u00e9mon.",
            cost={},
            effect=unimplemented,
        ),
        Attack(
            title="Reflect Energy",
            game_text="Move an Energy card attached to Rotom to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)