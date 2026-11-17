from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="625422aa-24bd-55a3-acb1-ccb2670cd5e6",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Potion.Name",
    display_name="Potion",
    searchable_by=["Potion", "Item"],
    subtypes=["Item"],
    collector_number=91,
    set_code="EX1",
    rarity=Rarities.Common,
    effect=unimplemented
)
