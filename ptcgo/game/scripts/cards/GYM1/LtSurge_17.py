from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import basic_from_hand_as_active, bench_has_room_condition

card = ItemCardDef(
    guid="fdfe2f97-6c95-5e31-a180-1d6b21f7f82a",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LtSurge.Name",
    display_name="Lt. Surge",
    searchable_by=["Lt. Surge"],
    subtypes=[],
    collector_number=17,
    set_code="GYM1",
    rarity=Rarities.RareHolo,
    effect=basic_from_hand_as_active(),
    condition=bench_has_room_condition()
)
