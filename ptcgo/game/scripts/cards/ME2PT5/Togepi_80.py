from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0b361efd-81df-598d-a072-85f091e3cf45",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Togepi.Name",
    display_name="Togepi",
    searchable_by=["Togepi", "Basic", "Togepi"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="ME2PT5",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=175,
    abilities=[
        Attack(
            title="Pound",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)