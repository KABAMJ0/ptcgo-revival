from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import if_heads, is_item_card

card = ItemCardDef(
    guid="ea39c280-408d-597b-9a7d-d7586e5ea8e2",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.OrderPad.Name",
    display_name="Order Pad",
    searchable_by=["Order Pad", "Item"],
    subtypes=["Item"],
    collector_number=131,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    effect=if_heads(search_to_hand(is_item_card, count=1))
)
