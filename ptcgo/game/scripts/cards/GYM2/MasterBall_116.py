from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import look_at_top
from ptcgo.game.card_effects.trainers import any_of, is_basic_pokemon, is_evolution_pokemon

card = ItemCardDef(
    guid="3174f8da-44dc-58e3-9d1b-eca9871f4154",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MasterBall.Name",
    display_name="Master Ball",
    searchable_by=["Master Ball"],
    subtypes=[],
    collector_number=116,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    effect=look_at_top(7, take=1, predicate=any_of(is_basic_pokemon, is_evolution_pokemon))
)
