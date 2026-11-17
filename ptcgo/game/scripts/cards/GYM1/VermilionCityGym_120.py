from ptcgo.game.data_utils import StadiumCardDef, unimplemented
from ptcgo.game.attributes import Rarities

card = StadiumCardDef(
    guid="0760beea-88de-58bf-9526-3ebe4198398f",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.VermilionCityGym.Name",
    display_name="Vermilion City Gym",
    searchable_by=["Vermilion City Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=120,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
