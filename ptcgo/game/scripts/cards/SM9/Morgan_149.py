from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities

card = SupporterCardDef(
    guid="a7ad922d-1bd6-5fcd-b378-830c4699c2af",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Morgan.Name",
    display_name="Morgan",
    searchable_by=["Morgan", "Supporter"],
    subtypes=["Supporter"],
    collector_number=149,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
