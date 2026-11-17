from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import all_of, is_item_card, is_tool_card

card = SupporterCardDef(
    guid="46445fbb-6d14-59d4-a8e6-cbd75e021354",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Arven.Name",
    display_name="Arven",
    searchable_by=["Arven", "Supporter"],
    subtypes=["Supporter"],
    collector_number=235,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    effect=search_to_hand(all_of(is_item_card, is_tool_card), count=1)
)
