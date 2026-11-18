from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_bench
from ptcgo.game.card_effects.trainers import all_of, any_of, is_basic_pokemon, pokemon_of, stadium_ability

card = StadiumCardDef(
    guid="5f7cfa81-4439-597b-b8fa-e4ac46729c22",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BrookletHill.Name",
    display_name="Brooklet Hill",
    searchable_by=["Brooklet Hill", "Stadium"],
    subtypes=["Stadium"],
    collector_number=120,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    ability=stadium_ability('Brooklet Hill', search_to_bench(any_of(all_of(is_basic_pokemon, pokemon_of("water")), all_of(is_basic_pokemon, pokemon_of("fighting"))), 1))
)
