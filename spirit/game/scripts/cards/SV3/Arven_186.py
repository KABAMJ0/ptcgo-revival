from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import all_of, is_item_card, is_tool_card

card = SupporterCardDef(
    guid="0d5af623-846d-520d-8544-b2f1877c5a12",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Arven.Name",
    display_name="Arven",
    searchable_by=["Arven", "Supporter"],
    subtypes=["Supporter"],
    collector_number=186,
    set_code="SV3",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(all_of(is_item_card, is_tool_card), count=1)
)
