from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import is_pokemon_EX, pokemon_of, stadium_damage_boost

card = StadiumCardDef(
    guid="d32c8e6b-3a8f-5b02-a431-15c3145fa013",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FightingStadium.Name",
    display_name="Fighting Stadium",
    searchable_by=["Fighting Stadium", "Stadium"],
    subtypes=["Stadium"],
    collector_number=90,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    passive=stadium_damage_boost(20, pokemon_of("fighting"), target=is_pokemon_EX)
)
