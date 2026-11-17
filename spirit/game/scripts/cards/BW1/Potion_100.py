from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import heal_item

card = ItemCardDef(
    guid="d8e89b92-f9ec-5e3a-a7fe-baa886639e94",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Potion.Name",
    display_name="Potion",
    searchable_by=["Potion", "Item"],
    subtypes=["Item"],
    collector_number=100,
    set_code="BW1",
    rarity=Rarities.Common,
    effect=heal_item(amount=30, scope="choice")
)
