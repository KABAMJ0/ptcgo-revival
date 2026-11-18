from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_tools

card = ItemCardDef(
    guid="8b68c57e-60c9-58fd-b87c-aa6e2dd4a841",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ToolScrapper.Name",
    display_name="Tool Scrapper",
    searchable_by=["Tool Scrapper", "Item"],
    subtypes=["Item"],
    collector_number=116,
    set_code="BW6",
    rarity=Rarities.Uncommon,
    effect=discard_tools(2)
)
