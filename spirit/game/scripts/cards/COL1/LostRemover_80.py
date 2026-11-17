from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="1a0fdbbf-214e-501e-ba70-8d97fc3f623b",
    key="COL1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LostRemover.Name",
    display_name="Lost Remover",
    searchable_by=["Lost Remover", "Item"],
    subtypes=["Item"],
    collector_number=80,
    set_code="COL1",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
