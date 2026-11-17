from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import heal_item

card = SupporterCardDef(
    guid="f23ef764-45b6-53a1-b8c2-8f05e924dd33",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Jacinthe.Name",
    display_name="Jacinthe",
    searchable_by=["Jacinthe", "Supporter"],
    subtypes=["Supporter"],
    collector_number=122,
    set_code="ME3",
    rarity=Rarities.Rare,
    effect=heal_item(amount=150, scope="choice")
)
