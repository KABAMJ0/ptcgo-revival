from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import draw_per_opponent_hand_card, is_supporter_card

card = SupporterCardDef(
    guid="2ed241a3-b3a0-5cdd-ba15-ee75a1f88815",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Clive.Name",
    display_name="Clive",
    searchable_by=["Clive", "Supporter"],
    subtypes=["Supporter"],
    collector_number=227,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    effect=draw_per_opponent_hand_card(predicate=is_supporter_card, per=2)
)
