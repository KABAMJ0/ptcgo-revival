from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1a1641b8-eae1-51d4-81d8-669172d811ba",
    key="MCD17",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Popplio.Name",
    display_name="Popplio",
    searchable_by=["Popplio", "Basic", "Popplio"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="MCD17",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=728,
    abilities=[
        Attack(
            title="Pound",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title="Water Gun",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)