from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import is_pokemon_gx

card = ItemCardDef(
    guid="e4c3219c-86a4-5916-b99c-b1f96a23f8a8",
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
