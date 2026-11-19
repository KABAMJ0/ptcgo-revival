from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import pokemon_of_subtype, stadium_ability
from ptcgo.game.card_effects.support_common import search_to_hand


_ULTRA_BEAST = pokemon_of_subtype("Ultra Beast")

_SEARCH_ULTRA_BEAST = search_to_hand(
    _ULTRA_BEAST, count=1, minimum=0, reveal=True,
    prompt="Choose an Ultra Beast card to put into your hand")


card = StadiumCardDef(
    guid="275ec1de-d82c-5643-8416-eb4529477822",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UltraSpace.Name",
    display_name="Ultra Space",
    searchable_by=["Ultra Space", "Stadium"],
    subtypes=["Stadium"],
    collector_number=115,
    set_code="SM6",
    rarity=Rarities.Uncommon,
    ability=stadium_ability("Ultra Space", _SEARCH_ULTRA_BEAST),
)
