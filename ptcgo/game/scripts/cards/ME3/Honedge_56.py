from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="523d6c51-b2d5-5186-a64c-57fb49fb7432",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Honedge.Name",
    display_name="Honedge",
    searchable_by=["Honedge", "Basic", "Honedge"],
    subtypes=["Basic"],
    collector_number=56,
    set_code="ME3",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=679,
    abilities=[
        Attack(
            title="Cut",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)