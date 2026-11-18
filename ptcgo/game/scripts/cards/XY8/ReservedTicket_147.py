from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import if_heads, search_to_top

card = ItemCardDef(
    guid="b3f7ca8f-d81a-5893-b7e7-c9e7bc56799a",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ReservedTicket.Name",
    display_name="Reserved Ticket",
    searchable_by=["Reserved Ticket", "Item"],
    subtypes=["Item"],
    collector_number=147,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    effect=if_heads(search_to_top(1))
)
