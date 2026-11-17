from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="5b4345fc-a8f6-5bf2-bd1e-a865ac7d503b",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Copycat.Name",
    display_name="Copycat",
    searchable_by=["Copycat", "Supporter"],
    subtypes=["Supporter"],
    collector_number=138,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
