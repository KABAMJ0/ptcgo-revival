from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities

card = SupporterCardDef(
    guid="3358863d-bf4d-575d-b784-04f0754a6116",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Oracle.Name",
    display_name="Oracle",
    searchable_by=["Oracle", "Supporter"],
    subtypes=["Supporter"],
    collector_number=138,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
