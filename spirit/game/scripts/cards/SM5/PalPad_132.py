from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import is_supporter_card

card = ItemCardDef(
    guid="3fc95433-f1bc-5080-b3f9-36183a475eba",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PalPad.Name",
    display_name="Pal Pad",
    searchable_by=["Pal Pad", "Item"],
    subtypes=["Item"],
    collector_number=132,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    effect=recover_from_discard(is_supporter_card, count=2, to="deck_shuffle")
)
