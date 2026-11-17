from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c5dd0c83-c472-532c-8d2c-675a93c28521",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Morelull.Name",
    display_name="Morelull",
    searchable_by=["Morelull", "Basic", "Morelull"],
    subtypes=["Basic"],
    collector_number=8,
    set_code="SV8",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=755,
    abilities=[
        Attack(
            title="Attach",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)