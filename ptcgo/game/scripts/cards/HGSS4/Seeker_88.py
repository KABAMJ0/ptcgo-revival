from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities

card = SupporterCardDef(
    guid="68a2abbd-7505-59cf-a68d-5fd5d401d6a1",
    key="HGSS4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Seeker.Name",
    display_name="Seeker",
    searchable_by=["Seeker", "Supporter"],
    subtypes=["Supporter"],
    collector_number=88,
    set_code="HGSS4",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
