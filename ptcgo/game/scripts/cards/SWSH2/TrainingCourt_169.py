from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import TRAINING_COURT_ABILITY

card = StadiumCardDef(
    guid="99b25418-beff-59e3-adee-20d807853ab0",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TrainingCourt.Name",
    display_name="Training Court",
    searchable_by=["Training Court", "Stadium"],
    subtypes=["Stadium"],
    collector_number=169,
    set_code="SWSH2",
    rarity=Rarities.Uncommon,
    ability=TRAINING_COURT_ABILITY,
)
