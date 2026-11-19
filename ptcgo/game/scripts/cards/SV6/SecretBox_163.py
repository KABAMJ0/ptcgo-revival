from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.session.effects import is_item_card, is_supporter_card
from ptcgo.game.card_effects.trainers import is_stadium_card, is_tool_card, search_one_of_each, with_discard_cost

_SECRET_BOX_KINDS = [
    is_item_card, is_tool_card, is_supporter_card, is_stadium_card]


card = ItemCardDef(
    guid="fdbdeb3f-039f-5812-b678-11ef9082900a",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SecretBox.Name",
    display_name="Secret Box",
    searchable_by=["Secret Box", "Item", "ACE SPEC"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=163,
    set_code="SV6",
    rarity=Rarities.Rare,
    effect=with_discard_cost(3, search_one_of_each(_SECRET_BOX_KINDS))
)
