from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import with_discard_cost

card = ItemCardDef(
    guid="7c865218-6d19-5016-b199-e353d3542aff",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ComputerSearch.Name",
    display_name="Computer Search",
    searchable_by=["Computer Search"],
    subtypes=[],
    collector_number=101,
    set_code="BASE4",
    rarity=Rarities.Rare,
    effect=with_discard_cost(2, search_to_hand(None, count=1))
)
