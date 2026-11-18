from ptcgo.game.data_utils import FossilItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import FossilBodyPassive, fossil_discard_ability

card = FossilItemCardDef(
    guid="b4047f72-2203-5b26-81ba-b562b7bc009d",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ClefairyDoll.Name",
    display_name="Clefairy Doll",
    searchable_by=["Clefairy Doll"],
    subtypes=[],
    collector_number=70,
    set_code="BASE1",
    rarity=Rarities.Rare,
    hp=10, passive=FossilBodyPassive(blocks_conditions=True), abilities=[fossil_discard_ability()]
)
card.prize_count = 0
