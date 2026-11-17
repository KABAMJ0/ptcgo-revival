from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import heal_item

card = SupporterCardDef(
    guid="2c9f13c3-3860-592f-9fa8-d73f6a2b6c71",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Jacinthe.Name",
    display_name="Jacinthe",
    searchable_by=["Jacinthe", "Supporter"],
    subtypes=["Supporter"],
    collector_number=110,
    set_code="ME3",
    rarity=Rarities.Rare,
    effect=heal_item(amount=150, scope="choice")
)
