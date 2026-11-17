from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="e0e03f29-2dbb-55e9-a7c8-ef3f01d69303",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Judge.Name",
    display_name="Judge",
    searchable_by=["Judge", "Supporter"],
    subtypes=["Supporter"],
    collector_number=76,
    set_code="ME3",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
