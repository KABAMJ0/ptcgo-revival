from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import card_named_contains, look_bottom_to_bench

card = ItemCardDef(
    guid="8d39e07c-2ead-54f4-9f11-c6a2f6e6c6a9",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DomeFossilKabuto.Name",
    display_name="Dome Fossil Kabuto",
    searchable_by=["Dome Fossil Kabuto", "Item"],
    subtypes=["Item"],
    collector_number=96,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    effect=look_bottom_to_bench(7, card_named_contains("kabuto"))
)
