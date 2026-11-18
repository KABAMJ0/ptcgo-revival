from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import heal_item

card = ItemCardDef(
    guid="dc77866f-0d84-527f-af8b-a2e88b40b10f",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Potion.Name",
    display_name="Potion",
    searchable_by=["Potion", "Item"],
    subtypes=["Item"],
    collector_number=87,
    set_code="EX14",
    rarity=Rarities.Common,
    effect=heal_item(amount=20, scope="choice")
)
