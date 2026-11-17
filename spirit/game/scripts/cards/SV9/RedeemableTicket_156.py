from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="7ef29643-8712-5a65-91da-d74c087985c9",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RedeemableTicket.Name",
    display_name="Redeemable Ticket",
    searchable_by=["Redeemable Ticket", "Item"],
    subtypes=["Item"],
    collector_number=156,
    set_code="SV9",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
