from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import all_of, is_basic_energy_card, is_supporter_card

card = SupporterCardDef(
    guid="2222e444-ca70-5b8a-9ba8-c8990419db06",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Steven.Name",
    display_name="Steven",
    searchable_by=["Steven", "Supporter"],
    subtypes=["Supporter"],
    collector_number=95,
    set_code="XY7",
    rarity=Rarities.RareUltra,
    effect=search_to_hand(all_of(is_supporter_card, is_basic_energy_card), count=1)
)
