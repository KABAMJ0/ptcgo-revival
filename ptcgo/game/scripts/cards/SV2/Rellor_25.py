from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c14d80d3-533b-5802-8dab-77f0093b7fcd",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rellor.Name",
    display_name="Rellor",
    searchable_by=["Rellor", "Basic", "Rellor"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="SV2",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=953,
    abilities=[
        Attack(
            title="Bug Bite",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)