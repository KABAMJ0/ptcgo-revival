from ptcgo.game.data_utils import FossilItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import FossilBodyPassive, fossil_discard_ability

card = FossilItemCardDef(
    guid="976c54d0-e02d-5f4d-84a9-e20a6e2dba23",
    key="DP2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SkullFossil.Name",
    display_name="Skull Fossil",
    searchable_by=["Skull Fossil", "Item"],
    subtypes=["Item"],
    collector_number=117,
    set_code="DP2",
    rarity=Rarities.Common,
    hp=50,
    passive=FossilBodyPassive(blocks_conditions=True),
    abilities=[fossil_discard_ability()],
)
