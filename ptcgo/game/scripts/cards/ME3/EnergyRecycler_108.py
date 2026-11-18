from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.card_effects.trainers import is_basic_energy_card

card = ItemCardDef(
    guid="4ab9a4ab-037d-5c2f-b5b1-9061e84f2752",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRecycler.Name",
    display_name="Energy Recycler",
    searchable_by=["Energy Recycler", "Item"],
    subtypes=["Item"],
    collector_number=108,
    set_code="ME3",
    rarity=Rarities.Rare,
    effect=recover_from_discard(is_basic_energy_card, count=5, to="deck_shuffle")
)
