from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e38d09d1-38f1-58ab-a6cd-f35aea3b9194",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spinarak.Name",
    display_name="Spinarak",
    searchable_by=["Spinarak", "Basic", "Spinarak"],
    subtypes=["Basic"],
    collector_number=1,
    set_code="ME3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=167,
    abilities=[
        Attack(
            title="Gooey Thread",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=unimplemented,
        ),
    ],
)