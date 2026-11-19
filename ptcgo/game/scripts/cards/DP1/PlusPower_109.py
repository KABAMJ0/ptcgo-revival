from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import turn_boost_chosen

card = ItemCardDef(
    guid="69fd2176-48c0-5434-a271-5c99e13b8ed6",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PlusPower.Name",
    display_name="PlusPower",
    searchable_by=["PlusPower", "Item"],
    subtypes=["Item"],
    collector_number=109,
    set_code="DP1",
    rarity=Rarities.Uncommon,
    effect=turn_boost_chosen(10)
)
