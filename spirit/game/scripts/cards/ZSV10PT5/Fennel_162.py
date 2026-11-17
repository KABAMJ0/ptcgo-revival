from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import heal_item

card = SupporterCardDef(
    guid="07a9d67c-84ba-575e-9dde-ecd72fb17ed4",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Fennel.Name",
    display_name="Fennel",
    searchable_by=["Fennel", "Supporter"],
    subtypes=["Supporter"],
    collector_number=162,
    set_code="ZSV10PT5",
    rarity=Rarities.Rare,
    effect=heal_item(amount=40, scope="each_own")
)
