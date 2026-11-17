from ptcgo.game.data_utils import StadiumCardDef, unimplemented
from ptcgo.game.attributes import Rarities

card = StadiumCardDef(
    guid="02b0c11b-06d6-5bc7-9ee6-e920ed4bbda5",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyStadium.Name",
    display_name="Energy Stadium",
    searchable_by=["Energy Stadium", "Stadium"],
    subtypes=["Stadium"],
    collector_number=99,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
