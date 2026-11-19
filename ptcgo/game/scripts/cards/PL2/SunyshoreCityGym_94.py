from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import typed_no_resistance_no_weakness

card = StadiumCardDef(
    guid="8dc7cd8e-792f-50af-a796-10c99749b6d6",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SunyshoreCityGym.Name",
    display_name="Sunyshore City Gym",
    searchable_by=["Sunyshore City Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=94,
    set_code="PL2",
    rarity=Rarities.Uncommon,
    passive=typed_no_resistance_no_weakness('lightning')
)
