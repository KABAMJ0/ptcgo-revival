from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import look_at_top
from spirit.game.card_effects.trainers import any_of, is_basic_pokemon, is_energy_card, is_evolution_pokemon

card = ItemCardDef(
    guid="1aea3327-5b65-5f73-a3ca-bd2822bd2c45",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokNav.Name",
    display_name="PokéNav",
    searchable_by=["Pok\u00e9Nav", "Item"],
    subtypes=["Item"],
    collector_number=88,
    set_code="EX1",
    rarity=Rarities.Uncommon,
    effect=look_at_top(3, take=1, predicate=any_of(is_basic_pokemon, is_evolution_pokemon, is_energy_card), rest="back")
)
