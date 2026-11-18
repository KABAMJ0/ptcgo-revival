from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities

from ptcgo.game.card_effects.trainers import flip_search_pair, is_basic_pokemon, is_pokemon_card

card = SupporterCardDef(
    guid="07e872bc-8e5b-51d7-94cb-8af6a7f5bfe4",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Larry.Name",
    display_name="Larry",
    searchable_by=["Larry", "Supporter"],
    subtypes=["Supporter"],
    collector_number=165,
    set_code="SV4",
    rarity=Rarities.Common,
    effect=flip_search_pair(is_pokemon_card, 2, is_basic_pokemon, 1)
)
