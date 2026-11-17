from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import all_of, is_basic_pokemon, named

card = SupporterCardDef(
    guid="3637ac08-41b7-58fa-94be-cc8ff50a3624",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsProton.Name",
    display_name="Team Rocket's Proton",
    searchable_by=["Team Rocket's Proton", "Supporter"],
    subtypes=["Supporter"],
    collector_number=208,
    set_code="ME2PT5",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(all_of(is_basic_pokemon, named("team rocket")), count=3)
)
