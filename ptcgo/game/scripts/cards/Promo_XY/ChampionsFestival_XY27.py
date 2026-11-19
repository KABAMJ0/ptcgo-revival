from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.card_effects.trainers import heal_each_with_pokemon_in_play, stadium_ability
from ptcgo.game.attributes import Rarities

card = StadiumCardDef(
    guid="18518adf-4894-548f-a27b-78bb7783abdf",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ChampionsFestival.Name",
    display_name="Champions Festival",
    searchable_by=["Champions Festival", "Stadium"],
    subtypes=["Stadium"],
    collector_number=27,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    ability=stadium_ability('Champions Festival', heal_each_with_pokemon_in_play(10, 6))
)
