from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import switch

card = ItemCardDef(
    guid="03c640e5-6ab0-5487-8f7f-bf01e656ab6e",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Switch.Name",
    display_name="Switch",
    searchable_by=["Switch", "Item"],
    subtypes=["Item"],
    collector_number=123,
    set_code="ME2",
    rarity=Rarities.Rare,
    effect=switch
)
