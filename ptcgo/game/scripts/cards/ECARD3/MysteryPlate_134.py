from ptcgo.game.data_utils import PokemonToolCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import PokemonTypes, Rarities, SpecialConditions
from ptcgo.game.card_effects.trainers import mystery_plate_stone_crush, discard_tool_at_end_of_turn

card = PokemonToolCardDef(
    guid="476b9808-6971-5be2-ad19-73e228ec2598",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MysteryPlate.Name",
    display_name="Mystery Plate β",
    searchable_by=["Mystery Plate \u03b2", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=134,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Attack(
            title="Stone Crush",
            game_text="If your opponent has 5 or more Prizes, draw 3 cards. If your opponent has only 1 Prize, choose 2 Energy cards attached to the Defending Pokémon (1 if there is only 1). Your opponent shuffles those cards into his or her deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=mystery_plate_stone_crush(),
        ),
        Ability(
            title="Mystery Plate β",
            game_text="Discard this card at the end of your turn.",
            trigger=Triggers.END_OF_TURN,
            effect=discard_tool_at_end_of_turn(),
        ),
    ],
)
