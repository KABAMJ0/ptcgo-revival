from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import is_basic_energy_card

card = ItemCardDef(
    guid="69df534d-067c-5710-80b1-4517bc0ad4ea",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySearch.Name",
    display_name="Energy Search",
    searchable_by=["Energy Search", "Item"],
    subtypes=["Item"],
    collector_number=86,
    set_code="EX14",
    rarity=Rarities.Common,
    effect=search_to_hand(is_basic_energy_card, count=1)
)
