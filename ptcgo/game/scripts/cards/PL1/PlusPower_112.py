from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import turn_boost_chosen

card = ItemCardDef(
    guid="cfce6c9e-8d56-51b5-95d1-b57bc910e6aa",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PlusPower.Name",
    display_name="PlusPower",
    searchable_by=["PlusPower", "Item"],
    subtypes=["Item"],
    collector_number=112,
    set_code="PL1",
    rarity=Rarities.Uncommon,
    effect=turn_boost_chosen(10)
)
