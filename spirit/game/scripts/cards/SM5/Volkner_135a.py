from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import all_of, basic_energy_of, is_item_card

card = SupporterCardDef(
    guid="e8cbab33-acb2-595c-8ee1-38082621b7f8",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Volkner.Name",
    display_name="Volkner",
    searchable_by=["Volkner", "Supporter"],
    subtypes=["Supporter"],
    collector_number=135,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(all_of(is_item_card, basic_energy_of("lightning")), count=1)
)
