from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import with_discard_cost

card = ItemCardDef(
    guid="cbeac06c-8bf8-5c29-a596-955ff0f2445c",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ComputerSearch.Name",
    display_name="Computer Search",
    searchable_by=["Computer Search"],
    subtypes=[],
    collector_number=71,
    set_code="BASE1",
    rarity=Rarities.Rare,
    effect=with_discard_cost(2, search_to_hand(None, count=1))
)
