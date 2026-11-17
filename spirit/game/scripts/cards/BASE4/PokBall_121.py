from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import any_of, if_heads, is_basic_pokemon, is_evolution_pokemon

card = ItemCardDef(
    guid="ea0157c8-db2a-5fe7-b8a7-246b6f96f09d",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokBall.Name",
    display_name="Poké Ball",
    searchable_by=["Pok\u00e9 Ball"],
    subtypes=[],
    collector_number=121,
    set_code="BASE4",
    rarity=Rarities.Common,
    effect=if_heads(search_to_hand(any_of(is_basic_pokemon, is_evolution_pokemon), count=1))
)
