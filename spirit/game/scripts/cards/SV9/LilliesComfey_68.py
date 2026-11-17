from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a11e3c4b-adc2-5ada-85bb-dfe8cd896eee",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LilliesComfey.Name",
    display_name="Lillie's Comfey",
    searchable_by=["Lillie's Comfey", "Basic", "LilliesComfey"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="SV9",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=764,
    abilities=[
        Attack(
            title="Inviting Flowers",
            game_text="You may search your deck for any number of Basic Lillie's Pok\u00e9mon and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Fade Out",
            game_text="Put this Pok\u00e9mon and all attached cards into your hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)