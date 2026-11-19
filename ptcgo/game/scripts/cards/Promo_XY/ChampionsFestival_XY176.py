from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.card_effects.trainers import heal_each_with_pokemon_in_play, stadium_ability
from ptcgo.game.attributes import Rarities

card = StadiumCardDef(
    guid="9bcd0311-7133-5c36-b213-f77c64312bb9",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ChampionsFestival.Name",
    display_name="Champions Festival",
    searchable_by=["Champions Festival", "Stadium"],
    subtypes=["Stadium"],
    collector_number=176,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    ability=stadium_ability('Champions Festival', heal_each_with_pokemon_in_play(10, 6))
)
