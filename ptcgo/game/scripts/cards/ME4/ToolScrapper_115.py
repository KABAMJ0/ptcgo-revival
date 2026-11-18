from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_tools

card = ItemCardDef(
    guid="05a5cb17-62a5-5b9c-b10b-722e368245fd",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ToolScrapper.Name",
    display_name="Tool Scrapper",
    searchable_by=["Tool Scrapper", "Item"],
    subtypes=["Item"],
    collector_number=115,
    set_code="ME4",
    rarity=Rarities.Rare,
    effect=discard_tools(2)
)
