from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import abilities_off_for, any_of, is_pokemon_EX, is_pokemon_gx

card = StadiumCardDef(
    guid="e8a68e1d-2d9b-5b51-8acc-21cdd274776a",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PowerPlant.Name",
    display_name="Power Plant",
    searchable_by=["Power Plant", "Stadium"],
    subtypes=["Stadium"],
    collector_number=269,
    set_code="SM12",
    rarity=Rarities.RareSecret,
    passive=abilities_off_for(any_of(is_pokemon_gx, is_pokemon_EX))
)
