from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import super_potion

card = ItemCardDef(
    guid="b81031be-c19d-5c53-bab4-175f89fe8d30",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperPotion.Name",
    display_name="Super Potion",
    searchable_by=["Super Potion", "Item"],
    subtypes=["Item"],
    collector_number=158,
    set_code="SV9",
    rarity=Rarities.Uncommon,
    effect=super_potion(60)
)
