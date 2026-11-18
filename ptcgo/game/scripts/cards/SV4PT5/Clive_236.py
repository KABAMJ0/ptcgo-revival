from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_per_opponent_hand_card, is_supporter_card

card = SupporterCardDef(
    guid="9aee2b88-4b44-5703-a9f0-a0306b7d3e13",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Clive.Name",
    display_name="Clive",
    searchable_by=["Clive", "Supporter"],
    subtypes=["Supporter"],
    collector_number=236,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    effect=draw_per_opponent_hand_card(predicate=is_supporter_card, per=2)
)
