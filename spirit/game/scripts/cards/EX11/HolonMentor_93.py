from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import all_of, is_basic_pokemon, pokemon_with_hp_at_most, with_discard_cost

card = SupporterCardDef(
    guid="96273697-7dfc-56d8-b71f-92b917da80cb",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HolonMentor.Name",
    display_name="Holon Mentor",
    searchable_by=["Holon Mentor", "Supporter"],
    subtypes=["Supporter"],
    collector_number=93,
    set_code="EX11",
    rarity=Rarities.Uncommon,
    effect=with_discard_cost(1, search_to_hand(all_of(is_basic_pokemon, pokemon_with_hp_at_most(100)), count=3))
)
