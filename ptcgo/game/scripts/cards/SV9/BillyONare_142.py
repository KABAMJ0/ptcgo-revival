from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_then_if_hand_at_least

card = SupporterCardDef(
    guid="aafc5c57-26c6-529b-aae7-003924485dbe",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BillyONare.Name",
    display_name="Billy & O'Nare",
    searchable_by=["Billy & O'Nare", "Supporter"],
    subtypes=["Supporter"],
    collector_number=142,
    set_code="SV9",
    rarity=Rarities.Common,
    effect=draw_then_if_hand_at_least(2, 10, 2)
)
