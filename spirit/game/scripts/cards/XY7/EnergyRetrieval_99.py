from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import is_basic_energy_card

card = ItemCardDef(
    guid="490cf4ec-d7cc-599a-a191-8669ea2f4855",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRetrieval.Name",
    display_name="Energy Retrieval",
    searchable_by=["Energy Retrieval", "Item"],
    subtypes=["Item"],
    collector_number=99,
    set_code="XY7",
    rarity=Rarities.RareSecret,
    effect=recover_from_discard(is_basic_energy_card, count=2, to="hand")
)
