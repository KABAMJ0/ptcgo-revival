from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import all_of, excluding, is_pokemon_card, pokemon_lv_x

card = ItemCardDef(
    guid="d5c3c385-8cec-58eb-bc2b-aeddcee83f88",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LuxuryBall.Name",
    display_name="Luxury Ball",
    searchable_by=["Luxury Ball", "Item"],
    subtypes=["Item"],
    collector_number=86,
    set_code="DP7",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(all_of(is_pokemon_card, excluding(pokemon_lv_x())), count=1)
)
