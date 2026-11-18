from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import heal_where

card = ItemCardDef(
    guid="230115f3-ff70-5fa7-8020-3b524848fb72",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ErikasKindness.Name",
    display_name="Erika's Kindness",
    searchable_by=["Erika's Kindness"],
    subtypes=[],
    collector_number=103,
    set_code="GYM2",
    rarity=Rarities.Rare,
    effect=heal_where(20, "each_both")
)
