from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import all_of, is_item_card, is_tool_card

card = SupporterCardDef(
    guid="9cd76f29-7ed0-5119-aac4-fdb0adc23b8b",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Arven.Name",
    display_name="Arven",
    searchable_by=["Arven", "Supporter"],
    subtypes=["Supporter"],
    collector_number=249,
    set_code="SV1",
    rarity=Rarities.Rare,
    effect=search_to_hand(all_of(is_item_card, is_tool_card), count=1)
)
