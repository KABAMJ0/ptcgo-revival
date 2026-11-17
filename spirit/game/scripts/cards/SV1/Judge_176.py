from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="011a4419-840d-5a73-ad34-450491bb8c59",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Judge.Name",
    display_name="Judge",
    searchable_by=["Judge", "Supporter"],
    subtypes=["Supporter"],
    collector_number=176,
    set_code="SV1",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
