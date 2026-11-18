from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import pokemon_of_subtype

card = ItemCardDef(
    guid="04a9f03e-8f5c-5b8d-a5a2-661a1dc0ed92",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TagCall.Name",
    display_name="Tag Call",
    searchable_by=["Tag Call", "Item"],
    subtypes=["Item"],
    collector_number=206,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(pokemon_of_subtype("TAG TEAM"), count=2)
)
