from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import all_of, is_item_card, is_tool_card

card = SupporterCardDef(
    guid="21615cc1-0ae5-5f28-b880-64538407bbe8",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Arven.Name",
    display_name="Arven",
    searchable_by=["Arven", "Supporter"],
    subtypes=["Supporter"],
    collector_number=235,
    set_code="SV1",
    rarity=Rarities.Rare,
    effect=search_to_hand(all_of(is_item_card, is_tool_card), count=1)
)
