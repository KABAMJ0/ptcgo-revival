from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import search_named_card

card = ItemCardDef(
    guid="eb0703a6-60cd-5a7a-b492-38a343b91d6a",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BeginningDoor.Name",
    display_name="Beginning Door",
    searchable_by=["Beginning Door", "Item"],
    subtypes=["Item"],
    collector_number=82,
    set_code="PL4",
    rarity=Rarities.Uncommon,
    effect=search_named_card("arceus")
)
