from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import recycle_from_discard

card = ItemCardDef(
    guid="08517d71-90c7-5629-b4b2-7d3db1763e53",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Recycle.Name",
    display_name="Recycle",
    searchable_by=["Recycle", "Item"],
    subtypes=["Item"],
    collector_number=96,
    set_code="BW2",
    rarity=Rarities.Uncommon,
    effect=recycle_from_discard(1)
)
