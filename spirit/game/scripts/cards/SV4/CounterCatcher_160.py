from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="99fba3a1-d60e-5ff0-991b-7040641f4831",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CounterCatcher.Name",
    display_name="Counter Catcher",
    searchable_by=["Counter Catcher", "Item"],
    subtypes=["Item"],
    collector_number=160,
    set_code="SV4",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
