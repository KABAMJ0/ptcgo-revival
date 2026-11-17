from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import is_basic_energy_card

card = ItemCardDef(
    guid="afcd74ce-1221-5b41-97be-d243d8d2f542",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySearch.Name",
    display_name="Energy Search",
    searchable_by=["Energy Search", "Item"],
    subtypes=["Item"],
    collector_number=93,
    set_code="BW1",
    rarity=Rarities.Common,
    effect=search_to_hand(is_basic_energy_card, count=1)
)
