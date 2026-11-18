from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.card_effects.trainers import is_basic_energy_card

card = ItemCardDef(
    guid="f9827398-87c0-583b-84f3-9bb314a7c29b",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRetrieval.Name",
    display_name="Energy Retrieval",
    searchable_by=["Energy Retrieval", "Item"],
    subtypes=["Item"],
    collector_number=77,
    set_code="XY12",
    rarity=Rarities.Uncommon,
    effect=recover_from_discard(is_basic_energy_card, count=2, to="hand")
)
