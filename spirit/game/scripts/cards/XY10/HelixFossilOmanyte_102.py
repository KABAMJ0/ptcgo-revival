from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import card_named_contains, look_bottom_to_bench

card = ItemCardDef(
    guid="40fa2b61-b005-5839-8432-f96e46f5ceeb",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HelixFossilOmanyte.Name",
    display_name="Helix Fossil Omanyte",
    searchable_by=["Helix Fossil Omanyte", "Item"],
    subtypes=["Item"],
    collector_number=102,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    effect=look_bottom_to_bench(7, card_named_contains("omanyte"))
)
