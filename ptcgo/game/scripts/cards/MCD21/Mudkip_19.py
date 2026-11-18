from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="debf360f-e490-5724-af2e-bb7478ac5683",
    key="MCD21",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mudkip.Name",
    display_name="Mudkip",
    searchable_by=["Mudkip", "Basic", "Mudkip"],
    subtypes=["Basic"],
    collector_number=19,
    set_code="MCD21",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=258,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title="Mud-Slap",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)