from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import gust_bench_only, pokemon_of_subtype


_MEGA_CATCHER = gust_bench_only(pokemon_of_subtype("MEGA"))


card = ItemCardDef(
    guid="c102cb21-1255-5094-95c7-7525ec80e694",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MegaCatcher.Name",
    display_name="Mega Catcher",
    searchable_by=["Mega Catcher", "Item"],
    subtypes=["Item"],
    collector_number=104,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    effect=_MEGA_CATCHER
)
