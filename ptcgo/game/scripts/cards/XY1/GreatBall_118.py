from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import look_at_top
from ptcgo.game.card_effects.trainers import is_pokemon_card

card = ItemCardDef(
    guid="456f5154-79bb-567c-b554-91d300008321",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GreatBall.Name",
    display_name="Great Ball",
    searchable_by=["Great Ball", "Item"],
    subtypes=["Item"],
    collector_number=118,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    effect=look_at_top(7, take=1, predicate=is_pokemon_card)
)
