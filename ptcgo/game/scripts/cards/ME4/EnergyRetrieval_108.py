from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.card_effects.trainers import is_basic_energy_card

card = ItemCardDef(
    guid="2adff3ff-c196-5a82-93bb-3ed3868ea4a7",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRetrieval.Name",
    display_name="Energy Retrieval",
    searchable_by=["Energy Retrieval", "Item"],
    subtypes=["Item"],
    collector_number=108,
    set_code="ME4",
    rarity=Rarities.Rare,
    effect=recover_from_discard(is_basic_energy_card, count=2, to="hand")
)
