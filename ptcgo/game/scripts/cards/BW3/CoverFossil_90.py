from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import card_named_contains, look_bottom_to_bench

card = ItemCardDef(
    guid="f2987372-7898-53bf-810b-e00e3fa45d59",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CoverFossil.Name",
    display_name="Cover Fossil",
    searchable_by=["Cover Fossil", "Item"],
    subtypes=["Item"],
    collector_number=90,
    set_code="BW3",
    rarity=Rarities.Uncommon,
    effect=look_bottom_to_bench(7, card_named_contains("tirtouga"))
)
