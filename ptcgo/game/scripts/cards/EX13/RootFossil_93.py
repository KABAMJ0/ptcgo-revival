from ptcgo.game.data_utils import FossilItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import FossilBodyPassive, fossil_discard_ability

card = FossilItemCardDef(
    guid="a4e3d313-4e54-541b-82c4-d885f56afcd7",
    key="EX13",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RootFossil.Name",
    display_name="Root Fossil",
    searchable_by=["Root Fossil", "Item"],
    subtypes=["Item"],
    collector_number=93,
    set_code="EX13",
    rarity=Rarities.Common,
    hp=40, passive=FossilBodyPassive(blocks_conditions=True), abilities=[fossil_discard_ability()]
)
card.prize_count = 0
