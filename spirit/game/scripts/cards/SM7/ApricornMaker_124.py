from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import all_of, card_named_contains, is_item_card

card = SupporterCardDef(
    guid="84ac64f4-d478-5575-8ab3-7137074956dc",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ApricornMaker.Name",
    display_name="Apricorn Maker",
    searchable_by=["Apricorn Maker", "Supporter"],
    subtypes=["Supporter"],
    collector_number=124,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(all_of(is_item_card, card_named_contains("ball")), count=2)
)
