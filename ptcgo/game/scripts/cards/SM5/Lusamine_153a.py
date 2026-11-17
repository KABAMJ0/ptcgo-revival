from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.card_effects.trainers import any_of, is_stadium_card, is_supporter_card

card = SupporterCardDef(
    guid="d8fddfb2-f391-52fa-b8bc-f39586a2e960",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lusamine.Name",
    display_name="Lusamine",
    searchable_by=["Lusamine", "Supporter"],
    subtypes=["Supporter"],
    collector_number=153,
    set_code="SM5",
    rarity=Rarities.RareUltra,
    effect=recover_from_discard(any_of(is_supporter_card, is_stadium_card), count=2, to="hand")
)
