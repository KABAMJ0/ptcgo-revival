from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import is_basic_energy_card

card = SupporterCardDef(
    guid="9d694724-7791-5d1c-8ce0-343194d7b910",
    key="SVault",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lady.Name",
    display_name="Lady",
    searchable_by=["Lady", "Supporter"],
    subtypes=["Supporter"],
    collector_number=86,
    set_code="SVault",
    rarity=Rarities.RareUltra,
    effect=search_to_hand(is_basic_energy_card, count=4)
)
