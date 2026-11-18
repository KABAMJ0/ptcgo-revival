from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import all_of, any_of, basic_energy_of, is_pokemon_card, owned_by

card = SupporterCardDef(
    guid="9c6f88bb-eba2-5df1-bfe1-9c57cba6c010",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EthansAdventure.Name",
    display_name="Ethan's Adventure",
    searchable_by=["Ethan's Adventure", "Supporter"],
    subtypes=["Supporter"],
    collector_number=165,
    set_code="SV10",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(any_of(all_of(is_pokemon_card, owned_by("ethan")), basic_energy_of("fire")), count=3)
)
