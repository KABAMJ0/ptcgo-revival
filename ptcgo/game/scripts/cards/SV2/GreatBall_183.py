from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import look_at_top
from ptcgo.game.card_effects.trainers import is_pokemon_card

card = ItemCardDef(
    guid="052ebaa7-7cac-5da5-bb3f-3bdfa8ff7ef0",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GreatBall.Name",
    display_name="Great Ball",
    searchable_by=["Great Ball", "Item"],
    subtypes=["Item"],
    collector_number=183,
    set_code="SV2",
    rarity=Rarities.Common,
    effect=look_at_top(7, take=1, predicate=is_pokemon_card)
)
