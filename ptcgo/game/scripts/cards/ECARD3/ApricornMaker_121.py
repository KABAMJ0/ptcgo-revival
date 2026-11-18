from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import all_of, card_named_contains, is_item_card

card = SupporterCardDef(
    guid="d1632ad8-ccea-5bb2-bf9d-18bdddaaab22",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ApricornMaker.Name",
    display_name="Apricorn Maker",
    searchable_by=["Apricorn Maker", "Supporter"],
    subtypes=["Supporter"],
    collector_number=121,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(all_of(is_item_card, card_named_contains("ball")), count=2)
)
