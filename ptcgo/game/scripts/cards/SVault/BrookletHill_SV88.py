from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_bench
from ptcgo.game.card_effects.trainers import all_of, any_of, is_basic_pokemon, pokemon_of, stadium_ability

card = StadiumCardDef(
    guid="5d15b7f6-57be-561f-9616-728860e17a53",
    key="SVault",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BrookletHill.Name",
    display_name="Brooklet Hill",
    searchable_by=["Brooklet Hill", "Stadium"],
    subtypes=["Stadium"],
    collector_number=88,
    set_code="SVault",
    rarity=Rarities.RareSecret,
    ability=stadium_ability('Brooklet Hill', search_to_bench(any_of(all_of(is_basic_pokemon, pokemon_of("water")), all_of(is_basic_pokemon, pokemon_of("fighting"))), 1))
)
