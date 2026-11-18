from ptcgo.game.data_utils import PokemonToolCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import PokemonTypes, Rarities, SpecialConditions
from ptcgo.game.card_effects.trainers import mystery_plate_retro_cave, discard_tool_at_end_of_turn

card = PokemonToolCardDef(
    guid="2df7341b-3e56-5074-bb39-e25cf8758790",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MysteryPlate.Name",
    display_name="Mystery Plate γ",
    searchable_by=["Mystery Plate \u03b3", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=135,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Attack(
            title="Retro Cave",
            game_text="If your opponent has 5 or more Prizes, shuffle your hand into your deck and then draw 6 cards. If your opponent has exactly 2 Prizes, choose 1 of your opponent's Evolved Pokémon. Your opponent puts the top card on that Evolved Pokémon on the bottom of his or her deck. (This counts as devolving that Pokémon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=mystery_plate_retro_cave(),
        ),
        Ability(
            title="Mystery Plate γ",
            game_text="Discard this card at the end of your turn.",
            trigger=Triggers.END_OF_TURN,
            effect=discard_tool_at_end_of_turn(),
        ),
    ],
)
