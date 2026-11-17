from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import is_pokemon_card, with_discard_cost

card = ItemCardDef(
    guid="b1e1bab4-fd2a-516f-8fed-22e0d9708638",
    key="ME55",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UltraBall.Name",
    display_name="Ultra Ball",
    searchable_by=["Ultra Ball", "Item"],
    subtypes=["Item"],
    collector_number=128,
    set_code="ME55",
    rarity=Rarities.Common,
    effect=with_discard_cost(2, search_to_hand(is_pokemon_card, count=1))
)
