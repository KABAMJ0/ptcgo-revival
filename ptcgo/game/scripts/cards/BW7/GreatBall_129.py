from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import look_at_top
from ptcgo.game.card_effects.trainers import is_pokemon_card

card = ItemCardDef(
    guid="decebfad-53ba-5c6a-84a9-6e342e63231e",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GreatBall.Name",
    display_name="Great Ball",
    searchable_by=["Great Ball", "Item"],
    subtypes=["Item"],
    collector_number=129,
    set_code="BW7",
    rarity=Rarities.Uncommon,
    effect=look_at_top(7, take=1, predicate=is_pokemon_card, minimum=0)
)
