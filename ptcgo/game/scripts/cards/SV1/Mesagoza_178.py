from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import if_heads, is_pokemon_card, stadium_ability

card = StadiumCardDef(
    guid="aeb5c2c2-5fa2-5bd2-a7a9-1e7521f2172f",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Mesagoza.Name",
    display_name="Mesagoza",
    searchable_by=["Mesagoza", "Stadium"],
    subtypes=["Stadium"],
    collector_number=178,
    set_code="SV1",
    rarity=Rarities.Uncommon,
    ability=stadium_ability('Mesagoza', if_heads(search_to_hand(is_pokemon_card, count=1)))
)
