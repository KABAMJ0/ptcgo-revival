from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities

card = SupporterCardDef(
    guid="8f3a7c42-53df-530b-b29f-fd96705a4b07",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorRowan.Name",
    display_name="Professor Rowan",
    searchable_by=["Professor Rowan", "Supporter"],
    subtypes=["Supporter"],
    collector_number=123,
    set_code="DP3",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
