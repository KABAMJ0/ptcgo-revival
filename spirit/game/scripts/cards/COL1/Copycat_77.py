from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="1e37970b-44c9-52e9-b1ad-42deb3cfb2fd",
    key="COL1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Copycat.Name",
    display_name="Copycat",
    searchable_by=["Copycat", "Supporter"],
    subtypes=["Supporter"],
    collector_number=77,
    set_code="COL1",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
