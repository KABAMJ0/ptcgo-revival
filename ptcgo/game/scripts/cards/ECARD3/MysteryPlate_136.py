from ptcgo.game.data_utils import PokemonToolCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import PokemonTypes, Rarities, SpecialConditions
from ptcgo.game.card_effects.trainers import mystery_plate_healing_oasis, discard_tool_at_end_of_turn

card = PokemonToolCardDef(
    guid="80309a3f-6cbc-5966-b3af-13753e616cdd",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MysteryPlate.Name",
    display_name="Mystery Plate δ",
    searchable_by=["Mystery Plate \u03b4", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=136,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Attack(
            title="Healing Oasis",
            game_text="If your opponent has 5 or more Prizes, search your deck for up to 3 basic Energy cards, show them to your opponent, and put them into your hand. Shuffle your deck afterward. If your opponent has exactly 2 Prizes, remove all damage counters from 1 of your Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=mystery_plate_healing_oasis(),
        ),
        Ability(
            title="Mystery Plate δ",
            game_text="Discard this card at the end of your turn.",
            trigger=Triggers.END_OF_TURN,
            effect=discard_tool_at_end_of_turn(),
        ),
    ],
)
