from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import look_at_top
from ptcgo.game.card_effects.trainers import is_supporter_card

card = ItemCardDef(
    guid="0128a5d9-7a82-5747-8273-8979ed5e663d",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Pokgear30.Name",
    display_name="Pokégear 3.0",
    searchable_by=["Pok\u00e9gear 3.0", "Item"],
    subtypes=["Item"],
    collector_number=84,
    set_code="ZSV10PT5",
    rarity=Rarities.Uncommon,
    effect=look_at_top(7, take=1, predicate=is_supporter_card)
)
