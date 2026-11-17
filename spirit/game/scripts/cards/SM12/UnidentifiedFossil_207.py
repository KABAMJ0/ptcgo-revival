from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="97458d5c-c30e-5972-9922-30ecf7b16f65",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UnidentifiedFossil.Name",
    display_name="Unidentified Fossil",
    searchable_by=["Unidentified Fossil", "Item"],
    subtypes=["Item"],
    collector_number=207,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
