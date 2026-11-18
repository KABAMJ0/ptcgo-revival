from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import opponent_bench_to_active

card = SupporterCardDef(
    guid="bec4baf1-59f5-5ccd-bf49-a838925940d2",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BosssOrders.Name",
    display_name="Boss's Orders",
    searchable_by=["Boss's Orders", "Supporter"],
    subtypes=["Supporter"],
    collector_number=114,
    set_code="ME1",
    rarity=Rarities.Uncommon,
    effect=opponent_bench_to_active()
)
