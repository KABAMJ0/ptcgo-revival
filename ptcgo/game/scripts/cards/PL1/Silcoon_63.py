from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="305d29d9-6de4-5163-a783-b2c635b7469b",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Silcoon.Name",
    display_name="Silcoon",
    searchable_by=["Silcoon", "Stage 1", "Silcoon"],
    subtypes=["Stage 1"],
    collector_number=63,
    set_code="PL1",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wurmple.Name",
    family_id=265,
    abilities=[
        Attack(
            title="Ascension",
            game_text="Search your deck for a card that evolves from Silcoon and put it onto Silcoon. (This counts as evolving Silcoon.) Shuffle your deck afterward.",
            cost={},
            effect=unimplemented,
        ),
        Attack(
            title="Sticky String",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
    ],
)