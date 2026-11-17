from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import is_pokemon_card, with_discard_cost

card = ItemCardDef(
    guid="a0d4b655-f3bb-563c-b9c1-79ea425d7a65",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UltraBall.Name",
    display_name="Ultra Ball",
    searchable_by=["Ultra Ball", "Item"],
    subtypes=["Item"],
    collector_number=161,
    set_code="SM1",
    rarity=Rarities.RareSecret,
    effect=with_discard_cost(2, search_to_hand(is_pokemon_card, count=1))
)
