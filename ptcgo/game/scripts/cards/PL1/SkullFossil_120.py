from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities

card = ItemCardDef(
    guid="507e5460-127b-5c85-978a-591fe604c620",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SkullFossil.Name",
    display_name="Skull Fossil",
    searchable_by=["Skull Fossil", "Item"],
    subtypes=["Item"],
    collector_number=120,
    set_code="PL1",
    rarity=Rarities.Common,
    effect=unimplemented
)
