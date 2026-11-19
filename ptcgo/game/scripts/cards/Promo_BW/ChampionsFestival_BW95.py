from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.card_effects.trainers import heal_each_with_pokemon_in_play, stadium_ability
from ptcgo.game.attributes import Rarities

card = StadiumCardDef(
    guid="2bf36470-e0ed-5ace-8902-e76fba2b0ec0",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ChampionsFestival.Name",
    display_name="Champions Festival",
    searchable_by=["Champions Festival", "Stadium"],
    subtypes=["Stadium"],
    collector_number=95,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    ability=stadium_ability('Champions Festival', heal_each_with_pokemon_in_play(10, 6))
)
