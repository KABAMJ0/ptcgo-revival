from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import tool_search_deck_on_ko

card = PokemonToolCardDef(
    guid="cc4158ec-3ea7-5f85-b528-b1b001380760",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ReversalTrigger.Name",
    display_name="Reversal Trigger",
    searchable_by=["Reversal Trigger", "Pok\u00e9mon Tool", "Team Plasma"],
    subtypes=["Pok\u00e9mon Tool", "Team Plasma"],
    collector_number=86,
    set_code="BW10",
    rarity=Rarities.Uncommon,
    on_carrier_knocked_out=tool_search_deck_on_ko(1, "Team Plasma"),
)
