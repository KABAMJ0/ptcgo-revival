from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import card_named_contains, look_bottom_to_bench

card = ItemCardDef(
    guid="972135c9-19af-57e4-8f29-3c663fcfd9d0",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RootFossilLileep.Name",
    display_name="Root Fossil Lileep",
    searchable_by=["Root Fossil Lileep", "Item"],
    subtypes=["Item"],
    collector_number=87,
    set_code="BW10",
    rarity=Rarities.Uncommon,
    effect=look_bottom_to_bench(7, card_named_contains("lileep"))
)
