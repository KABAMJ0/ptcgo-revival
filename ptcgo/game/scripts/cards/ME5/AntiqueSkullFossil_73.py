from ptcgo.game.data_utils import FossilItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import FossilBodyPassive, fossil_discard_ability

card = FossilItemCardDef(
    guid="a46e2788-672b-515f-838e-296ebce9f735",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AntiqueSkullFossil.Name",
    display_name="Antique Skull Fossil",
    searchable_by=["Antique Skull Fossil", "Item"],
    subtypes=["Item"],
    collector_number=73,
    set_code="ME5",
    rarity=Rarities.Common,
    hp=60, passive=FossilBodyPassive(), abilities=[fossil_discard_ability()]
)
