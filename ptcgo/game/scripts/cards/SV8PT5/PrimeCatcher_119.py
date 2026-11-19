from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import gust_then_self_switch

card = ItemCardDef(
    guid="c2cacac0-ac47-58e4-a8de-31c8588d0faf",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PrimeCatcher.Name",
    display_name="Prime Catcher",
    searchable_by=["Prime Catcher", "Item", "ACE SPEC"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=119,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    effect=gust_then_self_switch()
)
