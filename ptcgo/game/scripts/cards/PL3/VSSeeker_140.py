from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities

card = ItemCardDef(
    guid="415c45ab-fac1-5e08-a53c-a32a2837b0d4",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.VSSeeker.Name",
    display_name="VS Seeker",
    searchable_by=["VS Seeker", "Item"],
    subtypes=["Item"],
    collector_number=140,
    set_code="PL3",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
