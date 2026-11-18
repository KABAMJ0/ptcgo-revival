from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import draw_attack

card = SupporterCardDef(
    guid="d73c8c29-ff5d-587d-befd-99ef44c401ba",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FriendsinSinnoh.Name",
    display_name="Friends in Sinnoh",
    searchable_by=["Friends in Sinnoh", "Supporter"],
    subtypes=["Supporter"],
    collector_number=149,
    set_code="CZ",
    rarity=Rarities.RareUltra,
    effect=draw_attack(3)
)
