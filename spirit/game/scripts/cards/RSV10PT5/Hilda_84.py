from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import all_of, is_energy_card, is_evolution_pokemon

card = SupporterCardDef(
    guid="0805f37c-37cf-5367-87a0-5621ad772ea6",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Hilda.Name",
    display_name="Hilda",
    searchable_by=["Hilda", "Supporter"],
    subtypes=["Supporter"],
    collector_number=84,
    set_code="RSV10PT5",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(all_of(is_evolution_pokemon, is_energy_card), count=1)
)
