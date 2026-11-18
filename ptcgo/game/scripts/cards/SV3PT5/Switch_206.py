from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import switch

card = ItemCardDef(
    guid="8e3ae811-75b0-5572-9a52-574c5f772ff2",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Switch.Name",
    display_name="Switch",
    searchable_by=["Switch", "Item"],
    subtypes=["Item"],
    collector_number=206,
    set_code="SV3PT5",
    rarity=Rarities.Rare,
    effect=switch
)
