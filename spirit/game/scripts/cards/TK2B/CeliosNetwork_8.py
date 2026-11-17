from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import all_of, any_of, excluding, is_basic_pokemon, is_evolution_pokemon, is_pokemon_ex

card = SupporterCardDef(
    guid="87595c4e-2fd3-5b46-a9ea-9229a1829f23",
    key="TK2B",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CeliosNetwork.Name",
    display_name="Celio's Network",
    searchable_by=["Celio's Network", "Supporter"],
    subtypes=["Supporter"],
    collector_number=8,
    set_code="TK2B",
    rarity=Rarities.Common,
    effect=search_to_hand(all_of(any_of(is_basic_pokemon, is_evolution_pokemon), excluding(is_pokemon_ex)), count=1)
)
