from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import look_at_top
from ptcgo.game.card_effects.trainers import is_pokemon_card

card = ItemCardDef(
    guid="b0576e28-6c57-5c5b-a3d6-5eca04ec248a",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GreatBall.Name",
    display_name="Great Ball",
    searchable_by=["Great Ball", "Item"],
    subtypes=["Item"],
    collector_number=60,
    set_code="SL",
    rarity=Rarities.Uncommon,
    effect=look_at_top(7, take=1, predicate=is_pokemon_card)
)
