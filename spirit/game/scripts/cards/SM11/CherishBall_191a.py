from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import is_pokemon_gx

card = ItemCardDef(
    guid="9a8cfa9e-1ac3-546d-aa78-919458d9ad56",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CherishBall.Name",
    display_name="Cherish Ball",
    searchable_by=["Cherish Ball", "Item"],
    subtypes=["Item"],
    collector_number=191,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(is_pokemon_gx, count=1)
)
