from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import is_pokemon_card, with_discard_cost

card = ItemCardDef(
    guid="972b5791-87f4-537e-827c-6ccc76334d75",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UltraBall.Name",
    display_name="Ultra Ball",
    searchable_by=["Ultra Ball", "Item"],
    subtypes=["Item"],
    collector_number=131,
    set_code="ME1",
    rarity=Rarities.Common,
    effect=with_discard_cost(2, search_to_hand(is_pokemon_card, count=1))
)
