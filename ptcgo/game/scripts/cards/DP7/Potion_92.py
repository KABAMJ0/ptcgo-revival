from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import heal_item

card = ItemCardDef(
    guid="b4f031af-021c-55f2-b952-0223a54becbb",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Potion.Name",
    display_name="Potion",
    searchable_by=["Potion", "Item"],
    subtypes=["Item"],
    collector_number=92,
    set_code="DP7",
    rarity=Rarities.Common,
    effect=heal_item(amount=20, scope="choice")
)
