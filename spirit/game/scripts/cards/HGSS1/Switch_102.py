from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="edc5ffe5-03b0-516c-9656-794d88323516",
    key="HGSS1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Switch.Name",
    display_name="Switch",
    searchable_by=["Switch", "Item"],
    subtypes=["Item"],
    collector_number=102,
    set_code="HGSS1",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
