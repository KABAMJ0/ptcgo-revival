from ptcgo.game.data_utils import FossilItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import FossilBodyPassive, fossil_discard_ability

card = FossilItemCardDef(
    guid="6446788d-846b-5cee-8431-09a8bae44527",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HelixFossil.Name",
    display_name="Helix Fossil",
    searchable_by=["Helix Fossil", "Item"],
    subtypes=["Item"],
    collector_number=93,
    set_code="PL4",
    rarity=Rarities.Common,
    hp=50,
    passive=FossilBodyPassive(blocks_conditions=True),
    abilities=[fossil_discard_ability()],
)
