from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="d9f4c6af-2405-5c90-85ba-050a39590caf",
    key="HGSS1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FullHeal.Name",
    display_name="Full Heal",
    searchable_by=["Full Heal", "Item"],
    subtypes=["Item"],
    collector_number=93,
    set_code="HGSS1",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
