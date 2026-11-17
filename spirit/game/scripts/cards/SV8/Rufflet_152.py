from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e7447b65-44b4-54b7-8e2e-ba4b98454ed3",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rufflet.Name",
    display_name="Rufflet",
    searchable_by=["Rufflet", "Basic", "Rufflet"],
    subtypes=["Basic"],
    collector_number=152,
    set_code="SV8",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=627,
    abilities=[
        Attack(
            title="Flap",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)