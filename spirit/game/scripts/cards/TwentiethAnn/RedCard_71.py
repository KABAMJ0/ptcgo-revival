from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="e5e855ca-2af9-536e-a349-7dcf5d43bfc1",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RedCard.Name",
    display_name="Red Card",
    searchable_by=["Red Card", "Item"],
    subtypes=["Item"],
    collector_number=71,
    set_code="TwentiethAnn",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
