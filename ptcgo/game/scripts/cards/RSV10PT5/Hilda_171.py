from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import all_of, is_energy_card, is_evolution_pokemon

card = SupporterCardDef(
    guid="efbea99b-6560-5de6-9222-669d5cef5ae0",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Hilda.Name",
    display_name="Hilda",
    searchable_by=["Hilda", "Supporter"],
    subtypes=["Supporter"],
    collector_number=171,
    set_code="RSV10PT5",
    rarity=Rarities.Rare,
    effect=search_to_hand(all_of(is_evolution_pokemon, is_energy_card), count=1)
)
