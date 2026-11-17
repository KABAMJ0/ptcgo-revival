from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_bench
from spirit.game.card_effects.trainers import is_basic_pokemon

card = ItemCardDef(
    guid="68820d08-93e3-5a8c-9e07-243675e71bae",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NestBall.Name",
    display_name="Nest Ball",
    searchable_by=["Nest Ball", "Item"],
    subtypes=["Item"],
    collector_number=84,
    set_code="SV4PT5",
    rarity=Rarities.Uncommon,
    effect=search_to_bench(is_basic_pokemon, 1)
)
