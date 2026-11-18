from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.card_effects.trainers import is_supporter_card

card = ItemCardDef(
    guid="415c45ab-fac1-5e08-a53c-a32a2837b0d4",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.VSSeeker.Name",
    display_name="VS Seeker",
    searchable_by=["VS Seeker", "Item"],
    subtypes=["Item"],
    collector_number=140,
    set_code="PL3",
    rarity=Rarities.Uncommon,
    effect=recover_from_discard(is_supporter_card, count=1, to="hand", reveal=True)
)
