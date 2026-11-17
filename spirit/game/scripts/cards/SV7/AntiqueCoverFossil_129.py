from spirit.game.data_utils import FossilItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import FossilBodyPassive, fossil_discard_ability

card = FossilItemCardDef(
    guid="776f60a3-b390-5f43-a75b-742e47f8aed9",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AntiqueCoverFossil.Name",
    display_name="Antique Cover Fossil",
    searchable_by=["Antique Cover Fossil", "Item"],
    subtypes=["Item"],
    collector_number=129,
    set_code="SV7",
    rarity=Rarities.Common,
    hp=60, passive=FossilBodyPassive(), abilities=[fossil_discard_ability()]
)
