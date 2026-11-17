from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import look_at_top
from spirit.game.card_effects.trainers import any_of, is_basic_pokemon, is_evolution_pokemon

card = ItemCardDef(
    guid="8e415aef-79fb-516d-870c-5bc63747c59a",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MasterBall.Name",
    display_name="Master Ball",
    searchable_by=["Master Ball", "Item"],
    subtypes=["Item"],
    collector_number=78,
    set_code="EX16",
    rarity=Rarities.Uncommon,
    effect=look_at_top(7, take=1, predicate=any_of(is_basic_pokemon, is_evolution_pokemon), rest="shuffle")
)
