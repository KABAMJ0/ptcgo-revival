from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4b3c05f5-b96d-5c01-8fee-09cf5cc4111f",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chespin.Name",
    display_name="Chespin",
    searchable_by=["Chespin", "Basic", "Chespin"],
    subtypes=["Basic"],
    collector_number=5,
    set_code="ME4",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=650,
    abilities=[
        Attack(
            title="Beat",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
        Attack(
            title="Spike Sting",
            cost={PokemonTypes.GRASS: 2},
            damage=30,
        ),
    ],
)