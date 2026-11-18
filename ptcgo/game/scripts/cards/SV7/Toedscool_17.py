from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="61ef19e6-3a18-56e7-a22e-d50b655576cc",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toedscool.Name",
    display_name="Toedscool",
    searchable_by=["Toedscool", "Basic", "Toedscool"],
    subtypes=["Basic"],
    collector_number=17,
    set_code="SV7",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=948,
    abilities=[
        Attack(
            title="Ram",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
        Attack(
            title="Gentle Slap",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)