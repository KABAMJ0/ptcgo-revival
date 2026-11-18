from ptcgo.game.data_utils import FossilItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import FossilBodyPassive, fossil_discard_ability

card = FossilItemCardDef(
    guid="b9cea90c-cfda-587c-91a2-ffc487fbfc1f",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AntiqueArmorFossil.Name",
    display_name="Antique Armor Fossil",
    searchable_by=["Antique Armor Fossil", "Item"],
    subtypes=["Item"],
    collector_number=72,
    set_code="ME5",
    rarity=Rarities.Common,
    hp=60, passive=FossilBodyPassive(), abilities=[fossil_discard_ability()]
)
