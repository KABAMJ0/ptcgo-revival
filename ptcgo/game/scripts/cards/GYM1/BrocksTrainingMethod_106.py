from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import all_of, any_of, card_named_contains, is_basic_pokemon, is_evolution_pokemon

card = ItemCardDef(
    guid="366c7650-ebff-5de4-b32b-80a20bd0600a",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BrocksTrainingMethod.Name",
    display_name="Brock's Training Method",
    searchable_by=["Brock's Training Method"],
    subtypes=[],
    collector_number=106,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(all_of(any_of(is_basic_pokemon, is_evolution_pokemon), card_named_contains('brock')), count=1)
)
