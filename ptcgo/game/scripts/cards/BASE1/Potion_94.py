from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import heal_item

card = ItemCardDef(
    guid="d54dd009-991e-554a-a43e-cbc6b410056e",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Potion.Name",
    display_name="Potion",
    searchable_by=["Potion"],
    subtypes=[],
    collector_number=94,
    set_code="BASE1",
    rarity=Rarities.Common,
    effect=heal_item(amount=20, scope="choice")
)
