from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import if_heads, is_pokemon_card

card = ItemCardDef(
    guid="993aeed0-962b-504b-a786-6834b2f375bf",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokBall.Name",
    display_name="Poké Ball",
    searchable_by=["Pok\u00e9 Ball", "Item"],
    subtypes=["Item"],
    collector_number=185,
    set_code="SV1",
    rarity=Rarities.Common,
    effect=if_heads(search_to_hand(is_pokemon_card, count=1))
)
