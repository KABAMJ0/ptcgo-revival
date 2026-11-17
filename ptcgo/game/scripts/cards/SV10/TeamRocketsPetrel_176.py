from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import is_trainer_card

card = SupporterCardDef(
    guid="27759999-a630-5eba-b663-c21c5f64ad17",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsPetrel.Name",
    display_name="Team Rocket's Petrel",
    searchable_by=["Team Rocket's Petrel", "Supporter"],
    subtypes=["Supporter"],
    collector_number=176,
    set_code="SV10",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(is_trainer_card, count=1)
)
