from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import any_of, is_stadium_card, is_supporter_card

card = SupporterCardDef(
    guid="818de1d4-6a4e-585f-af57-b03b0b3a7dd9",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lusamine.Name",
    display_name="Lusamine",
    searchable_by=["Lusamine", "Supporter"],
    subtypes=["Supporter"],
    collector_number=96,
    set_code="SM4",
    rarity=Rarities.Uncommon,
    effect=recover_from_discard(any_of(is_supporter_card, is_stadium_card), count=2, to="hand")
)
