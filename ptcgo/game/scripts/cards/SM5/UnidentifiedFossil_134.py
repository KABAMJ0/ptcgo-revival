from ptcgo.game.data_utils import FossilItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import FossilBodyPassive, fossil_discard_ability

card = FossilItemCardDef(
    guid="e2ccaf21-019e-5810-a5c6-2140ec999467",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UnidentifiedFossil.Name",
    display_name="Unidentified Fossil",
    searchable_by=["Unidentified Fossil", "Item"],
    subtypes=["Item"],
    collector_number=134,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    hp=60, passive=FossilBodyPassive(), abilities=[fossil_discard_ability()]
)
