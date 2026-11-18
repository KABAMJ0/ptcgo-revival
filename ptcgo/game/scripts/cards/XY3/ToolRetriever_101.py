from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import tools_to_hand

card = ItemCardDef(
    guid="b7c58442-1e30-51b9-b283-f08a6b335f2e",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ToolRetriever.Name",
    display_name="Tool Retriever",
    searchable_by=["Tool Retriever", "Item"],
    subtypes=["Item"],
    collector_number=101,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    effect=tools_to_hand(None, 2)
)
