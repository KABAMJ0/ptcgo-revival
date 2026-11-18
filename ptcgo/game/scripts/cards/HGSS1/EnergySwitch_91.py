from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities

card = ItemCardDef(
    guid="e085f783-c8aa-5678-962b-31ab4192df39",
    key="HGSS1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySwitch.Name",
    display_name="Energy Switch",
    searchable_by=["Energy Switch", "Item"],
    subtypes=["Item"],
    collector_number=91,
    set_code="HGSS1",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
