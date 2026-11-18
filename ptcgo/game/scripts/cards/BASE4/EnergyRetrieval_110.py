from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_basic_energy_card, trade_to_hand

card = ItemCardDef(
    guid="14f2bf5e-bc6c-5c61-b75d-69544763092f",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRetrieval.Name",
    display_name="Energy Retrieval",
    searchable_by=["Energy Retrieval"],
    subtypes=[],
    collector_number=110,
    set_code="BASE4",
    rarity=Rarities.Uncommon,
    effect=trade_to_hand(is_basic_energy_card, count=2)
)
