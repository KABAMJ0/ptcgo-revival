from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import is_basic_energy_card

card = ItemCardDef(
    guid="af564d46-b56a-5152-9eb8-a9faa44be548",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRetrieval.Name",
    display_name="Energy Retrieval",
    searchable_by=["Energy Retrieval", "Item"],
    subtypes=["Item"],
    collector_number=82,
    set_code="RSV10PT5",
    rarity=Rarities.Uncommon,
    effect=recover_from_discard(is_basic_energy_card, count=2, to="hand")
)
