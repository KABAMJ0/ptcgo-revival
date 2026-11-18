from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import any_of, card_named_contains, is_tool_card

card = SupporterCardDef(
    guid="c0fe7623-f237-5205-a417-776add2aaa3b",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TravelingSalesman.Name",
    display_name="Traveling Salesman",
    searchable_by=["Traveling Salesman", "Supporter"],
    subtypes=["Supporter"],
    collector_number=137,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(any_of(is_tool_card, card_named_contains('technical machine')), count=2)
)
