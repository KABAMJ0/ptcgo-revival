from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import is_basic_energy_card

card = ItemCardDef(
    guid="3f77c3a8-e7cc-529d-8bf0-d36796798a45",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRetrieval.Name",
    display_name="Energy Retrieval",
    searchable_by=["Energy Retrieval", "Item"],
    subtypes=["Item"],
    collector_number=171,
    set_code="SV1",
    rarity=Rarities.Common,
    effect=recover_from_discard(is_basic_energy_card, count=2, to="hand")
)
