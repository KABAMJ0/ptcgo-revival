from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c52e67e6-21d7-502a-94a0-d0c371c15e2d",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gastly.Name",
    display_name="Gastly",
    searchable_by=["Gastly", "Basic", "Gastly"],
    subtypes=["Basic"],
    collector_number=55,
    set_code="SV4PT5",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=92,
    abilities=[
        Attack(
            title="Allure",
            game_text="Draw a card.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Will-O-Wisp",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)