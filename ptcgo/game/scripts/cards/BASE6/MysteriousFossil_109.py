from ptcgo.game.data_utils import FossilItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import FossilBodyPassive, fossil_discard_ability

card = FossilItemCardDef(
    guid="18b2ea39-96c8-5eae-85c0-d4aacd06c58b",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MysteriousFossil.Name",
    display_name="Mysterious Fossil",
    searchable_by=["Mysterious Fossil"],
    subtypes=[],
    collector_number=109,
    set_code="BASE6",
    rarity=Rarities.Common,
    hp=10, passive=FossilBodyPassive(blocks_conditions=True), abilities=[fossil_discard_ability()]
)
card.prize_count = 0
