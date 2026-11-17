from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="fa70ef3e-1626-5313-8467-278e0072161a",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MegaSignal.Name",
    display_name="Mega Signal",
    searchable_by=["Mega Signal", "Item"],
    subtypes=["Item"],
    collector_number=121,
    set_code="ME1",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
