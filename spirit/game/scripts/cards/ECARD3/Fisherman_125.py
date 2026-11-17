from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="f1937dc1-34e8-52f3-8e0d-16cf1ab528a6",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Fisherman.Name",
    display_name="Fisherman",
    searchable_by=["Fisherman", "Supporter"],
    subtypes=["Supporter"],
    collector_number=125,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
