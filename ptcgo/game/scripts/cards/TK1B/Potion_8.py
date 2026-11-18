from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import heal_item

card = ItemCardDef(
    guid="b99f85cc-2524-54ed-bcea-11dd3f7dd5cb",
    key="TK1B",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Potion.Name",
    display_name="Potion",
    searchable_by=["Potion", "Item"],
    subtypes=["Item"],
    collector_number=8,
    set_code="TK1B",
    rarity=Rarities.Common,
    effect=heal_item(amount=20, scope="choice")
)
