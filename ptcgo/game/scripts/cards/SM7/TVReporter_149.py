from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities

card = SupporterCardDef(
    guid="1c654575-c481-5dce-aabf-0f3142da2fc0",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TVReporter.Name",
    display_name="TV Reporter",
    searchable_by=["TV Reporter", "Supporter"],
    subtypes=["Supporter"],
    collector_number=149,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
