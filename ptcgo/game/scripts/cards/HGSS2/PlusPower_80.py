from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities

card = ItemCardDef(
    guid="d52715cc-ac2c-5677-be96-4193b0a7721a",
    key="HGSS2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PlusPower.Name",
    display_name="PlusPower",
    searchable_by=["PlusPower", "Item"],
    subtypes=["Item"],
    collector_number=80,
    set_code="HGSS2",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
