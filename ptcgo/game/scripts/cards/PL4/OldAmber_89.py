from ptcgo.game.data_utils import FossilItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import FossilBodyPassive, fossil_discard_ability


card = FossilItemCardDef(
    guid="bdf5470b-d68e-513d-bc99-90369ace7eee",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.OldAmber.Name",
    display_name="Old Amber",
    searchable_by=["Old Amber", "Item"],
    subtypes=["Item"],
    collector_number=89,
    set_code="PL4",
    rarity=Rarities.Common,
    hp=50,
    passive=FossilBodyPassive(blocks_conditions=True),
    abilities=[fossil_discard_ability()],
)
