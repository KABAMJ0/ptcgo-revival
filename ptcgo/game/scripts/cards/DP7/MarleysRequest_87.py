from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import any_of, is_stadium_card, is_supporter_card, is_trainer_card, opponent_chooses_discard_take

card = SupporterCardDef(
    guid="95179315-1d39-5ea7-a6f3-90fbb0befae9",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MarleysRequest.Name",
    display_name="Marley's Request",
    searchable_by=["Marley's Request", "Supporter"],
    subtypes=["Supporter"],
    collector_number=87,
    set_code="DP7",
    rarity=Rarities.Uncommon,
    effect=opponent_chooses_discard_take(any_of(is_trainer_card, is_supporter_card, is_stadium_card))
)
