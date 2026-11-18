from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import devolve_one

card = ItemCardDef(
    guid="596eb03a-6cff-5ba6-8a9e-e3fb245b2630",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DevolutionSpray.Name",
    display_name="Devolution Spray",
    searchable_by=["Devolution Spray", "Item"],
    subtypes=["Item"],
    collector_number=95,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    effect=devolve_one(1)
)
