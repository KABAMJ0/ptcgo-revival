from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import pokemon_of_subtype

card = ItemCardDef(
    guid="034de107-16f2-542a-93bc-ad786eb1b7b4",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TagCall.Name",
    display_name="Tag Call",
    searchable_by=["Tag Call", "Item"],
    subtypes=["Item"],
    collector_number=270,
    set_code="SM12",
    rarity=Rarities.RareSecret,
    effect=search_to_hand(pokemon_of_subtype("TAG TEAM"), count=2)
)
