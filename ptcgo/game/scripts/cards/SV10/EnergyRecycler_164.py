from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.card_effects.trainers import is_basic_energy_card

card = ItemCardDef(
    guid="7d8d48d4-2137-5701-8011-337d883a93a9",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRecycler.Name",
    display_name="Energy Recycler",
    searchable_by=["Energy Recycler", "Item"],
    subtypes=["Item"],
    collector_number=164,
    set_code="SV10",
    rarity=Rarities.Uncommon,
    effect=recover_from_discard(is_basic_energy_card, count=5, to="deck_shuffle")
)
