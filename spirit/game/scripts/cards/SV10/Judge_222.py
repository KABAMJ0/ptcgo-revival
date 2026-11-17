from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="7b2c4b16-9492-53db-9952-acd66d076982",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Judge.Name",
    display_name="Judge",
    searchable_by=["Judge", "Supporter"],
    subtypes=["Supporter"],
    collector_number=222,
    set_code="SV10",
    rarity=Rarities.Rare,
    effect=unimplemented
)
