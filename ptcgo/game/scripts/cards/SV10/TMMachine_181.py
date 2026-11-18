from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import all_of, card_named_contains, is_tool_card

card = ItemCardDef(
    guid="ecca6db6-927b-5c0f-bc8f-80ec67368173",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TMMachine.Name",
    display_name="TM Machine",
    searchable_by=["TM Machine", "Item", "MEGA"],
    subtypes=["Item", "MEGA"],
    collector_number=181,
    set_code="SV10",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(all_of(is_tool_card, card_named_contains("technical machine")), count=3)
)
