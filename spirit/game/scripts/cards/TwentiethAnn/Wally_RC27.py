from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="b5cb4fd0-47bb-5f4a-aa12-ab674497aecd",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Wally.Name",
    display_name="Wally",
    searchable_by=["Wally", "Supporter"],
    subtypes=["Supporter"],
    collector_number=10027,
    set_code="TwentiethAnn",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
