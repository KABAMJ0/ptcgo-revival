from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.card_effects.trainers import is_supporter_card

card = ItemCardDef(
    guid="0b83cf15-1302-5b47-aa39-9fd803d5e895",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PalPad.Name",
    display_name="Pal Pad",
    searchable_by=["Pal Pad", "Item"],
    subtypes=["Item"],
    collector_number=182,
    set_code="SV1",
    rarity=Rarities.Common,
    effect=recover_from_discard(is_supporter_card, count=2, to="deck_shuffle")
)
