from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import pokemon_named, stadium_retreat_shift

card = StadiumCardDef(
    guid="b06ff56d-2204-5fec-84a3-4398d36e4545",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CeruleanCityGym.Name",
    display_name="Cerulean City Gym",
    searchable_by=["Cerulean City Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=108,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    passive=stadium_retreat_shift(-1, pokemon_named('misty'))
)
