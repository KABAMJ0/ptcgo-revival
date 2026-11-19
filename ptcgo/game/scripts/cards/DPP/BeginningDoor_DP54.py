from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import search_named_card

card = ItemCardDef(
    guid="975b44be-db60-524a-bfcd-ffcb09eb1e61",
    key="DPP",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BeginningDoor.Name",
    display_name="Beginning Door",
    searchable_by=["Beginning Door", "Item"],
    subtypes=["Item"],
    collector_number=54,
    set_code="DPP",
    rarity=Rarities.RarePromo,
    effect=search_named_card("arceus")
)
