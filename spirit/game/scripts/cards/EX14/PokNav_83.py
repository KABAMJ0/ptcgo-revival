from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import look_at_top
from spirit.game.card_effects.trainers import any_of, is_basic_pokemon, is_energy_card, is_evolution_pokemon

card = ItemCardDef(
    guid="ca85ee98-a445-53c9-9a7e-57cc8972f51c",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokNav.Name",
    display_name="PokéNav",
    searchable_by=["Pok\u00e9Nav", "Item"],
    subtypes=["Item"],
    collector_number=83,
    set_code="EX14",
    rarity=Rarities.Uncommon,
    effect=look_at_top(3, take=1, predicate=any_of(is_basic_pokemon, is_evolution_pokemon, is_energy_card), rest="back")
)
