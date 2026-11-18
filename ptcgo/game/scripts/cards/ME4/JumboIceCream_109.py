from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import heal_where

card = ItemCardDef(
    guid="8f362e2a-76d8-5cc5-9288-305a68f9fce6",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.JumboIceCream.Name",
    display_name="Jumbo Ice Cream",
    searchable_by=["Jumbo Ice Cream", "Item"],
    subtypes=["Item"],
    collector_number=109,
    set_code="ME4",
    rarity=Rarities.Rare,
    effect=heal_where(80, "active", None, min_energy=3)
)
