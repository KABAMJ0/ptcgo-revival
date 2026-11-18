from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import heal_where

card = ItemCardDef(
    guid="bf3c425b-900f-5db2-a666-62d98e1e4b1e",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.JumboIceCream.Name",
    display_name="Jumbo Ice Cream",
    searchable_by=["Jumbo Ice Cream", "Item"],
    subtypes=["Item"],
    collector_number=91,
    set_code="ME2",
    rarity=Rarities.Uncommon,
    effect=heal_where(80, "active", None, min_energy=3)
)
