from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.card_effects.trainers import is_supporter_card

card = ItemCardDef(
    guid="0daf3ae6-be85-5a7e-9d62-44327f84e1ed",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.VSSeeker.Name",
    display_name="VS Seeker",
    searchable_by=["VS Seeker", "Item"],
    subtypes=["Item"],
    collector_number=100,
    set_code="EX6",
    rarity=Rarities.Uncommon,
    effect=recover_from_discard(is_supporter_card, count=1, to="hand", reveal=True)
)
