from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import is_pokemon_card, with_discard_cost

card = ItemCardDef(
    guid="6f677f82-e8a6-565a-b9e0-3c03444c17e5",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UltraBall.Name",
    display_name="Ultra Ball",
    searchable_by=["Ultra Ball", "Item"],
    subtypes=["Item"],
    collector_number=213,
    set_code="ME2PT5",
    rarity=Rarities.Common,
    effect=with_discard_cost(2, search_to_hand(is_pokemon_card, count=1))
)
