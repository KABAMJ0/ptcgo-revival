from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="1442d11a-2ff6-55a7-b23e-c7b37dc4fc0c",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FairyDrop.Name",
    display_name="Fairy Drop",
    searchable_by=["Fairy Drop", "Item"],
    subtypes=["Item"],
    collector_number=99,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
