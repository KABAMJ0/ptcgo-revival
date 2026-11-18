from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import opponent_bench_to_active

card = ItemCardDef(
    guid="beed2548-4563-5060-8181-6326bcd7aea0",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GustofWind.Name",
    display_name="Gust of Wind",
    searchable_by=["Gust of Wind"],
    subtypes=[],
    collector_number=120,
    set_code="BASE4",
    rarity=Rarities.Common,
    effect=opponent_bench_to_active()
)
