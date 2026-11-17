from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_bench
from ptcgo.game.card_effects.trainers import all_of, excluding, is_basic_pokemon, is_pokemon_ex

card = ItemCardDef(
    guid="9859277c-0cce-53d7-a80c-c62ee1df5845",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GreatBall.Name",
    display_name="Great Ball",
    searchable_by=["Great Ball", "Item"],
    subtypes=["Item"],
    collector_number=92,
    set_code="EX6",
    rarity=Rarities.Uncommon,
    effect=search_to_bench(all_of(is_basic_pokemon, excluding(is_pokemon_ex)), 1)
)
