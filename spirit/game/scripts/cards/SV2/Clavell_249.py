from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import all_of, is_basic_pokemon, pokemon_with_hp_at_most

card = SupporterCardDef(
    guid="8d51956d-2f6a-54d0-82cb-d6146a02ad4c",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Clavell.Name",
    display_name="Clavell",
    searchable_by=["Clavell", "Supporter"],
    subtypes=["Supporter"],
    collector_number=249,
    set_code="SV2",
    rarity=Rarities.Rare,
    effect=search_to_hand(all_of(is_basic_pokemon, pokemon_with_hp_at_most(120)), count=3)
)
