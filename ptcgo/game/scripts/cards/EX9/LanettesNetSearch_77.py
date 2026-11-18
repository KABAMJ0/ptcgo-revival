from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import all_of, excluding, is_basic_pokemon, pokemon_of_subtype, search_distinct_types

card = SupporterCardDef(
    guid="72952279-5dd3-51ef-b4e4-ed23fe287d86",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LanettesNetSearch.Name",
    display_name="Lanette's Net Search",
    searchable_by=["Lanette's Net Search", "Supporter"],
    subtypes=["Supporter"],
    collector_number=77,
    set_code="EX9",
    rarity=Rarities.Uncommon,
    effect=search_distinct_types(all_of(is_basic_pokemon, excluding(pokemon_of_subtype("Baby"))), 3)
)
