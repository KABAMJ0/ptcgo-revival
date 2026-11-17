from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="42a54f77-ffd1-51ac-8175-70de265f2b2c",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RedBlue.Name",
    display_name="Red & Blue",
    searchable_by=["Red & Blue", "Supporter", "TAG TEAM"],
    subtypes=["Supporter", "TAG TEAM"],
    collector_number=234,
    set_code="SM12",
    rarity=Rarities.RareUltra,
    effect=unimplemented
)
