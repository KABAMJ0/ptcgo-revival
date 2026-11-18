from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import super_potion

card = ItemCardDef(
    guid="ba4e49c8-3fab-584e-b664-207889afcbbe",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperPotion.Name",
    display_name="Super Potion",
    searchable_by=["Super Potion", "Item"],
    subtypes=["Item"],
    collector_number=128,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    effect=super_potion(60)
)
