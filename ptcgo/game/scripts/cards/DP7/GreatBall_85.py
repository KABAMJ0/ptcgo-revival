from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_bench
from ptcgo.game.card_effects.trainers import is_basic_pokemon

card = ItemCardDef(
    guid="7e1b1b8d-6dad-565c-8eb1-5eb1f2c56ecd",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GreatBall.Name",
    display_name="Great Ball",
    searchable_by=["Great Ball", "Item"],
    subtypes=["Item"],
    collector_number=85,
    set_code="DP7",
    rarity=Rarities.Uncommon,
    effect=search_to_bench(is_basic_pokemon, 1)
)
