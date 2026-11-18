from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import card_named_contains, look_bottom_to_bench

card = ItemCardDef(
    guid="e482382e-c42b-5200-bb37-ad1e96179bff",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CoverFossil.Name",
    display_name="Cover Fossil",
    searchable_by=["Cover Fossil", "Item"],
    subtypes=["Item"],
    collector_number=79,
    set_code="BW10",
    rarity=Rarities.Uncommon,
    effect=look_bottom_to_bench(7, card_named_contains("tirtouga"))
)
