from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import heal_item, requires_damaged_pokemon

card = ItemCardDef(
    guid="4caa253e-ae15-556b-ba22-541b14b50fd5",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Potion.Name",
    display_name="Potion",
    searchable_by=["Potion", "Item"],
    subtypes=["Item"],
    collector_number=177,
    set_code="SWSH1",
    rarity=Rarities.Uncommon,
    condition=requires_damaged_pokemon(),
    effect=heal_item(30)
)
