from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="aa3e2c53-e367-5685-8e2f-51c5f1cda887",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fuecoco.Name",
    display_name="Fuecoco",
    searchable_by=["Fuecoco", "Basic", "Fuecoco"],
    subtypes=["Basic"],
    collector_number=23,
    set_code="SV4",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=909,
    abilities=[
        Attack(
            title="Live Coal",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
        ),
        Attack(
            title="Ram",
            cost={PokemonTypes.FIRE: 2},
            damage=30,
        ),
    ],
)