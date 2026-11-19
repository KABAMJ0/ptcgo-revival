from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import heal_item


card = ItemCardDef(
    guid="7a2c3aff-ac27-5a97-8ca0-7e239c97e5ee",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BigMalasada.Name",
    display_name="Big Malasada",
    searchable_by=["Big Malasada", "Item"],
    subtypes=["Item"],
    collector_number=114,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    effect=heal_item(20, scope="active", condition_cure=True),
)
