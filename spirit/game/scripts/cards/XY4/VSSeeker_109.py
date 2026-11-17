from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import is_supporter_card

card = ItemCardDef(
    guid="f8bef826-caea-5575-926e-0ffca16f2c5e",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.VSSeeker.Name",
    display_name="VS Seeker",
    searchable_by=["VS Seeker", "Item"],
    subtypes=["Item"],
    collector_number=109,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    effect=recover_from_discard(is_supporter_card, count=1, to="hand")
)
