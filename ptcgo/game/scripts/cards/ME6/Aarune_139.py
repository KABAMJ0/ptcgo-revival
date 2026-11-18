from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import any_of, is_stadium_card, is_supporter_card

card = SupporterCardDef(
    guid="8053a651-4579-549a-9a0c-2ae9834eae5f",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Aarune.Name",
    display_name="Aarune",
    searchable_by=["Aarune", "Supporter"],
    subtypes=["Supporter"],
    collector_number=139,
    set_code="ME6",
    rarity=Rarities.Rare,
    effect=search_to_hand(any_of(is_supporter_card, is_stadium_card), count=3)
)
