from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import each_may_draw_up_to

card = ItemCardDef(
    guid="fe02825e-4cbe-5bc4-a87c-c7b44dc67364",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Erika.Name",
    display_name="Erika",
    searchable_by=["Erika"],
    subtypes=[],
    collector_number=100,
    set_code="GYM1",
    rarity=Rarities.Rare,
    effect=each_may_draw_up_to(3)
)
