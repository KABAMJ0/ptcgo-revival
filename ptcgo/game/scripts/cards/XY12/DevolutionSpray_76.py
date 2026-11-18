from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import devolve_one

card = ItemCardDef(
    guid="fffc7ce3-749f-5fa5-94d5-c39526977302",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DevolutionSpray.Name",
    display_name="Devolution Spray",
    searchable_by=["Devolution Spray", "Item"],
    subtypes=["Item"],
    collector_number=76,
    set_code="XY12",
    rarity=Rarities.Uncommon,
    effect=devolve_one(1)
)
