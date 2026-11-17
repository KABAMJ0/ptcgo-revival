from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import is_basic_energy_card

card = SupporterCardDef(
    guid="2941d516-5f1c-5e61-bb90-33e244c58664",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lady.Name",
    display_name="Lady",
    searchable_by=["Lady", "Supporter"],
    subtypes=["Supporter"],
    collector_number=109,
    set_code="SM6",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(is_basic_energy_card, count=4)
)
