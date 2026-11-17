from spirit.game.data_utils import FossilItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import FossilBodyPassive, fossil_discard_ability

card = FossilItemCardDef(
    guid="d7c7fd29-8a46-51c4-8132-5d3334ed7de7",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AntiquePlumeFossil.Name",
    display_name="Antique Plume Fossil",
    searchable_by=["Antique Plume Fossil", "Item"],
    subtypes=["Item"],
    collector_number=79,
    set_code="RSV10PT5",
    rarity=Rarities.Common,
    hp=60, passive=FossilBodyPassive(), abilities=[fossil_discard_ability()]
)
