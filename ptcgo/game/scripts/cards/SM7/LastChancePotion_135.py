from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import heal_chosen

card = ItemCardDef(
    guid="ae195811-c19a-598c-97b5-c879564382f6",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LastChancePotion.Name",
    display_name="Last Chance Potion",
    searchable_by=["Last Chance Potion", "Item"],
    subtypes=["Item"],
    collector_number=135,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    effect=heal_chosen(120, count=1, hp_at_most=30)
)
