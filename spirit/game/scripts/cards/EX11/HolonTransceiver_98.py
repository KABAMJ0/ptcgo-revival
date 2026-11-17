from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="04caf74a-9cd8-5f0e-804e-cea91f974739",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HolonTransceiver.Name",
    display_name="Holon Transceiver",
    searchable_by=["Holon Transceiver", "Item"],
    subtypes=["Item"],
    collector_number=98,
    set_code="EX11",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
