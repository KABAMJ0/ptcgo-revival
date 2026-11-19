from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import tool_counters_on_attacker

card = PokemonToolCardDef(
    guid="65745751-0123-5aa3-aec1-f443028b5b9f",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BurstingBalloon.Name",
    display_name="Bursting Balloon",
    searchable_by=["Bursting Balloon", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=97,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Bursting Balloon",
            game_text="Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it. If this card is attached to 1 of your Pokémon, discard it at the end of your opponent's turn. If the Pokémon this card is attached to is your Active Pokémon and is damaged by an opponent's attack (even if that Pokémon is Knocked Out), put 6 damage counters on the Attacking Pokémon. You may play as many Item cards as you like during your turn (before your attack).",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=tool_counters_on_attacker(6, 0),
        ),
    ],
)
