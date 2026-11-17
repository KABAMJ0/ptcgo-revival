from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities

card = SupporterCardDef(
    guid="c9f5e4ac-36a4-5da9-acf1-d84198fbd72e",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BrocksTraining.Name",
    display_name="Brock's Training",
    searchable_by=["Brock's Training", "Supporter"],
    subtypes=["Supporter"],
    collector_number=55,
    set_code="HF",
    rarity=Rarities.RareHolo,
    effect=unimplemented
)
