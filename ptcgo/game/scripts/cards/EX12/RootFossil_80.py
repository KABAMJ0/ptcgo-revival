from ptcgo.game.data_utils import FossilItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import FossilBodyPassive, fossil_discard_ability

card = FossilItemCardDef(
    guid="eb644d15-542d-5835-9d7b-785f7a822e9e",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RootFossil.Name",
    display_name="Root Fossil",
    searchable_by=["Root Fossil", "Item"],
    subtypes=["Item"],
    collector_number=80,
    set_code="EX12",
    rarity=Rarities.Common,
    hp=40, passive=FossilBodyPassive(blocks_conditions=True), abilities=[fossil_discard_ability()]
)
card.prize_count = 0
