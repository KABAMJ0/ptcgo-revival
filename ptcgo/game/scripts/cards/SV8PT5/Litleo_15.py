from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e4ada0df-571c-53ef-a075-475af2102e4b",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Litleo.Name",
    display_name="Litleo",
    searchable_by=["Litleo", "Basic", "Litleo"],
    subtypes=["Basic"],
    collector_number=15,
    set_code="SV8PT5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=667,
    abilities=[
        Attack(
            title="Combustion",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
        ),
        Attack(
            title="Headbutt",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)