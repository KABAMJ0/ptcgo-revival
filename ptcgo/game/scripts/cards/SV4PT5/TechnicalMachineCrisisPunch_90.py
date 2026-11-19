from ptcgo.game.data_utils import PokemonToolCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import PokemonTypes, Rarities
from ptcgo.game.card_effects.trainers import discard_tool_at_end_of_turn, opponent_one_prize_left

card = PokemonToolCardDef(
    guid="625128f2-da71-59b3-90bd-39d1a71dd6e0",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TechnicalMachineCrisisPunch.Name",
    display_name="Technical Machine: Crisis Punch",
    searchable_by=["Technical Machine: Crisis Punch", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=90,
    set_code="SV4PT5",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Attack(
            title="Crisis Punch",
            game_text="You can use this attack only when your opponent has exactly 1 Prize card remaining.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=280,
            condition=opponent_one_prize_left(),
        ),
        Ability(
            title="Technical Machine: Crisis Punch",
            game_text="Discard this card at the end of your turn.",
            trigger=Triggers.END_OF_TURN,
            effect=discard_tool_at_end_of_turn(),
        ),
    ],
)
