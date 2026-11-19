from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_in_active_spot, stadium_retreat_shift

card = StadiumCardDef(
    guid="42a29a8d-835a-5f36-8650-e918f2b9f4b6",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TheRocketsTrainingGym.Name",
    display_name="The Rocket's Training Gym",
    searchable_by=["The Rocket's Training Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=104,
    set_code="GYM1",
    rarity=Rarities.Rare,
    passive=stadium_retreat_shift(1, is_in_active_spot)
)
