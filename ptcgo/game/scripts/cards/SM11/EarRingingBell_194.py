from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import tool_confuse_attacker

card = PokemonToolCardDef(
    guid="2d77f5bb-b373-5265-8b33-6902f10fffe8",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EarRingingBell.Name",
    display_name="Ear-Ringing Bell",
    searchable_by=["Ear-Ringing Bell", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=194,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Ear-Ringing Bell",
            game_text="Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it. If the Pokémon this card is attached to is your Active Pokémon and is damaged by an opponent's attack (even if that Pokémon is Knocked Out), the Attacking Pokémon is now Confused. You may play as many Item cards as you like during your turn (before your attack).",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=tool_confuse_attacker(),
        ),
    ],
)
