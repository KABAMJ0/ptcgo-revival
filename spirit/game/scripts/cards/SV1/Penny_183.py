from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import is_basic_pokemon, return_pokemon_to_hand

card = SupporterCardDef(
    guid="9c866c37-f841-5f2e-8dc2-d2cbe67375f7",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Penny.Name",
    display_name="Penny",
    searchable_by=["Penny", "Supporter"],
    subtypes=["Supporter"],
    collector_number=183,
    set_code="SV1",
    rarity=Rarities.Uncommon,
    effect=return_pokemon_to_hand(predicate=is_basic_pokemon)
)
