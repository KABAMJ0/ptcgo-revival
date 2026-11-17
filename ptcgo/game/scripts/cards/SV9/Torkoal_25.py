from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ae8b6e56-698a-5a5d-9de6-a222863e7a2b",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Torkoal.Name",
    display_name="Torkoal",
    searchable_by=["Torkoal", "Basic", "Torkoal"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="SV9",
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=324,
    abilities=[
        Attack(
            title="Live Coal",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
        ),
        Attack(
            title="Heat Blast",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
    ],
)