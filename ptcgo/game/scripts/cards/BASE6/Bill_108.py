from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_n

card = ItemCardDef(
    guid="bfc1af0c-ff99-5130-a3f7-89387834cd69",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Bill.Name",
    display_name="Bill",
    searchable_by=["Bill"],
    subtypes=[],
    collector_number=108,
    set_code="BASE6",
    rarity=Rarities.Common,
    effect=draw_n(2)
)
