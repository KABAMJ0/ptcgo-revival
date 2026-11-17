from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="aa17d6e6-95ff-54af-9fc8-da00059c8d62",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MegaSignal.Name",
    display_name="Mega Signal",
    searchable_by=["Mega Signal", "Item"],
    subtypes=["Item"],
    collector_number=171,
    set_code="ME1",
    rarity=Rarities.Rare,
    effect=unimplemented
)
