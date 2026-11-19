from ptcgo.game.data_utils import PokemonToolCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import PokemonTypes, Rarities, SpecialConditions
from ptcgo.game.card_effects.trainers import mystery_plate_desert_burn, discard_tool_at_end_of_turn

card = PokemonToolCardDef(
    guid="515fe3e5-53e1-55f4-a1f8-bd47e4158edd",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MysteryPlate.Name",
    display_name="Mystery Plate α",
    searchable_by=["Mystery Plate \u03b1", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=133,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Attack(
            title="Desert Burn",
            game_text="If your opponent has 5 or more Prizes, search your deck for a Trainer card, show it to your opponent, and put it into your hand. If your opponent has only 1 Prize, the Defending Pokémon is now Burned, Paralyzed, and Poisoned.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=mystery_plate_desert_burn(),
        ),
        Ability(
            title="Mystery Plate α",
            game_text="Discard this card at the end of your turn.",
            trigger=Triggers.END_OF_TURN,
            effect=discard_tool_at_end_of_turn(),
        ),
    ],
)
