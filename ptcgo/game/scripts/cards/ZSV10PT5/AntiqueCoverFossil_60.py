from ptcgo.game.data_utils import FossilItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import FossilBodyPassive, fossil_discard_ability

card = FossilItemCardDef(
    guid="5b2a795b-3aa5-59bc-86ba-4d5a5e06039c",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AntiqueCoverFossil.Name",
    display_name="Antique Cover Fossil",
    searchable_by=["Antique Cover Fossil", "Item"],
    subtypes=["Item"],
    collector_number=60,
    set_code="ZSV10PT5",
    rarity=Rarities.Common,
    hp=60, passive=FossilBodyPassive(), abilities=[fossil_discard_ability()]
)
