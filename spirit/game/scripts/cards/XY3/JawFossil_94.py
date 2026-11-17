from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import card_named_contains, look_bottom_to_bench

card = ItemCardDef(
    guid="98f9f9d7-d9ab-5369-af62-c82c5b553100",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.JawFossil.Name",
    display_name="Jaw Fossil",
    searchable_by=["Jaw Fossil", "Item"],
    subtypes=["Item"],
    collector_number=94,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    effect=look_bottom_to_bench(7, card_named_contains("tyrunt"))
)
