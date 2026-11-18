from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_bench
from ptcgo.game.card_effects.trainers import BENCH_CAPACITY, is_basic_pokemon

card = ItemCardDef(
    guid="4246a29d-05e4-5789-9529-e0c9110b89c9",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PreciousTrolley.Name",
    display_name="Precious Trolley",
    searchable_by=["Precious Trolley", "Item", "ACE SPEC"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=185,
    set_code="SV8",
    rarity=Rarities.Rare,
    effect=search_to_bench(is_basic_pokemon, BENCH_CAPACITY)
)
