from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_tools

card = ItemCardDef(
    guid="d9dba033-3e5f-56e9-8c6d-39539398122a",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ToolScrapper.Name",
    display_name="Tool Scrapper",
    searchable_by=["Tool Scrapper", "Item"],
    subtypes=["Item"],
    collector_number=212,
    set_code="ME2PT5",
    rarity=Rarities.Common,
    effect=discard_tools(2)
)
