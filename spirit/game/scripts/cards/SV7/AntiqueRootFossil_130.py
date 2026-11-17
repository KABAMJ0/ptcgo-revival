from spirit.game.data_utils import FossilItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import FossilBodyPassive, fossil_discard_ability

card = FossilItemCardDef(
    guid="4d2f3e05-3346-5374-a3c6-2f2c7effa7d5",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AntiqueRootFossil.Name",
    display_name="Antique Root Fossil",
    searchable_by=["Antique Root Fossil", "Item"],
    subtypes=["Item"],
    collector_number=130,
    set_code="SV7",
    rarity=Rarities.Common,
    hp=60, passive=FossilBodyPassive(), abilities=[fossil_discard_ability()]
)
