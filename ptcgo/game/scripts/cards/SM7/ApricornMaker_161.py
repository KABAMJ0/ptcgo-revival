from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import all_of, card_named_contains, is_item_card

card = SupporterCardDef(
    guid="22e510d3-8464-514d-8f9d-626260a00a63",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ApricornMaker.Name",
    display_name="Apricorn Maker",
    searchable_by=["Apricorn Maker", "Supporter"],
    subtypes=["Supporter"],
    collector_number=161,
    set_code="SM7",
    rarity=Rarities.RareUltra,
    effect=search_to_hand(all_of(is_item_card, card_named_contains("ball")), count=2)
)
