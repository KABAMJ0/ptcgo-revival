from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import is_prism_star

card = SupporterCardDef(
    guid="505bf65f-28dc-5209-87ed-3c0abc7ebfbf",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lisia.Name",
    display_name="Lisia",
    searchable_by=["Lisia", "Supporter"],
    subtypes=["Supporter"],
    collector_number=164,
    set_code="SM7",
    rarity=Rarities.RareUltra,
    effect=search_to_hand(is_prism_star, count=2)
)
