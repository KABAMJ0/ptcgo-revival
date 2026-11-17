from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import all_of, is_basic_pokemon, pokemon_with_hp_at_most, with_discard_cost

card = SupporterCardDef(
    guid="56487d85-6838-5dbc-950b-643b06ce73c8",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HolonMentor.Name",
    display_name="Holon Mentor",
    searchable_by=["Holon Mentor", "Supporter"],
    subtypes=["Supporter"],
    collector_number=75,
    set_code="EX15",
    rarity=Rarities.Uncommon,
    effect=with_discard_cost(1, search_to_hand(all_of(is_basic_pokemon, pokemon_with_hp_at_most(100)), count=3))
)
