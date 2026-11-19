from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.card_effects.trainers import heal_each_with_pokemon_in_play, stadium_ability
from ptcgo.game.attributes import Rarities

card = StadiumCardDef(
    guid="0e80c2d3-ba27-54e5-87f0-fe658fe26278",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ChampionsFestival.Name",
    display_name="Champions Festival",
    searchable_by=["Champions Festival", "Stadium"],
    subtypes=["Stadium"],
    collector_number=78,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    ability=stadium_ability('Champions Festival', heal_each_with_pokemon_in_play(10, 6))
)
