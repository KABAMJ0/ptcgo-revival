from ptcgo.game.data_utils import FossilItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import FossilBodyPassive, fossil_discard_ability

card = FossilItemCardDef(
    guid="fa34c662-3f2c-513c-b977-69f0dbad66e4",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AntiqueJawFossil.Name",
    display_name="Antique Jaw Fossil",
    searchable_by=["Antique Jaw Fossil", "Item"],
    subtypes=["Item"],
    collector_number=68,
    set_code="ME3",
    rarity=Rarities.Common,
    hp=60, passive=FossilBodyPassive(), abilities=[fossil_discard_ability()]
)
