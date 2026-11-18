from ptcgo.game.data_utils import StadiumCardDef, unimplemented
from ptcgo.game.attributes import Rarities

card = StadiumCardDef(
    guid="9f716805-d6d8-5400-bd3a-d295e751aacd",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TrainingCenter.Name",
    display_name="Training Center",
    searchable_by=["Training Center", "Stadium"],
    subtypes=["Stadium"],
    collector_number=102,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
