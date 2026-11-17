from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import any_of, if_heads, is_basic_pokemon, is_evolution_pokemon

card = ItemCardDef(
    guid="4b0489f7-d7e0-5b1c-a27b-a73dc98e6867",
    key="BASE2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokBall.Name",
    display_name="Poké Ball",
    searchable_by=["Pok\u00e9 Ball"],
    subtypes=[],
    collector_number=64,
    set_code="BASE2",
    rarity=Rarities.Common,
    effect=if_heads(search_to_hand(any_of(is_basic_pokemon, is_evolution_pokemon), count=1))
)
