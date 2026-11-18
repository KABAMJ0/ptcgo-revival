from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import opponent_bench_to_active

card = SupporterCardDef(
    guid="05ba6ea4-307a-5613-a7ee-40d53ebc277b",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BosssOrders.Name",
    display_name="Boss's Orders",
    searchable_by=["Boss's Orders", "Supporter"],
    subtypes=["Supporter"],
    collector_number=183,
    set_code="ME2PT5",
    rarity=Rarities.Uncommon,
    effect=opponent_bench_to_active()
)
