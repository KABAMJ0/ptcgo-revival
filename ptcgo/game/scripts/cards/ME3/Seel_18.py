from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cf17069f-eca7-525c-860a-2bc7a5391ea3",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seel.Name",
    display_name="Seel",
    searchable_by=["Seel", "Basic", "Seel"],
    subtypes=["Basic"],
    collector_number=18,
    set_code="ME3",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=86,
    abilities=[
        Attack(
            title="Rain Splash",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title="Wave Splash",
            cost={PokemonTypes.WATER: 2},
            damage=30,
        ),
    ],
)