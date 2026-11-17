from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="c7315377-2a14-5f14-bc97-679102ca9c77",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TicklingMachine.Name",
    display_name="Tickling Machine",
    searchable_by=["Tickling Machine", "Rocket's Secret Machine"],
    subtypes=["Rocket's Secret Machine"],
    collector_number=119,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
