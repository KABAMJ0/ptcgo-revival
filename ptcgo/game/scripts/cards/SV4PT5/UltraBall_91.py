from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import is_pokemon_card, with_discard_cost

card = ItemCardDef(
    guid="869269a5-ac83-58fc-85a6-1f0aa370c539",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UltraBall.Name",
    display_name="Ultra Ball",
    searchable_by=["Ultra Ball", "Item"],
    subtypes=["Item"],
    collector_number=91,
    set_code="SV4PT5",
    rarity=Rarities.Uncommon,
    effect=with_discard_cost(2, search_to_hand(is_pokemon_card, count=1))
)
