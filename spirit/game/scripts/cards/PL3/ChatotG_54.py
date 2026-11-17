from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6587dd1a-7ae0-5c12-a1cc-b5e45998bb98",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ChatotG.Name",
    display_name="Chatot G",
    searchable_by=["Chatot G", "Basic", "SP", "ChatotG"],
    subtypes=["Basic", "SP"],
    collector_number=54,
    set_code="PL3",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=441,
    abilities=[
        Ability(
            title="Disrupting Spy",
            game_text="Once during your turn, when you put Chatot G from your hand onto your Bench, you may look at the top 4 cards of your opponent's deck. Put them back on top of your opponent's deck in any order.",
            effect=unimplemented,
        ),
        Attack(
            title="Search and Escape",
            game_text="Search your deck for a Trainer card, show it to your opponent, and put it into your hand. Put Chatot G and all cards attached to it on top of your deck. Shuffle your deck afterward.",
            cost={},
            effect=unimplemented,
        ),
    ],
)