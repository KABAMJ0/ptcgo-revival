from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import turn_boost_chosen

card = ItemCardDef(
    guid="94526f6a-cfa6-5dec-9819-2798ae52e5c8",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PlusPower.Name",
    display_name="PlusPower",
    searchable_by=["PlusPower", "Item"],
    subtypes=["Item"],
    collector_number=121,
    set_code="DP3",
    rarity=Rarities.Uncommon,
    effect=turn_boost_chosen(10)
)
