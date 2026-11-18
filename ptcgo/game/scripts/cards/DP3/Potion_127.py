from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import heal_item

card = ItemCardDef(
    guid="6a9588c0-0cd1-554c-ab63-c1cebf799f38",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Potion.Name",
    display_name="Potion",
    searchable_by=["Potion", "Item"],
    subtypes=["Item"],
    collector_number=127,
    set_code="DP3",
    rarity=Rarities.Common,
    effect=heal_item(amount=20, scope="choice")
)
