from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import is_trainer_card

card = SupporterCardDef(
    guid="39d5627b-d8b2-58ec-894e-ac276442d1a4",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsPetrel.Name",
    display_name="Team Rocket's Petrel",
    searchable_by=["Team Rocket's Petrel", "Supporter"],
    subtypes=["Supporter"],
    collector_number=207,
    set_code="ME2PT5",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(is_trainer_card, count=1)
)
