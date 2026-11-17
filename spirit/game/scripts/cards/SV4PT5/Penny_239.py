from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import is_basic_pokemon, return_pokemon_to_hand

card = SupporterCardDef(
    guid="d78f5db3-4dfa-5fcb-8c35-2015657cbad0",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Penny.Name",
    display_name="Penny",
    searchable_by=["Penny", "Supporter"],
    subtypes=["Supporter"],
    collector_number=239,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    effect=return_pokemon_to_hand(predicate=is_basic_pokemon)
)
