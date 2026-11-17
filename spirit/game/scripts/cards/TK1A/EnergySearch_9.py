from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import is_basic_energy_card

card = ItemCardDef(
    guid="e8bb5119-9817-54f4-a0e0-097fef27af5b",
    key="TK1A",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySearch.Name",
    display_name="Energy Search",
    searchable_by=["Energy Search", "Item"],
    subtypes=["Item"],
    collector_number=9,
    set_code="TK1A",
    rarity=Rarities.Common,
    effect=search_to_hand(is_basic_energy_card, count=1)
)
