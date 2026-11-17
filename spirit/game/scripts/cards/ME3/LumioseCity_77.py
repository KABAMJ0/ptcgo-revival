from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_bench
from spirit.game.card_effects.trainers import ends_turn_after, is_basic_pokemon, stadium_ability

card = StadiumCardDef(
    guid="3cd8104d-bec6-523f-88db-9ea26e408770",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LumioseCity.Name",
    display_name="Lumiose City",
    searchable_by=["Lumiose City", "Stadium"],
    subtypes=["Stadium"],
    collector_number=77,
    set_code="ME3",
    rarity=Rarities.Uncommon,
    ability=stadium_ability('Lumiose City', ends_turn_after(search_to_bench(is_basic_pokemon, 1)))
)
