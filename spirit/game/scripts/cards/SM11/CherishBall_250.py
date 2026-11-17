from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import is_pokemon_gx

card = ItemCardDef(
    guid="93beed6a-ad2e-5997-ad4f-d723a1e6dc51",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CherishBall.Name",
    display_name="Cherish Ball",
    searchable_by=["Cherish Ball", "Item"],
    subtypes=["Item"],
    collector_number=250,
    set_code="SM11",
    rarity=Rarities.RareSecret,
    effect=search_to_hand(is_pokemon_gx, count=1)
)
