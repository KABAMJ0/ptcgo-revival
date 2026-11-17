from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import all_of, is_basic_energy_card, is_basic_pokemon

card = SupporterCardDef(
    guid="08e613b5-6a9e-5b82-ab58-d87070f8b593",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RoseannesResearch.Name",
    display_name="Roseanne's Research",
    searchable_by=["Roseanne's Research", "Supporter"],
    subtypes=["Supporter"],
    collector_number=125,
    set_code="DP3",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(all_of(is_basic_pokemon, is_basic_energy_card), count=2)
)
