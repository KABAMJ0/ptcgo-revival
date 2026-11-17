from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import switch

card = ItemCardDef(
    guid="bdf86208-74f6-568e-abdf-f8fc04fc8623",
    key="SM35",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Switch.Name",
    display_name="Switch",
    searchable_by=["Switch", "Item"],
    subtypes=["Item"],
    collector_number=67,
    set_code="SM35",
    rarity=Rarities.Uncommon,
    effect=switch
)
