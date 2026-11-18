from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import heal_item

card = ItemCardDef(
    guid="7d1f2e4f-9288-50d2-8817-3521f9b40e2c",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Potion.Name",
    display_name="Potion",
    searchable_by=["Potion"],
    subtypes=[],
    collector_number=156,
    set_code="ECARD1",
    rarity=Rarities.Common,
    effect=heal_item(amount=20, scope="choice")
)
