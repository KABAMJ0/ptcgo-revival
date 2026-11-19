from ptcgo.game.data_utils import FossilItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import FossilBodyPassive, fossil_discard_ability


card = FossilItemCardDef(
    guid="791338a4-da4b-5477-b9a9-b70c043ebfa6",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DomeFossil.Name",
    display_name="Dome Fossil",
    searchable_by=["Dome Fossil", "Item"],
    subtypes=["Item"],
    collector_number=92,
    set_code="PL4",
    rarity=Rarities.Common,
    hp=50,
    passive=FossilBodyPassive(blocks_conditions=True),
    abilities=[fossil_discard_ability()],
)
