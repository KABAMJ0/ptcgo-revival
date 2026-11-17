from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card, trade_to_hand

card = ItemCardDef(
    guid="0b0dab82-1de7-59c4-8e6e-4b2aa650f8ac",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRetrieval.Name",
    display_name="Energy Retrieval",
    searchable_by=["Energy Retrieval"],
    subtypes=[],
    collector_number=81,
    set_code="BASE1",
    rarity=Rarities.Uncommon,
    effect=trade_to_hand(is_basic_energy_card, count=2)
)
