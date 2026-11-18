from ptcgo.game.data_utils import StadiumCardDef, unimplemented
from ptcgo.game.attributes import Rarities

card = StadiumCardDef(
    guid="42a29a8d-835a-5f36-8650-e918f2b9f4b6",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TheRocketsTrainingGym.Name",
    display_name="The Rocket's Training Gym",
    searchable_by=["The Rocket's Training Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=104,
    set_code="GYM1",
    rarity=Rarities.Rare,
    effect=unimplemented
)
