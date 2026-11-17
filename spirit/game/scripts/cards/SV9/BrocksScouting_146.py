from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import any_of, is_basic_pokemon, is_evolution_pokemon

card = SupporterCardDef(
    guid="1f8cabd2-07ba-585f-b8c1-11d39a5c0a62",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BrocksScouting.Name",
    display_name="Brock's Scouting",
    searchable_by=["Brock's Scouting", "Supporter"],
    subtypes=["Supporter"],
    collector_number=146,
    set_code="SV9",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(any_of(is_basic_pokemon, is_evolution_pokemon), count=2)
)
