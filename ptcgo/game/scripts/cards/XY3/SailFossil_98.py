from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import card_named_contains, look_bottom_to_bench

card = ItemCardDef(
    guid="878bdf8b-e25d-5433-8d07-3715f4cdedf5",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SailFossil.Name",
    display_name="Sail Fossil",
    searchable_by=["Sail Fossil", "Item"],
    subtypes=["Item"],
    collector_number=98,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    effect=look_bottom_to_bench(7, card_named_contains("amaura"))
)
