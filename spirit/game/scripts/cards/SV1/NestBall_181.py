from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_bench
from spirit.game.card_effects.trainers import is_basic_pokemon

card = ItemCardDef(
    guid="f3704611-9f83-5c87-aedf-2f68880c187e",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NestBall.Name",
    display_name="Nest Ball",
    searchable_by=["Nest Ball", "Item"],
    subtypes=["Item"],
    collector_number=181,
    set_code="SV1",
    rarity=Rarities.Uncommon,
    effect=search_to_bench(is_basic_pokemon, 1)
)
