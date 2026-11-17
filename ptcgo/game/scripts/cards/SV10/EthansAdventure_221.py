from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import all_of, any_of, basic_energy_of, is_pokemon_card, named

card = SupporterCardDef(
    guid="4a56b316-a851-55ca-8952-92e14bef6051",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EthansAdventure.Name",
    display_name="Ethan's Adventure",
    searchable_by=["Ethan's Adventure", "Supporter"],
    subtypes=["Supporter"],
    collector_number=221,
    set_code="SV10",
    rarity=Rarities.Rare,
    effect=search_to_hand(any_of(all_of(is_pokemon_card, named("ethan")), basic_energy_of("fire")), count=3)
)
