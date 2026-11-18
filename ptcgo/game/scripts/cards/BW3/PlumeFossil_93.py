from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import card_named_contains, look_bottom_to_bench

card = ItemCardDef(
    guid="a059c8ec-e1c3-549a-9aec-dd171b482c80",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PlumeFossil.Name",
    display_name="Plume Fossil",
    searchable_by=["Plume Fossil", "Item"],
    subtypes=["Item"],
    collector_number=93,
    set_code="BW3",
    rarity=Rarities.Uncommon,
    effect=look_bottom_to_bench(7, card_named_contains("archen"))
)
