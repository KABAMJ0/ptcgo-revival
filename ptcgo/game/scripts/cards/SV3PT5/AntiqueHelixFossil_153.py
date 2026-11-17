from ptcgo.game.data_utils import FossilItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import FossilBodyPassive, fossil_discard_ability

card = FossilItemCardDef(
    guid="b500d3cb-ce10-5632-a8aa-325059584f49",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AntiqueHelixFossil.Name",
    display_name="Antique Helix Fossil",
    searchable_by=["Antique Helix Fossil", "Item"],
    subtypes=["Item"],
    collector_number=153,
    set_code="SV3PT5",
    rarity=Rarities.Common,
    hp=60, passive=FossilBodyPassive(), abilities=[fossil_discard_ability()]
)
