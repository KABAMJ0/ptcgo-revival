from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import (
    tool_counters_on_attacker, tool_discard_after_opponents_turn,
)

card = PokemonToolCardDef(
    guid="be4af5b4-2fb5-5014-87db-b12d4fafece0",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GiantBomb.Name",
    display_name="Giant Bomb",
    searchable_by=["Giant Bomb", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=251,
    set_code="SM11",
    rarity=Rarities.RareSecret,
    granted_abilities=[
        Ability(
            title="Giant Bomb",
            game_text="Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it. If this card is attached to 1 of your Pokémon, discard it at the end of your opponent's turn. If the Pokémon this card is attached to is your Active Pokémon and takes 180 or more damage from an opponent's attack (even if this Pokémon is Knocked Out), put 10 damage counters on the Attacking Pokémon. You may play as many Item cards as you like during your turn (before your attack).",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=tool_counters_on_attacker(10, 180),
        ),
        tool_discard_after_opponents_turn("Giant Bomb"),
    ],
)
