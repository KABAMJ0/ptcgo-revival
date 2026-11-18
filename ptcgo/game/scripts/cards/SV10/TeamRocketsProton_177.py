from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import all_of, is_basic_pokemon, owned_by

card = SupporterCardDef(
    guid="71411299-4113-5009-9616-0e69285014cf",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsProton.Name",
    display_name="Team Rocket's Proton",
    searchable_by=["Team Rocket's Proton", "Supporter"],
    subtypes=["Supporter"],
    collector_number=177,
    set_code="SV10",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(all_of(is_basic_pokemon, owned_by("team rocket")), count=3)
)
