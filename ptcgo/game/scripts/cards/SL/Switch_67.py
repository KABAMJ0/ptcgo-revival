from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import switch

card = ItemCardDef(
    guid="bdf86208-74f6-568e-abdf-f8fc04fc8623",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Switch.Name",
    display_name="Switch",
    searchable_by=["Switch", "Item"],
    subtypes=["Item"],
    collector_number=67,
    set_code="SL",
    rarity=Rarities.Uncommon,
    effect=switch
)
