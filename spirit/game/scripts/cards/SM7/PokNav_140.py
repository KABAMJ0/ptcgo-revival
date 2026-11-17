from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import look_at_top
from spirit.game.card_effects.trainers import any_of, is_energy_card, is_pokemon_card

card = ItemCardDef(
    guid="04c8d539-e29e-5004-9b73-2a8b785cbc48",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokNav.Name",
    display_name="PokéNav",
    searchable_by=["Pok\u00e9Nav", "Item"],
    subtypes=["Item"],
    collector_number=140,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    effect=look_at_top(3, take=1, predicate=any_of(is_pokemon_card, is_energy_card), rest="back", minimum=0)
)
