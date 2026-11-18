from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import abilities_off_for, any_of, is_pokemon_EX, is_pokemon_gx

card = StadiumCardDef(
    guid="247b5520-cbb1-5b07-8890-00e4bf8b64a4",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PowerPlant.Name",
    display_name="Power Plant",
    searchable_by=["Power Plant", "Stadium"],
    subtypes=["Stadium"],
    collector_number=183,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    passive=abilities_off_for(any_of(is_pokemon_gx, is_pokemon_EX))
)
