from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6794c4b7-8bf7-50af-be9f-b368d6fd4520",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Joltik.Name",
    display_name="Joltik",
    searchable_by=["Joltik", "Basic", "Joltik"],
    subtypes=["Basic"],
    collector_number=50,
    set_code="SV7",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=595,
    abilities=[
        Attack(
            title="Jolting Charge",
            game_text="Search your deck for up to 2 Basic Grass Energy cards and up to 2 Basic Lightning Energy cards and attach them to your Pok\u00e9mon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)