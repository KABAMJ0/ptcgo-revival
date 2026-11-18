from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import search_three_stages

card = SupporterCardDef(
    guid="cdcb61ab-7c9b-5c5b-abcd-b28d55b971b5",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Dawn.Name",
    display_name="Dawn",
    searchable_by=["Dawn", "Supporter"],
    subtypes=["Supporter"],
    collector_number=87,
    set_code="ME2",
    rarity=Rarities.Uncommon,
    effect=search_three_stages()
)
