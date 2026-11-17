from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import look_at_top
from spirit.game.card_effects.trainers import is_energy_card

card = ItemCardDef(
    guid="1a060d31-9c23-515d-8360-738b65244ff4",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyLoto.Name",
    display_name="Energy Loto",
    searchable_by=["Energy Loto", "Item"],
    subtypes=["Item"],
    collector_number=122,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    effect=look_at_top(7, take=1, predicate=is_energy_card)
)
