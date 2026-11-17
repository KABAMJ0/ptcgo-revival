from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import is_pokemon_card, with_discard_cost

card = ItemCardDef(
    guid="ef4b642a-1d6b-5223-8d1d-89d1bb6a7ac6",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UltraBall.Name",
    display_name="Ultra Ball",
    searchable_by=["Ultra Ball", "Item"],
    subtypes=["Item"],
    collector_number=68,
    set_code="SL",
    rarity=Rarities.Uncommon,
    effect=with_discard_cost(2, search_to_hand(is_pokemon_card, count=1))
)
