from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a8b73098-156a-50a9-8fc3-07fb1c59457d",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianZigzagoon.Name",
    display_name="Galarian Zigzagoon",
    searchable_by=["Galarian Zigzagoon", "Basic", "GalarianZigzagoon"],
    subtypes=["Basic"],
    collector_number=130,
    set_code="ME2PT5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=263,
    abilities=[
        Attack(
            title="Gnaw",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
    ],
)