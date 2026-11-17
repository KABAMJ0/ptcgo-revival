from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import all_of, is_basic_energy_card, is_supporter_card

card = SupporterCardDef(
    guid="1d911495-bac3-5000-b31b-4be666caca7e",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Steven.Name",
    display_name="Steven",
    searchable_by=["Steven", "Supporter"],
    subtypes=["Supporter"],
    collector_number=90,
    set_code="XY6",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(all_of(is_supporter_card, is_basic_energy_card), count=1)
)
