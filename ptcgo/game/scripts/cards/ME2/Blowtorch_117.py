from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities

card = ItemCardDef(
    guid="bd9a621d-d209-5efc-afee-09b5d3deaefe",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Blowtorch.Name",
    display_name="Blowtorch",
    searchable_by=["Blowtorch", "Item"],
    subtypes=["Item"],
    collector_number=117,
    set_code="ME2",
    rarity=Rarities.Rare,
    effect=unimplemented
)
