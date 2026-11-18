from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7a0b778c-7593-52d6-8c0f-4b4bbc0c622a",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlackKyuremex.Name",
    display_name="Black Kyurem ex",
    searchable_by=["Black Kyurem ex", "Basic", "ex", "BlackKyuremex"],
    subtypes=["Basic", "ex"],
    collector_number=218,
    set_code="SV8",
    rarity=Rarities.Rare,
    hp=230,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    family_id=646,
    abilities=[
        Attack(
            title="Ice Age",
            game_text="If your opponent's Active Pok\u00e9mon is a Dragon Pok\u00e9mon, it is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
            effect=unimplemented,
        ),
        Attack(
            title="Black Frost",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=250,
            effect=unimplemented,
        ),
    ],
)