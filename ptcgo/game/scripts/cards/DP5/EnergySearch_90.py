from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import is_basic_energy_card

card = ItemCardDef(
    guid="3afedf74-0a26-5162-9f9d-2bacb3ed80a1",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySearch.Name",
    display_name="Energy Search",
    searchable_by=["Energy Search", "Item"],
    subtypes=["Item"],
    collector_number=90,
    set_code="DP5",
    rarity=Rarities.Common,
    effect=search_to_hand(is_basic_energy_card, count=1)
)
