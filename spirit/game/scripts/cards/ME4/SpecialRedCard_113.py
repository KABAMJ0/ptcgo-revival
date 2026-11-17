from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="7d7a4521-9eda-5f7d-91d7-08ff2f5b64d9",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SpecialRedCard.Name",
    display_name="Special Red Card",
    searchable_by=["Special Red Card", "Item"],
    subtypes=["Item"],
    collector_number=113,
    set_code="ME4",
    rarity=Rarities.Rare,
    effect=unimplemented
)
