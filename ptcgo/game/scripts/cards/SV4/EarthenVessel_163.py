from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import is_basic_energy_card, with_discard_cost

card = ItemCardDef(
    guid="10f9d0a4-a4f9-5774-9bf4-3304369f9bcc",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EarthenVessel.Name",
    display_name="Earthen Vessel",
    searchable_by=["Earthen Vessel", "Item", "Ancient"],
    subtypes=["Item", "Ancient"],
    collector_number=163,
    set_code="SV4",
    rarity=Rarities.Uncommon,
    effect=with_discard_cost(1, search_to_hand(is_basic_energy_card, count=2))
)
