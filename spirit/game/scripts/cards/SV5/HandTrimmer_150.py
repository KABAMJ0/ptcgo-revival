from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="aae207ce-e0a0-5f25-8063-2e1c66e4d901",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HandTrimmer.Name",
    display_name="Hand Trimmer",
    searchable_by=["Hand Trimmer", "Item"],
    subtypes=["Item"],
    collector_number=150,
    set_code="SV5",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
