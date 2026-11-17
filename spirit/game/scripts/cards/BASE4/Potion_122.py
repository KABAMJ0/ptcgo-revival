from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import heal_item

card = ItemCardDef(
    guid="c6ba229a-85b5-57fc-8a51-c88e316c61b8",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Potion.Name",
    display_name="Potion",
    searchable_by=["Potion"],
    subtypes=[],
    collector_number=122,
    set_code="BASE4",
    rarity=Rarities.Common,
    effect=heal_item(amount=20, scope="choice")
)
