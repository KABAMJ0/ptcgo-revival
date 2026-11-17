from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_bench
from spirit.game.card_effects.trainers import ends_turn_after, is_basic_pokemon, stadium_ability

card = StadiumCardDef(
    guid="76e936e6-c824-5be1-b10f-0c8ad89fa800",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LumioseCity.Name",
    display_name="Lumiose City",
    searchable_by=["Lumiose City", "Stadium"],
    subtypes=["Stadium"],
    collector_number=111,
    set_code="ME3",
    rarity=Rarities.Rare,
    ability=stadium_ability('Lumiose City', ends_turn_after(search_to_bench(is_basic_pokemon, 1)))
)
