from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import any_of, is_stadium_card, is_supporter_card

card = SupporterCardDef(
    guid="b4b4351d-1d5f-5d9e-9b70-3cf25f5bfd26",
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
