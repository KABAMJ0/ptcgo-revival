from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import any_of, is_basic_pokemon, is_evolution_pokemon

card = SupporterCardDef(
    guid="200a9989-6a08-59f3-9fa7-6749cf43a50f",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BrocksScouting.Name",
    display_name="Brock's Scouting",
    searchable_by=["Brock's Scouting", "Supporter"],
    subtypes=["Supporter"],
    collector_number=179,
    set_code="SV9",
    rarity=Rarities.Rare,
    effect=search_to_hand(any_of(is_basic_pokemon, is_evolution_pokemon), count=2)
)
