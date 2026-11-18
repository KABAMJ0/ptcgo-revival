from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities

card = SupporterCardDef(
    guid="12b2a860-fa29-577f-8511-434461d6e945",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsArcher.Name",
    display_name="Team Rocket's Archer",
    searchable_by=["Team Rocket's Archer", "Supporter"],
    subtypes=["Supporter"],
    collector_number=201,
    set_code="ME2PT5",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
