from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import heal_item

card = ItemCardDef(
    guid="fc5b182c-524d-53d2-8d5b-e92871f18317",
    key="XY0",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Potion.Name",
    display_name="Potion",
    searchable_by=["Potion", "Item"],
    subtypes=["Item"],
    collector_number=37,
    set_code="XY0",
    rarity=Rarities.Common,
    effect=heal_item(amount=30, scope="choice")
)
