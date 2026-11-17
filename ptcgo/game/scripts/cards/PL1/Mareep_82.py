from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ed4e9d48-b721-5670-bba1-39a77bade3a3",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mareep.Name",
    display_name="Mareep",
    searchable_by=["Mareep", "Basic", "Mareep"],
    subtypes=["Basic"],
    collector_number=82,
    set_code="PL1",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=179,
    abilities=[
        Attack(
            title="Minor Errand-Running",
            game_text="Search your deck for a basic Energy card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.",
            cost={},
            effect=unimplemented,
        ),
        Attack(
            title="Expand",
            game_text="During your opponent's next turn, any damage done to Mareep by attacks is reduced by 10 (after applying Weakness and Resistance).",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            effect=unimplemented,
        ),
    ],
)