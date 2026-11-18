from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4ce3cfe3-b5c4-53f7-a362-a03766a59eb2",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sewaddle.Name",
    display_name="Sewaddle",
    searchable_by=["Sewaddle", "Basic", "Sewaddle"],
    subtypes=["Basic"],
    collector_number=1,
    set_code="RSV10PT5",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=540,
    abilities=[
        Attack(
            title="Bug Bite",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
    ],
)