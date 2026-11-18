from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="496908b9-b5b3-551d-b36f-06b29cb6f8e9",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scraggy.Name",
    display_name="Scraggy",
    searchable_by=["Scraggy", "Basic", "Scraggy"],
    subtypes=["Basic"],
    collector_number=57,
    set_code="RSV10PT5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=559,
    abilities=[
        Attack(
            title="Headbutt",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
        Attack(
            title="Invade",
            cost={PokemonTypes.DARKNESS: 2},
            damage=30,
        ),
    ],
)