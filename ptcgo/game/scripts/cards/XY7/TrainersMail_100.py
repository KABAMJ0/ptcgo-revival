from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities

card = ItemCardDef(
    guid="ab14acf2-41de-5fb0-b424-f7c10e446763",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TrainersMail.Name",
    display_name="Trainers' Mail",
    searchable_by=["Trainers' Mail", "Item"],
    subtypes=["Item"],
    collector_number=100,
    set_code="XY7",
    rarity=Rarities.RareSecret,
    effect=unimplemented
)
