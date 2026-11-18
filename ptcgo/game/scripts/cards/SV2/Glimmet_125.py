from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bb60da25-bedc-5e20-aa37-bd4d313349bd",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Glimmet.Name",
    display_name="Glimmet",
    searchable_by=["Glimmet", "Basic", "Glimmet"],
    subtypes=["Basic"],
    collector_number=125,
    set_code="SV2",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=969,
    abilities=[
        Attack(
            title="Rock Throw",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
        ),
    ],
)