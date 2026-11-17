from spirit.game.data_utils import FossilItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import FossilBodyPassive, fossil_discard_ability

card = FossilItemCardDef(
    guid="d36a5bb1-24f7-529b-8484-86a8d577d7f0",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AntiqueOldAmber.Name",
    display_name="Antique Old Amber",
    searchable_by=["Antique Old Amber", "Item"],
    subtypes=["Item"],
    collector_number=154,
    set_code="SV3PT5",
    rarity=Rarities.Common,
    hp=60, passive=FossilBodyPassive(), abilities=[fossil_discard_ability()]
)
