from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="a8dd560b-233c-5e23-84af-52f218ed0804",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RotomDex.Name",
    display_name="Rotom Dex",
    searchable_by=["Rotom Dex", "Item"],
    subtypes=["Item"],
    collector_number=159,
    set_code="SM1",
    rarity=Rarities.RareSecret,
    effect=unimplemented
)
