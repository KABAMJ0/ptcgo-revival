from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import heal_item

card = SupporterCardDef(
    guid="a78c6e8c-107c-5b54-b53c-659d26dbb735",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Fennel.Name",
    display_name="Fennel",
    searchable_by=["Fennel", "Supporter"],
    subtypes=["Supporter"],
    collector_number=82,
    set_code="ZSV10PT5",
    rarity=Rarities.Uncommon,
    effect=heal_item(amount=40, scope="each_own")
)
