from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_hand_no_rule_box_draw_per_card

card = SupporterCardDef(
    guid="43a98a04-dde4-5acc-804c-3aa04affe131",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Gwynn.Name",
    display_name="Gwynn",
    searchable_by=["Gwynn", "Supporter"],
    subtypes=["Supporter"],
    collector_number=78,
    set_code="ME5",
    rarity=Rarities.Uncommon,
    effect=discard_hand_no_rule_box_draw_per_card(3, count=2)
)
