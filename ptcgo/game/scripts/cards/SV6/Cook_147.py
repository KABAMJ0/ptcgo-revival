from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities

card = SupporterCardDef(
    guid="3339efed-250b-5ec5-b113-e5787a79d27c",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Cook.Name",
    display_name="Cook",
    searchable_by=["Cook", "Supporter"],
    subtypes=["Supporter"],
    collector_number=147,
    set_code="SV6",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
