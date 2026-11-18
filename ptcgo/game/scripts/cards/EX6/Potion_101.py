from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import heal_item

card = ItemCardDef(
    guid="61d986d2-732f-52c8-9036-f83216df1fde",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Potion.Name",
    display_name="Potion",
    searchable_by=["Potion", "Item"],
    subtypes=["Item"],
    collector_number=101,
    set_code="EX6",
    rarity=Rarities.Common,
    effect=heal_item(amount=20, scope="choice")
)
