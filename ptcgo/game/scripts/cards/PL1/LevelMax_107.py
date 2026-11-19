from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.card_effects.trainers import level_max
from ptcgo.game.attributes import Rarities

card = ItemCardDef(
    guid="1629e651-c6b6-5ccd-bbe9-0e088128bd9c",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LevelMax.Name",
    display_name="Level Max",
    searchable_by=["Level Max", "Item"],
    subtypes=["Item"],
    collector_number=107,
    set_code="PL1",
    rarity=Rarities.Uncommon,
    effect=level_max
)
