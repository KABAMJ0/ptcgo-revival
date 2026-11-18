from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_then_shuffle_hand

card = ItemCardDef(
    guid="0c3ceeb5-261d-59f2-b81a-a9ba9351e29d",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Mary.Name",
    display_name="Mary",
    searchable_by=["Mary"],
    subtypes=[],
    collector_number=87,
    set_code="NEO1",
    rarity=Rarities.Rare,
    effect=draw_then_shuffle_hand(2, 2)
)
