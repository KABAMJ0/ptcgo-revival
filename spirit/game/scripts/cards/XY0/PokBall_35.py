from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import if_heads, is_pokemon_card

card = ItemCardDef(
    guid="49a0c826-6d02-516d-9152-a107bb902d8a",
    key="XY0",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokBall.Name",
    display_name="Poké Ball",
    searchable_by=["Pok\u00e9 Ball", "Item"],
    subtypes=["Item"],
    collector_number=35,
    set_code="XY0",
    rarity=Rarities.Common,
    effect=if_heads(search_to_hand(is_pokemon_card, count=1))
)
