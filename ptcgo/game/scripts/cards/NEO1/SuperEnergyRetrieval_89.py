from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_basic_energy_card, trade_n_to_hand

card = ItemCardDef(
    guid="0d7c1281-b3da-5ce6-b7eb-1100930f7ad2",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperEnergyRetrieval.Name",
    display_name="Super Energy Retrieval",
    searchable_by=["Super Energy Retrieval"],
    subtypes=[],
    collector_number=89,
    set_code="NEO1",
    rarity=Rarities.Rare,
    effect=trade_n_to_hand(2, is_basic_energy_card, 4)
)
