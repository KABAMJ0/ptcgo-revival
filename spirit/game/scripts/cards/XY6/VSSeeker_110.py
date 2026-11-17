from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import is_supporter_card

card = ItemCardDef(
    guid="f499207a-db1a-5bdd-a33c-776871533a3f",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.VSSeeker.Name",
    display_name="VS Seeker",
    searchable_by=["VS Seeker", "Item"],
    subtypes=["Item"],
    collector_number=110,
    set_code="XY6",
    rarity=Rarities.RareSecret,
    effect=recover_from_discard(is_supporter_card, count=1, to="hand")
)
