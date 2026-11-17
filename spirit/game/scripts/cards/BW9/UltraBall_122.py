from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import is_pokemon_card, with_discard_cost

card = ItemCardDef(
    guid="9c213040-d91d-5c46-adea-10316aaacebf",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UltraBall.Name",
    display_name="Ultra Ball",
    searchable_by=["Ultra Ball", "Item"],
    subtypes=["Item"],
    collector_number=122,
    set_code="BW9",
    rarity=Rarities.RareSecret,
    effect=with_discard_cost(2, search_to_hand(is_pokemon_card, count=1))
)
