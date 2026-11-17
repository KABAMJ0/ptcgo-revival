from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import search_three_stages

card = SupporterCardDef(
    guid="6640d9ce-054f-5194-befc-348e2f2c836e",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Dawn.Name",
    display_name="Dawn",
    searchable_by=["Dawn", "Supporter"],
    subtypes=["Supporter"],
    collector_number=118,
    set_code="ME2",
    rarity=Rarities.Rare,
    effect=search_three_stages()
)
