from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import all_of, any_of, excluding, is_basic_pokemon, is_evolution_pokemon, is_pokemon_ex

card = SupporterCardDef(
    guid="3cafbf7c-2b94-5525-81d9-bc133819cc01",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CeliosNetwork.Name",
    display_name="Celio's Network",
    searchable_by=["Celio's Network", "Supporter"],
    subtypes=["Supporter"],
    collector_number=88,
    set_code="EX6",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(all_of(any_of(is_basic_pokemon, is_evolution_pokemon), excluding(is_pokemon_ex)), count=1)
)
