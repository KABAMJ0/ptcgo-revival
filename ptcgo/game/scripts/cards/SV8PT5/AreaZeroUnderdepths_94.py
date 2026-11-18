from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import tera_bench_cap

card = StadiumCardDef(
    guid="2af2b37a-205e-56d2-9a83-bf83c7c2c6de",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AreaZeroUnderdepths.Name",
    display_name="Area Zero Underdepths",
    searchable_by=["Area Zero Underdepths", "Stadium"],
    subtypes=["Stadium"],
    collector_number=94,
    set_code="SV8PT5",
    rarity=Rarities.Uncommon,
    passive=tera_bench_cap(),
)
