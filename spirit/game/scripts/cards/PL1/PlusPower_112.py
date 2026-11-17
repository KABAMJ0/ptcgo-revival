from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="cfce6c9e-8d56-51b5-95d1-b57bc910e6aa",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PlusPower.Name",
    display_name="PlusPower",
    searchable_by=["PlusPower", "Item"],
    subtypes=["Item"],
    collector_number=112,
    set_code="PL1",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
