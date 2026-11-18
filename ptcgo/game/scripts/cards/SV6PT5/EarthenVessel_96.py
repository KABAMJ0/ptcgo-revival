from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import is_basic_energy_card, with_discard_cost

card = ItemCardDef(
    guid="6ed6d323-585a-5c20-8364-99bb28871fcf",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EarthenVessel.Name",
    display_name="Earthen Vessel",
    searchable_by=["Earthen Vessel", "Item", "Ancient"],
    subtypes=["Item", "Ancient"],
    collector_number=96,
    set_code="SV6PT5",
    rarity=Rarities.Rare,
    effect=with_discard_cost(1, search_to_hand(is_basic_energy_card, count=2))
)
