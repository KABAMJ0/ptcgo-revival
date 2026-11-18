from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import is_basic_energy_card

card = ItemCardDef(
    guid="57fda128-42ec-597a-a0a6-0ef76cb7da7f",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySearch.Name",
    display_name="Energy Search",
    searchable_by=["Energy Search", "Item"],
    subtypes=["Item"],
    collector_number=72,
    set_code="ME3",
    rarity=Rarities.Common,
    effect=search_to_hand(is_basic_energy_card, count=1)
)
