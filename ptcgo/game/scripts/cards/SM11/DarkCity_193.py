from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import all_of, is_basic_pokemon, pokemon_of, stadium_no_retreat

card = StadiumCardDef(
    guid="514ebc7f-bc7d-5240-ae25-3bfb27344360",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DarkCity.Name",
    display_name="Dark City",
    searchable_by=["Dark City", "Stadium"],
    subtypes=["Stadium"],
    collector_number=193,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    passive=stadium_no_retreat(all_of(is_basic_pokemon, pokemon_of("darkness")))
)
