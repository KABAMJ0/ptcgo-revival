from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import heal_item

card = ItemCardDef(
    guid="11bd62dd-de9c-54a4-8e20-ffb34b023e13",
    key="TK1A",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Potion.Name",
    display_name="Potion",
    searchable_by=["Potion", "Item"],
    subtypes=["Item"],
    collector_number=8,
    set_code="TK1A",
    rarity=Rarities.Common,
    effect=heal_item(amount=20, scope="choice")
)
