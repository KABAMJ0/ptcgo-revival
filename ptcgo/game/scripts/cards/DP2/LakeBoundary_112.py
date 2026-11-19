from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import stadium_weakness_multiplier

card = StadiumCardDef(
    guid="e58275a2-d98b-5056-acea-4a4170041551",
    key="DP2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LakeBoundary.Name",
    display_name="Lake Boundary",
    searchable_by=["Lake Boundary", "Stadium"],
    subtypes=["Stadium"],
    collector_number=112,
    set_code="DP2",
    rarity=Rarities.Uncommon,
    passive=stadium_weakness_multiplier(2)
)
