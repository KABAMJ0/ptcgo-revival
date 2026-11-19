from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import draw_attack

card = SupporterCardDef(
    guid="473f8b5f-0d4d-5a75-a68e-09b72a4bcc7a",
    key="SWSH12TG",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FriendsinGalar.Name",
    display_name="Friends in Galar",
    searchable_by=["Friends in Galar", "Supporter"],
    subtypes=["Supporter"],
    collector_number=23,
    set_code="SWSH12TG",
    rarity=Rarities.RareUltra,
    effect=draw_attack(3)
)
