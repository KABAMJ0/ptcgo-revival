from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import card_named_contains, look_bottom_to_bench

card = ItemCardDef(
    guid="c6afbafe-eec4-5ff8-a20d-f0e3401dac8b",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.OldAmberAerodactyl.Name",
    display_name="Old Amber Aerodactyl",
    searchable_by=["Old Amber Aerodactyl", "Item"],
    subtypes=["Item"],
    collector_number=106,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    effect=look_bottom_to_bench(7, card_named_contains("aerodactyl"))
)
