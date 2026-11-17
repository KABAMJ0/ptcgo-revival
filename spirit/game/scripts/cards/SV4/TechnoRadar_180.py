from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="1945e426-d6f3-596e-a039-7ea84f40831d",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TechnoRadar.Name",
    display_name="Techno Radar",
    searchable_by=["Techno Radar", "Item", "Future"],
    subtypes=["Item", "Future"],
    collector_number=180,
    set_code="SV4",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
