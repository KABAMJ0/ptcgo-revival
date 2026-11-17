from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import if_heads, is_pokemon_card

card = ItemCardDef(
    guid="d66bc6e5-8f65-5960-97eb-eef758905fd3",
    key="G1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokBall.Name",
    display_name="Poké Ball",
    searchable_by=["Pok\u00e9 Ball", "Item"],
    subtypes=["Item"],
    collector_number=67,
    set_code="G1",
    rarity=Rarities.Uncommon,
    effect=if_heads(search_to_hand(is_pokemon_card, count=1))
)
