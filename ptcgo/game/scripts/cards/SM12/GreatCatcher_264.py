from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import gust_bench_gx_ex, with_discard_cost

card = ItemCardDef(
    guid="34b89b48-244f-5cdf-8036-f1c642f7797d",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GreatCatcher.Name",
    display_name="Great Catcher",
    searchable_by=["Great Catcher", "Item"],
    subtypes=["Item"],
    collector_number=264,
    set_code="SM12",
    rarity=Rarities.RareSecret,
    effect=with_discard_cost(2, gust_bench_gx_ex(1))
)
