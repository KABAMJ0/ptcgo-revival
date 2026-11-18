from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f51d184a-97f8-5a64-a908-78f2354b5e14",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Frigibax.Name",
    display_name="Frigibax",
    searchable_by=["Frigibax", "Basic", "Frigibax"],
    subtypes=["Basic"],
    collector_number=58,
    set_code="SV2",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=996,
    abilities=[
        Attack(
            title="Chilly",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)