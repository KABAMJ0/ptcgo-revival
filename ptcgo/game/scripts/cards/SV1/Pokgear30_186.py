from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import look_at_top
from ptcgo.game.card_effects.trainers import is_supporter_card

card = ItemCardDef(
    guid="d7deddbf-4c18-5645-b9d1-7033d5aedaa0",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Pokgear30.Name",
    display_name="Pokégear 3.0",
    searchable_by=["Pok\u00e9gear 3.0", "Item"],
    subtypes=["Item"],
    collector_number=186,
    set_code="SV1",
    rarity=Rarities.Common,
    effect=look_at_top(7, take=1, predicate=is_supporter_card)
)
