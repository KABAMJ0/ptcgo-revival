from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import with_discard_cost

card = SupporterCardDef(
    guid="1c25a0e6-dc5b-5480-98b2-48cb7264aa8e",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RedsChallenge.Name",
    display_name="Red's Challenge",
    searchable_by=["Red's Challenge", "Supporter"],
    subtypes=["Supporter"],
    collector_number=213,
    set_code="SM10",
    rarity=Rarities.RareUltra,
    effect=with_discard_cost(2, search_to_hand(None, count=1))
)
