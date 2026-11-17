from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import all_of, is_basic_energy_card, is_basic_pokemon

card = SupporterCardDef(
    guid="9c0d1a53-c416-502a-bec0-382d1b0e89a8",
    key="POP8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RoseannesResearch.Name",
    display_name="Roseanne's Research",
    searchable_by=["Roseanne's Research", "Supporter"],
    subtypes=["Supporter"],
    collector_number=11,
    set_code="POP8",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(all_of(is_basic_pokemon, is_basic_energy_card), count=2)
)
