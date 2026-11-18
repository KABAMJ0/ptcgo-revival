from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import search_three_stages

card = SupporterCardDef(
    guid="83a75235-99ac-50d9-9c43-e44f00468d75",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Dawn.Name",
    display_name="Dawn",
    searchable_by=["Dawn", "Supporter"],
    subtypes=["Supporter"],
    collector_number=129,
    set_code="ME2",
    rarity=Rarities.Rare,
    effect=search_three_stages()
)
