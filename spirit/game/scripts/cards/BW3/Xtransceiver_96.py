from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import if_heads, is_supporter_card

card = ItemCardDef(
    guid="366251ef-5691-5e67-bf80-4bf88b52fae6",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Xtransceiver.Name",
    display_name="Xtransceiver",
    searchable_by=["Xtransceiver", "Item"],
    subtypes=["Item"],
    collector_number=96,
    set_code="BW3",
    rarity=Rarities.Uncommon,
    effect=if_heads(search_to_hand(is_supporter_card, count=1))
)
