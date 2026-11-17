from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_from_opponent_hand, is_item_card

card = SupporterCardDef(
    guid="de20ecd7-8cc2-5686-b6a8-3a2ba9dcf6a2",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Eri.Name",
    display_name="Eri",
    searchable_by=["Eri", "Supporter"],
    subtypes=["Supporter"],
    collector_number=136,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    effect=discard_from_opponent_hand(predicate=is_item_card, count=2)
)
