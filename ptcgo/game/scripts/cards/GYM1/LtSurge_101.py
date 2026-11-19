from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import basic_from_hand_as_active, bench_has_room

card = ItemCardDef(
    guid="4af0f412-55ba-53d3-a3a5-ef0f37835c01",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LtSurge.Name",
    display_name="Lt. Surge",
    searchable_by=["Lt. Surge"],
    subtypes=[],
    collector_number=101,
    set_code="GYM1",
    rarity=Rarities.Rare,
    effect=basic_from_hand_as_active(),
    condition=bench_has_room()
)
