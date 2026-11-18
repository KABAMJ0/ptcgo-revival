from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import opponent_bench_to_active

card = ItemCardDef(
    guid="972d7ee6-3386-5e82-b6c8-6c82034aa920",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GustofWind.Name",
    display_name="Gust of Wind",
    searchable_by=["Gust of Wind"],
    subtypes=[],
    collector_number=93,
    set_code="BASE1",
    rarity=Rarities.Common,
    effect=opponent_bench_to_active()
)
