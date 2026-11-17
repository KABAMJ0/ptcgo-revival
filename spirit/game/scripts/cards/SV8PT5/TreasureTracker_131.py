from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import is_tool_card

card = ItemCardDef(
    guid="e55640a4-19d4-5e11-b83a-7b5f8966c902",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TreasureTracker.Name",
    display_name="Treasure Tracker",
    searchable_by=["Treasure Tracker", "Item", "ACE SPEC"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=131,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    effect=search_to_hand(is_tool_card, count=5)
)
