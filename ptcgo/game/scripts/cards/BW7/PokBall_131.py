from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import if_heads, is_pokemon_card

card = ItemCardDef(
    guid="f097cce3-9f62-5b74-aa8e-cb2b53b007c0",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokBall.Name",
    display_name="Poké Ball",
    searchable_by=["Pok\u00e9 Ball", "Item"],
    subtypes=["Item"],
    collector_number=131,
    set_code="BW7",
    rarity=Rarities.Common,
    effect=if_heads(search_to_hand(is_pokemon_card, count=1))
)
