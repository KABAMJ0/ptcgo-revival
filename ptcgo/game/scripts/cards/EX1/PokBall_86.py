from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import any_of, if_heads, is_basic_pokemon, is_evolution_pokemon

card = ItemCardDef(
    guid="e1e5dd66-c185-5c10-86f7-0ee7597858fd",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokBall.Name",
    display_name="Poké Ball",
    searchable_by=["Pok\u00e9 Ball", "Item"],
    subtypes=["Item"],
    collector_number=86,
    set_code="EX1",
    rarity=Rarities.Uncommon,
    effect=if_heads(search_to_hand(any_of(is_basic_pokemon, is_evolution_pokemon), count=1))
)
