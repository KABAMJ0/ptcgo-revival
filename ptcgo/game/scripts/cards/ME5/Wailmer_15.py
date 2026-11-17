from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b3d0739b-d0c4-5008-9132-f89d2c6a2bc6",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wailmer.Name",
    display_name="Wailmer",
    searchable_by=["Wailmer", "Basic", "Wailmer"],
    subtypes=["Basic"],
    collector_number=15,
    set_code="ME5",
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=320,
    abilities=[
        Attack(
            title="Water Gun",
            cost={PokemonTypes.WATER: 2},
            damage=40,
        ),
        Attack(
            title="Wave Splash",
            cost={PokemonTypes.WATER: 3},
            damage=80,
        ),
    ],
)