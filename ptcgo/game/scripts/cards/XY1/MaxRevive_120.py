from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities

card = ItemCardDef(
    guid="bdfab0b2-e405-5f82-9a79-2dcf3987e2ed",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MaxRevive.Name",
    display_name="Max Revive",
    searchable_by=["Max Revive", "Item"],
    subtypes=["Item"],
    collector_number=120,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
