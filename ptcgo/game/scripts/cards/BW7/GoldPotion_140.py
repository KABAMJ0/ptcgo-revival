from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import heal_where

card = ItemCardDef(
    guid="361a42e7-0c15-53e1-828d-f278212fe518",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GoldPotion.Name",
    display_name="Gold Potion",
    searchable_by=["Gold Potion", "Item", "ACE SPEC"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=140,
    set_code="BW7",
    rarity=Rarities.Rare,
    effect=heal_where(90, "active", None, min_energy=0)
)
