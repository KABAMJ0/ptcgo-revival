from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import all_of, is_basic_pokemon, named

card = SupporterCardDef(
    guid="a1fc9d14-de47-52ad-9b43-a0ea54815a71",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsProton.Name",
    display_name="Team Rocket's Proton",
    searchable_by=["Team Rocket's Proton", "Supporter"],
    subtypes=["Supporter"],
    collector_number=227,
    set_code="SV10",
    rarity=Rarities.Rare,
    effect=search_to_hand(all_of(is_basic_pokemon, named("team rocket")), count=3)
)
