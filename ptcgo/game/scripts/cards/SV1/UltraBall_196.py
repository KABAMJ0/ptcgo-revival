from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import is_pokemon_card, with_discard_cost

card = ItemCardDef(
    guid="c5175f9b-a85d-54e7-945c-02b537ed4d8f",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UltraBall.Name",
    display_name="Ultra Ball",
    searchable_by=["Ultra Ball", "Item"],
    subtypes=["Item"],
    collector_number=196,
    set_code="SV1",
    rarity=Rarities.Uncommon,
    effect=with_discard_cost(2, search_to_hand(is_pokemon_card, count=1))
)
