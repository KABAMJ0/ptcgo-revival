from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import switch

card = ItemCardDef(
    guid="d25e1197-efa2-5328-a8dd-d1610471b288",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Switch.Name",
    display_name="Switch",
    searchable_by=["Switch", "Item"],
    subtypes=["Item"],
    collector_number=163,
    set_code="XY5",
    rarity=Rarities.RareSecret,
    effect=switch
)
