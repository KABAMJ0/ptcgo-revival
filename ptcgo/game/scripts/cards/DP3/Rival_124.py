from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities

card = SupporterCardDef(
    guid="7469ca89-93f5-564b-9dc6-e2edd08045ca",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Rival.Name",
    display_name="Rival",
    searchable_by=["Rival", "Supporter"],
    subtypes=["Supporter"],
    collector_number=124,
    set_code="DP3",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
