from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import bench_named_pokemon, card_named_any, choose_one, if_heads
from ptcgo.game.card_effects.support_common import requires_bench_space

_FOSSIL_EGG_FAMILY = card_named_any(("omanyte", "kabuto", "aerodactyl"))

_FOSSIL_EGG = if_heads(choose_one([
    ("Search your deck", bench_named_pokemon(_FOSSIL_EGG_FAMILY, source="deck")),
    ("From your hand", bench_named_pokemon(_FOSSIL_EGG_FAMILY, source="hand")),
]))


card = ItemCardDef(
    guid="8705713e-33f5-5de5-87af-5a3304666223",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FossilEgg.Name",
    display_name="Fossil Egg",
    searchable_by=["Fossil Egg"],
    subtypes=[],
    collector_number=72,
    set_code="NEO2",
    rarity=Rarities.Uncommon,
    effect=_FOSSIL_EGG, condition=requires_bench_space(1)
)
