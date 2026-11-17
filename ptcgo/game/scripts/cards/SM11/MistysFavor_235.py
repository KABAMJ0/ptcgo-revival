from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import is_supporter_card

card = SupporterCardDef(
    guid="904d8793-fc6a-547a-b0ca-935336c15769",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MistysFavor.Name",
    display_name="Misty's Favor",
    searchable_by=["Misty's Favor", "Supporter"],
    subtypes=["Supporter"],
    collector_number=235,
    set_code="SM11",
    rarity=Rarities.RareUltra,
    effect=search_to_hand(is_supporter_card, count=3)
)
