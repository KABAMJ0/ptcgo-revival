from ptcgo.game.data_utils import StadiumCardDef, unimplemented
from ptcgo.game.attributes import Rarities

card = StadiumCardDef(
    guid="32ae71dd-dc45-5e5a-88d8-870437cc1c25",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ChampionsRoom.Name",
    display_name="Champion's Room",
    searchable_by=["Champion's Room", "Stadium"],
    subtypes=["Stadium"],
    collector_number=135,
    set_code="PL3",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
