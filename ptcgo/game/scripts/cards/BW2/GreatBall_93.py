from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import look_at_top
from ptcgo.game.card_effects.trainers import is_pokemon_card

card = ItemCardDef(
    guid="a2635d70-23b1-5744-b198-5a889e4fb023",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GreatBall.Name",
    display_name="Great Ball",
    searchable_by=["Great Ball", "Item"],
    subtypes=["Item"],
    collector_number=93,
    set_code="BW2",
    rarity=Rarities.Uncommon,
    effect=look_at_top(7, take=1, predicate=is_pokemon_card)
)
