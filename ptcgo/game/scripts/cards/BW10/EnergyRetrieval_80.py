from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.card_effects.trainers import is_basic_energy_card

card = ItemCardDef(
    guid="ce769df0-6b2b-52e1-8901-644c4c43d1e4",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRetrieval.Name",
    display_name="Energy Retrieval",
    searchable_by=["Energy Retrieval", "Item"],
    subtypes=["Item"],
    collector_number=80,
    set_code="BW10",
    rarity=Rarities.Uncommon,
    effect=recover_from_discard(is_basic_energy_card, count=2, to="hand")
)
