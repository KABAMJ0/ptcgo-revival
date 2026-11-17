from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="45af2673-7da9-5e60-a2a3-6d6ea7fdc535",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Shauna.Name",
    display_name="Shauna",
    searchable_by=["Shauna", "Supporter"],
    subtypes=["Supporter"],
    collector_number=111,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
