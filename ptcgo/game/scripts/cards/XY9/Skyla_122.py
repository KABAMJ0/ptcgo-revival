from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import is_trainer_card

card = SupporterCardDef(
    guid="0d624a79-3a54-55f5-9d9d-c047f60f556b",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Skyla.Name",
    display_name="Skyla",
    searchable_by=["Skyla", "Supporter"],
    subtypes=["Supporter"],
    collector_number=122,
    set_code="XY9",
    rarity=Rarities.RareUltra,
    effect=search_to_hand(is_trainer_card, count=1)
)
