from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="d772de74-97f2-5b83-8561-4586479f1790",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NestBall.Name",
    display_name="Nest Ball",
    searchable_by=["Nest Ball", "Item"],
    subtypes=["Item"],
    collector_number=255,
    set_code="SV1",
    rarity=Rarities.Rare,
    effect=unimplemented
)
