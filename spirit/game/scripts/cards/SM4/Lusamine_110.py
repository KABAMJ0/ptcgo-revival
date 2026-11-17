from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import any_of, is_stadium_card, is_supporter_card

card = SupporterCardDef(
    guid="a7f7f22d-a109-5513-b901-2238d08d02b6",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lusamine.Name",
    display_name="Lusamine",
    searchable_by=["Lusamine", "Supporter"],
    subtypes=["Supporter"],
    collector_number=110,
    set_code="SM4",
    rarity=Rarities.RareUltra,
    effect=recover_from_discard(any_of(is_supporter_card, is_stadium_card), count=2, to="hand")
)
