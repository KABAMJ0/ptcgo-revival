from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities

card = ItemCardDef(
    guid="4ebc61ca-7af4-5584-b2af-df4d580918d5",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MaxRevive.Name",
    display_name="Max Revive",
    searchable_by=["Max Revive", "Item"],
    subtypes=["Item"],
    collector_number=65,
    set_code="TwentiethAnn",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
