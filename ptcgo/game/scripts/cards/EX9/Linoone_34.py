from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="013f6520-9423-57df-946a-fc4bd270e19c",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Linoone.Name",
    display_name="Linoone",
    searchable_by=["Linoone", "Stage 1", "Linoone"],
    subtypes=["Stage 1"],
    collector_number=34,
    set_code="EX9",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zigzagoon.Name",
    family_id=263,
    abilities=[
        Attack(
            title="Body Slam",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=unimplemented,
        ),
        Attack(
            title="Claw Swipe",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)