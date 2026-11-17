from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="b70f88dd-ba84-5684-9ca6-03162b5b6181",
    key="DC1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamMagmaGrunt.Name",
    display_name="Team Magma Grunt",
    searchable_by=["Team Magma Grunt", "Supporter"],
    subtypes=["Supporter"],
    collector_number=30,
    set_code="DC1",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
