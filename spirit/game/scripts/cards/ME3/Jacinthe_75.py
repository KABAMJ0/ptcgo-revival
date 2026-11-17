from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import heal_item

card = SupporterCardDef(
    guid="22fed7a7-bd29-5a06-a06b-b30799ee0d93",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Jacinthe.Name",
    display_name="Jacinthe",
    searchable_by=["Jacinthe", "Supporter"],
    subtypes=["Supporter"],
    collector_number=75,
    set_code="ME3",
    rarity=Rarities.Uncommon,
    effect=heal_item(amount=150, scope="choice")
)
