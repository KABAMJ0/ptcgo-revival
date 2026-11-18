from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import gust_bench_gx_ex, with_discard_cost

card = ItemCardDef(
    guid="790a9393-4d88-50ef-9dbe-0ce83805d7bd",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GreatCatcher.Name",
    display_name="Great Catcher",
    searchable_by=["Great Catcher", "Item"],
    subtypes=["Item"],
    collector_number=192,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    effect=with_discard_cost(2, gust_bench_gx_ex(1))
)
