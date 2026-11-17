from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import is_basic_energy_card

card = ItemCardDef(
    guid="8d7e9b30-ce96-5f75-9d48-a25c678fba68",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRetrieval.Name",
    display_name="Energy Retrieval",
    searchable_by=["Energy Retrieval", "Item"],
    subtypes=["Item"],
    collector_number=126,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    effect=recover_from_discard(is_basic_energy_card, count=2, to="hand")
)
