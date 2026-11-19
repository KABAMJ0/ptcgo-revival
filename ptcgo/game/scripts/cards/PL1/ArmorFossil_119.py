from ptcgo.game.data_utils import FossilItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import FossilBodyPassive, fossil_discard_ability

card = FossilItemCardDef(
    guid="6e82bc8b-841b-5415-8990-2d1b13bb0617",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ArmorFossil.Name",
    display_name="Armor Fossil",
    searchable_by=["Armor Fossil", "Item"],
    subtypes=["Item"],
    collector_number=119,
    set_code="PL1",
    rarity=Rarities.Common,
    hp=50,
    passive=FossilBodyPassive(blocks_conditions=True),
    abilities=[fossil_discard_ability()],
)
