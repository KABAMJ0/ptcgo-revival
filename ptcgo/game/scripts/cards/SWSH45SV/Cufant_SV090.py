from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9ffb97a4-ac56-5d71-8e85-e95e0baf1fce",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cufant.Name",
    display_name="Cufant",
    searchable_by=["Cufant", "Basic", "Cufant"],
    subtypes=["Basic"],
    collector_number=90,
    set_code="SWSH45SV",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=878,
    abilities=[
        Attack(
            title="Strength",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)