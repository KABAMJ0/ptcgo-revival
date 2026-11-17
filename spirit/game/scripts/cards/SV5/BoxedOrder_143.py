from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import ends_turn_after, is_item_card

card = ItemCardDef(
    guid="f0b0a90e-e6c5-55ac-945a-8c6e7f60e836",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BoxedOrder.Name",
    display_name="Boxed Order",
    searchable_by=["Boxed Order", "Item"],
    subtypes=["Item"],
    collector_number=143,
    set_code="SV5",
    rarity=Rarities.Uncommon,
    effect=ends_turn_after(search_to_hand(is_item_card, count=2))
)
