from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4d89de8b-6dee-5c2f-9f4f-83bfcee16bdf",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Finneon.Name",
    display_name="Finneon",
    searchable_by=["Finneon", "Basic", "Finneon"],
    subtypes=["Basic"],
    collector_number=35,
    set_code="SV7",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=456,
    abilities=[
        Attack(
            title="Sprinkle Water",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
    ],
)