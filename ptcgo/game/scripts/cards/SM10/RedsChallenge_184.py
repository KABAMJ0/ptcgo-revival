from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import with_discard_cost

card = SupporterCardDef(
    guid="878ce0c1-8979-539b-a8c1-3bbe352c0a68",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RedsChallenge.Name",
    display_name="Red's Challenge",
    searchable_by=["Red's Challenge", "Supporter"],
    subtypes=["Supporter"],
    collector_number=184,
    set_code="SM10",
    rarity=Rarities.RareHolo,
    effect=with_discard_cost(2, search_to_hand(None, count=1))
)
