from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import look_at_top
from ptcgo.game.card_effects.trainers import any_of, is_basic_pokemon, is_evolution_pokemon

card = ItemCardDef(
    guid="ad5cd530-6545-577e-b08a-7cdb6e409f21",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MasterBall.Name",
    display_name="Master Ball",
    searchable_by=["Master Ball"],
    subtypes=[],
    collector_number=143,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    effect=look_at_top(7, take=1, predicate=any_of(is_basic_pokemon, is_evolution_pokemon))
)
