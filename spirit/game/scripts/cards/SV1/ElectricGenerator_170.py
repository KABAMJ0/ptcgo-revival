from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="cdf66ab1-eee4-508e-b3b0-5c09c6455f21",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ElectricGenerator.Name",
    display_name="Electric Generator",
    searchable_by=["Electric Generator", "Item"],
    subtypes=["Item"],
    collector_number=170,
    set_code="SV1",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
