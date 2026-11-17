from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import look_at_top
from spirit.game.card_effects.trainers import is_supporter_card

card = ItemCardDef(
    guid="5f70a427-2e0b-5c38-a33f-668a24340ce1",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Pokgear30.Name",
    display_name="Pokégear 3.0",
    searchable_by=["Pok\u00e9gear 3.0", "Item"],
    subtypes=["Item"],
    collector_number=182,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    effect=look_at_top(7, take=1, predicate=is_supporter_card)
)
