from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="107ff3f7-be0b-5bd6-b988-b28468037856",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Purrloin.Name",
    display_name="Purrloin",
    searchable_by=["Purrloin", "Basic", "Purrloin"],
    subtypes=["Basic"],
    collector_number=135,
    set_code="SM11",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=509,
    abilities=[
        Attack(
            title="Cleaning Up",
            game_text="Discard a Pok\u00e9mon Tool card from 1 of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)