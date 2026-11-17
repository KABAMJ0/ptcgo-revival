from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import is_trainer_card

card = SupporterCardDef(
    guid="4540ecef-d467-59c6-aa74-93c021d51a53",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Skyla.Name",
    display_name="Skyla",
    searchable_by=["Skyla", "Supporter"],
    subtypes=["Supporter"],
    collector_number=148,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(is_trainer_card, count=1)
)
