from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="287e559b-a1c6-5544-92ae-e7faf412b1cc",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cetoddle.Name",
    display_name="Cetoddle",
    searchable_by=["Cetoddle", "Basic", "Cetoddle"],
    subtypes=["Basic"],
    collector_number=64,
    set_code="SV10",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    family_id=974,
    abilities=[
        Attack(
            title="Gentle Slap",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Frost Smash",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1},
            damage=80,
        ),
    ],
)