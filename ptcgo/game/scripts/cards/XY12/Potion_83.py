from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import heal_item

card = ItemCardDef(
    guid="73751f7c-efe3-5a0a-8c04-f59dac56911a",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Potion.Name",
    display_name="Potion",
    searchable_by=["Potion", "Item"],
    subtypes=["Item"],
    collector_number=83,
    set_code="XY12",
    rarity=Rarities.Uncommon,
    effect=heal_item(amount=30, scope="choice")
)
