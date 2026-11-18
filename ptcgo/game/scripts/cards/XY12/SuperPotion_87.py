from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import super_potion

card = ItemCardDef(
    guid="6360d78f-5eb0-5b72-bedb-451978952eca",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperPotion.Name",
    display_name="Super Potion",
    searchable_by=["Super Potion", "Item"],
    subtypes=["Item"],
    collector_number=87,
    set_code="XY12",
    rarity=Rarities.Uncommon,
    effect=super_potion(60)
)
