from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import look_at_top
from spirit.game.card_effects.trainers import any_of, is_basic_pokemon, is_evolution_pokemon

card = ItemCardDef(
    guid="05ad62a2-580f-5aa8-ab96-b43e5a3a6a66",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MasterBall.Name",
    display_name="Master Ball",
    searchable_by=["Master Ball", "Item"],
    subtypes=["Item"],
    collector_number=88,
    set_code="EX8",
    rarity=Rarities.Uncommon,
    effect=look_at_top(7, take=1, predicate=any_of(is_basic_pokemon, is_evolution_pokemon), rest="shuffle")
)
