from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import with_discard_cost

card = ItemCardDef(
    guid="f827aa15-b0c6-58a2-8fcb-21f1ccff73ac",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ComputerSearch.Name",
    display_name="Computer Search",
    searchable_by=["Computer Search", "Item", "ACE SPEC"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=137,
    set_code="BW7",
    rarity=Rarities.Rare,
    effect=with_discard_cost(2, search_to_hand(None, count=1))
)
