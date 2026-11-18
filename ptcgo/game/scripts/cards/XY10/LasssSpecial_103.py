from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_per_opponent_bench_basic

card = SupporterCardDef(
    guid="1a44fea6-e882-53b6-be66-799e0c629b48",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LasssSpecial.Name",
    display_name="Lass's Special",
    searchable_by=["Lass's Special", "Supporter"],
    subtypes=["Supporter"],
    collector_number=103,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    effect=draw_per_opponent_bench_basic(1)
)
