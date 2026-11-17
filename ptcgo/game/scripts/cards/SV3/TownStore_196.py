from ptcgo.game.data_utils import StadiumCardDef, unimplemented
from ptcgo.game.attributes import Rarities

card = StadiumCardDef(
    guid="72f9116a-7cc5-5e36-ab5e-bf1cc295dd8b",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TownStore.Name",
    display_name="Town Store",
    searchable_by=["Town Store", "Stadium"],
    subtypes=["Stadium"],
    collector_number=196,
    set_code="SV3",
    rarity=Rarities.Common,
    effect=unimplemented
)
