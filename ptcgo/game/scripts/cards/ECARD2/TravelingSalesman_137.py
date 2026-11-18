from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities

card = SupporterCardDef(
    guid="c0fe7623-f237-5205-a417-776add2aaa3b",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TravelingSalesman.Name",
    display_name="Traveling Salesman",
    searchable_by=["Traveling Salesman", "Supporter"],
    subtypes=["Supporter"],
    collector_number=137,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
