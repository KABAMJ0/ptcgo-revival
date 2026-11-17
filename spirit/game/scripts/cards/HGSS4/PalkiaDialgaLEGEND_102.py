from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="417186bf-fcfa-5f26-8806-ab659d4ad2df",
    key="HGSS4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PalkiaDialgaLEGEND.Name",
    display_name="Palkia & Dialga LEGEND",
    searchable_by=["Palkia & Dialga LEGEND", "LEGEND", "PalkiaDialgaLEGEND"],
    subtypes=["LEGEND"],
    collector_number=102,
    set_code="HGSS4",
    rarity=Rarities.Common,
    hp=160,
    elements=[PokemonTypes.WATER, PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=483,
    abilities=[
        Attack(
            title="Sudden Delete",
            game_text="Choose 1 of your opponent's Benched Pok\u00e9mon. Put that Pok\u00e9mon and all cards attached to it back to your opponent's hand.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Time Control",
            game_text="Discard all Metal Energy attached to Palkia & Dialga LEGEND. Add the top 2 cards of your opponent's deck to his or her Prize cards.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)