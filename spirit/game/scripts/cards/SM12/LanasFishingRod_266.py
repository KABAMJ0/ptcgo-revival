from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="c45f0375-1147-5185-bbfc-fc5a9ace97f7",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LanasFishingRod.Name",
    display_name="Lana's Fishing Rod",
    searchable_by=["Lana's Fishing Rod", "Item"],
    subtypes=["Item"],
    collector_number=266,
    set_code="SM12",
    rarity=Rarities.RareSecret,
    effect=unimplemented
)
