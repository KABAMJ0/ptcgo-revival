from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5f7e6dab-18f8-5c18-af1f-699fa0cd0cd8",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Corsola.Name",
    display_name="Corsola",
    searchable_by=["Corsola", "Basic", "Corsola"],
    subtypes=["Basic"],
    collector_number=84,
    set_code="DP3",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=222,
    abilities=[
        Attack(
            title="Rally",
            game_text="Search your deck for up to 3 different types of Basic Pok\u00e9mon and put them onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Hook",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)