from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import look_at_top
from ptcgo.game.card_effects.trainers import is_supporter_card

card = ItemCardDef(
    guid="be292e28-ece9-597f-bd4b-3e884acb23a1",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Pokgear30.Name",
    display_name="Pokégear 3.0",
    searchable_by=["Pok\u00e9gear 3.0", "Item"],
    subtypes=["Item"],
    collector_number=182,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    effect=look_at_top(7, take=1, predicate=is_supporter_card, minimum=0)
)
