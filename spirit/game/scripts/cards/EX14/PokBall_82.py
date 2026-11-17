from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import any_of, if_heads, is_basic_pokemon, is_evolution_pokemon

card = ItemCardDef(
    guid="9691db53-6f93-52fa-9b3b-32a2a0701284",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokBall.Name",
    display_name="Poké Ball",
    searchable_by=["Pok\u00e9 Ball", "Item"],
    subtypes=["Item"],
    collector_number=82,
    set_code="EX14",
    rarity=Rarities.Uncommon,
    effect=if_heads(search_to_hand(any_of(is_basic_pokemon, is_evolution_pokemon), count=1))
)
