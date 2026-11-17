from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import is_basic_energy_card

card = ItemCardDef(
    guid="90e33c91-c781-5c1a-bf33-e47456d26dc5",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySearch.Name",
    display_name="Energy Search",
    searchable_by=["Energy Search"],
    subtypes=[],
    collector_number=153,
    set_code="ECARD1",
    rarity=Rarities.Common,
    effect=search_to_hand(is_basic_energy_card, count=1)
)
