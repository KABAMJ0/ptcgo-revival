from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import look_at_top
from ptcgo.game.card_effects.trainers import any_of, is_basic_pokemon, is_evolution_pokemon

card = ItemCardDef(
    guid="077bf8e6-857a-5ee4-8e9c-8ecd9a5a4e89",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MasterBall.Name",
    display_name="Master Ball",
    searchable_by=["Master Ball", "Item"],
    subtypes=["Item"],
    collector_number=99,
    set_code="EX11",
    rarity=Rarities.Uncommon,
    effect=look_at_top(7, take=1, predicate=any_of(is_basic_pokemon, is_evolution_pokemon), rest="shuffle")
)
