from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import discard_tools

card = ItemCardDef(
    guid="9459576e-a4ed-5767-9133-6b152d2b0989",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ToolScrapper.Name",
    display_name="Tool Scrapper",
    searchable_by=["Tool Scrapper", "Item"],
    subtypes=["Item"],
    collector_number=85,
    set_code="RSV10PT5",
    rarity=Rarities.Uncommon,
    effect=discard_tools(2)
)
