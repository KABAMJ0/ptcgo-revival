from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import look_at_top
from ptcgo.game.card_effects.trainers import any_of, is_basic_pokemon, is_energy_card, is_evolution_pokemon

card = ItemCardDef(
    guid="25f127f0-8444-546a-b345-6f585716f5f8",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokNav.Name",
    display_name="PokéNav",
    searchable_by=["Pok\u00e9Nav", "Item"],
    subtypes=["Item"],
    collector_number=81,
    set_code="EX9",
    rarity=Rarities.Uncommon,
    effect=look_at_top(3, take=1, predicate=any_of(is_basic_pokemon, is_evolution_pokemon, is_energy_card), rest="back")
)
