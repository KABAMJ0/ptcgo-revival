from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.card_effects.trainers import heal_each_with_pokemon_in_play, stadium_ability
from ptcgo.game.attributes import Rarities

card = StadiumCardDef(
    guid="83751a88-bd2d-5f9f-b52f-baba3ce577f1",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ChampionsFestival.Name",
    display_name="Champions Festival",
    searchable_by=["Champions Festival", "Stadium"],
    subtypes=["Stadium"],
    collector_number=91,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    ability=stadium_ability('Champions Festival', heal_each_with_pokemon_in_play(10, 6))
)
