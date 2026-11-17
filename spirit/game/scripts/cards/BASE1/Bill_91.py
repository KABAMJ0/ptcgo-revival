from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import draw_n

card = ItemCardDef(
    guid="4a4961ac-af79-5067-b52d-be88935b48b8",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Bill.Name",
    display_name="Bill",
    searchable_by=["Bill"],
    subtypes=[],
    collector_number=91,
    set_code="BASE1",
    rarity=Rarities.Common,
    effect=draw_n(2)
)
