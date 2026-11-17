from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="10f9d0a4-a4f9-5774-9bf4-3304369f9bcc",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EarthenVessel.Name",
    display_name="Earthen Vessel",
    searchable_by=["Earthen Vessel", "Item", "Ancient"],
    subtypes=["Item", "Ancient"],
    collector_number=163,
    set_code="SV4",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
