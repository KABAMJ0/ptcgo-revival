from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities

card = SupporterCardDef(
    guid="1fc05985-a25a-5825-a3eb-e83c8ae36363",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Zinnia.Name",
    display_name="Zinnia",
    searchable_by=["Zinnia", "Supporter"],
    subtypes=["Supporter"],
    collector_number=64,
    set_code="DM",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
