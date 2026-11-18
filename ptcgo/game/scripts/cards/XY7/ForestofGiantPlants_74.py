from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import evolve_early_passive

card = StadiumCardDef(
    guid="aedb9e18-b3de-5561-a0ba-57491ab1a270",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ForestofGiantPlants.Name",
    display_name="Forest of Giant Plants",
    searchable_by=["Forest of Giant Plants", "Stadium"],
    subtypes=["Stadium"],
    collector_number=74,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    passive=evolve_early_passive("grass")
)
