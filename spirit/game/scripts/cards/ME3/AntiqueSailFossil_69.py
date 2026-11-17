from spirit.game.data_utils import FossilItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import FossilBodyPassive, fossil_discard_ability

card = FossilItemCardDef(
    guid="ea6326a0-4192-5ef2-a996-423bd0e31cf7",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AntiqueSailFossil.Name",
    display_name="Antique Sail Fossil",
    searchable_by=["Antique Sail Fossil", "Item"],
    subtypes=["Item"],
    collector_number=69,
    set_code="ME3",
    rarity=Rarities.Common,
    hp=60, passive=FossilBodyPassive(), abilities=[fossil_discard_ability()]
)
