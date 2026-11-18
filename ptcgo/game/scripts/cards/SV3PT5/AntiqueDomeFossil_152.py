from ptcgo.game.data_utils import FossilItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import FossilBodyPassive, fossil_discard_ability

card = FossilItemCardDef(
    guid="7a9a3cf8-041b-53a4-b40f-57efa201c75c",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AntiqueDomeFossil.Name",
    display_name="Antique Dome Fossil",
    searchable_by=["Antique Dome Fossil", "Item"],
    subtypes=["Item"],
    collector_number=152,
    set_code="SV3PT5",
    rarity=Rarities.Common,
    hp=60, passive=FossilBodyPassive(), abilities=[fossil_discard_ability()]
)
