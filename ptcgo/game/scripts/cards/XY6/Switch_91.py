from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import switch

card = ItemCardDef(
    guid="89bf02c0-a32e-54da-b22b-f077f6491061",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Switch.Name",
    display_name="Switch",
    searchable_by=["Switch", "Item"],
    subtypes=["Item"],
    collector_number=91,
    set_code="XY6",
    rarity=Rarities.Uncommon,
    effect=switch
)
