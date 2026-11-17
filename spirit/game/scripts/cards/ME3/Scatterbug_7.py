from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bfc216ad-cdaf-5ab6-b77f-d28eb732e689",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scatterbug.Name",
    display_name="Scatterbug",
    searchable_by=["Scatterbug", "Basic", "Scatterbug"],
    subtypes=["Basic"],
    collector_number=7,
    set_code="ME3",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=664,
    abilities=[
        Attack(
            title="Gnaw",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
    ],
)