from ptcgo.game.data_utils import FossilItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import FossilBodyPassive, fossil_discard_ability

card = FossilItemCardDef(
    guid="2af02f87-56c8-53fe-9489-e2f7aee433cf",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MysteriousFossil.Name",
    display_name="Mysterious Fossil",
    searchable_by=["Mysterious Fossil", "Item"],
    subtypes=["Item"],
    collector_number=79,
    set_code="EX12",
    rarity=Rarities.Common,
    hp=50, passive=FossilBodyPassive(blocks_conditions=True), abilities=[fossil_discard_ability()]
)
card.prize_count = 0
