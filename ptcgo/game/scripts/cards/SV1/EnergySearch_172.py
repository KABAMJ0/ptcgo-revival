from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import is_basic_energy_card

card = ItemCardDef(
    guid="46f48070-76c6-5e20-8f2f-682bdd057eb2",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySearch.Name",
    display_name="Energy Search",
    searchable_by=["Energy Search", "Item"],
    subtypes=["Item"],
    collector_number=172,
    set_code="SV1",
    rarity=Rarities.Common,
    effect=search_to_hand(is_basic_energy_card, count=1)
)
