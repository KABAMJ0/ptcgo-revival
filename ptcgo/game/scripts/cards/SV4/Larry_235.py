from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities

from ptcgo.game.card_effects.trainers import flip_search_pair, is_basic_pokemon, is_pokemon_card

card = SupporterCardDef(
    guid="2d2cf0ab-1972-5621-b768-f0acc569adbc",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Larry.Name",
    display_name="Larry",
    searchable_by=["Larry", "Supporter"],
    subtypes=["Supporter"],
    collector_number=235,
    set_code="SV4",
    rarity=Rarities.Rare,
    effect=flip_search_pair(is_pokemon_card, 2, is_basic_pokemon, 1)
)
