from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import pokemon_of_subtype, stadium_ability
from ptcgo.game.card_effects.support_common import search_to_hand

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
    ability=stadium_ability("Ultra Space", search_to_hand(pokemon_of_subtype("Ultra Beast"), 1))
)
