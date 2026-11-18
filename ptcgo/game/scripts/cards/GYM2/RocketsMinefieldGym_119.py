from ptcgo.game.data_utils import StadiumCardDef, unimplemented
from ptcgo.game.attributes import Rarities

card = StadiumCardDef(
    guid="001174e4-1a40-5fb7-a678-f8555a7adb78",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RocketsMinefieldGym.Name",
    display_name="Rocket's Minefield Gym",
    searchable_by=["Rocket's Minefield Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=119,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
