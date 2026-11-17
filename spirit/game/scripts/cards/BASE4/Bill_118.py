from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import draw_n

card = ItemCardDef(
    guid="87d14847-b7fb-5bac-a173-f4333188f321",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Bill.Name",
    display_name="Bill",
    searchable_by=["Bill"],
    subtypes=[],
    collector_number=118,
    set_code="BASE4",
    rarity=Rarities.Common,
    effect=draw_n(2)
)
