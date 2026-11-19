from ptcgo.game.data_utils import FossilItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import FossilBodyPassive, fossil_discard_ability

card = FossilItemCardDef(
    guid="507e5460-127b-5c85-978a-591fe604c620",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SkullFossil.Name",
    display_name="Skull Fossil",
    searchable_by=["Skull Fossil", "Item"],
    subtypes=["Item"],
    collector_number=120,
    set_code="PL1",
    rarity=Rarities.Common,
    hp=50,
    passive=FossilBodyPassive(blocks_conditions=True),
    abilities=[fossil_discard_ability()],
)
