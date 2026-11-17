from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import card_named_contains, look_bottom_to_bench

card = ItemCardDef(
    guid="9fcd7409-97fd-52b2-bb48-d2f70c8bbfbc",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PlumeFossil.Name",
    display_name="Plume Fossil",
    searchable_by=["Plume Fossil", "Item"],
    subtypes=["Item"],
    collector_number=82,
    set_code="BW10",
    rarity=Rarities.Uncommon,
    effect=look_bottom_to_bench(7, card_named_contains("archen"))
)
