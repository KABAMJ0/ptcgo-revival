from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import tera_bench_cap

card = StadiumCardDef(
    guid="5a29f77d-a55a-5428-96d9-9feaab82c8f3",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AreaZeroUnderdepths.Name",
    display_name="Area Zero Underdepths",
    searchable_by=["Area Zero Underdepths", "Stadium"],
    subtypes=["Stadium"],
    collector_number=131,
    set_code="SV7",
    rarity=Rarities.Uncommon,
    passive=tera_bench_cap(),
)
