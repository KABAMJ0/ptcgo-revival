from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities

card = SupporterCardDef(
    guid="fe27cfa7-6c7a-5e28-bdf2-0f75f19b006d",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LysandresTrumpCard.Name",
    display_name="Lysandre's Trump Card",
    searchable_by=["Lysandre's Trump Card", "Supporter"],
    subtypes=["Supporter"],
    collector_number=99,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
