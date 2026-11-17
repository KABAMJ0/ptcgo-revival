from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import is_basic_energy_card, with_discard_cost

card = ItemCardDef(
    guid="c3ab40fd-60c8-52db-8aff-57ec9008c821",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EarthenVessel.Name",
    display_name="Earthen Vessel",
    searchable_by=["Earthen Vessel", "Item", "Ancient"],
    subtypes=["Item", "Ancient"],
    collector_number=106,
    set_code="SV8PT5",
    rarity=Rarities.Uncommon,
    effect=with_discard_cost(1, search_to_hand(is_basic_energy_card, count=2))
)
