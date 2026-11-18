from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_hand_no_rule_box_draw_per_card

card = SupporterCardDef(
    guid="c9a5ea52-40d8-5716-9f50-d7b9c346d98d",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Gwynn.Name",
    display_name="Gwynn",
    searchable_by=["Gwynn", "Supporter"],
    subtypes=["Supporter"],
    collector_number=109,
    set_code="ME5",
    rarity=Rarities.Rare,
    effect=discard_hand_no_rule_box_draw_per_card(3, count=2)
)
