from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import any_of, is_stadium_card, is_supporter_card

card = SupporterCardDef(
    guid="9398ccf9-9829-54e1-a7da-af8e19b7b762",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Aarune.Name",
    display_name="Aarune",
    searchable_by=["Aarune", "Supporter"],
    subtypes=["Supporter"],
    collector_number=89,
    set_code="ME6",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(any_of(is_supporter_card, is_stadium_card), count=3)
)
