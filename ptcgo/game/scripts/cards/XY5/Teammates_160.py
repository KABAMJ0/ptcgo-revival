from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import knocked_out_last_turn

card = SupporterCardDef(
    guid="310ed132-2054-5afe-9fa4-dc2684a83865",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Teammates.Name",
    display_name="Teammates",
    searchable_by=["Teammates", "Supporter"],
    subtypes=["Supporter"],
    collector_number=160,
    set_code="XY5",
    rarity=Rarities.RareUltra,
    effect=search_to_hand(None, count=2), condition=knocked_out_last_turn()
)
