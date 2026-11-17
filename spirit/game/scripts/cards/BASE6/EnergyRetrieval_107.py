from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card, trade_to_hand

card = ItemCardDef(
    guid="e1c43bce-3938-5a06-a8c6-9f5d93f9ba5c",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRetrieval.Name",
    display_name="Energy Retrieval",
    searchable_by=["Energy Retrieval"],
    subtypes=[],
    collector_number=107,
    set_code="BASE6",
    rarity=Rarities.Uncommon,
    effect=trade_to_hand(is_basic_energy_card, count=2)
)
