from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="a0987a78-5f24-5020-890a-506d425d5e6f",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PremiumPowerPro.Name",
    display_name="Premium Power Pro",
    searchable_by=["Premium Power Pro", "Item"],
    subtypes=["Item"],
    collector_number=199,
    set_code="ME2PT5",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
