from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import pokemon_lv_x, search_deck_or_discard_to_hand

card = ItemCardDef(
    guid="949300da-ddee-5966-92e3-cdc060912465",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PremierBall.Name",
    display_name="Premier Ball",
    searchable_by=["Premier Ball", "Item"],
    subtypes=["Item"],
    collector_number=91,
    set_code="DP7",
    rarity=Rarities.Uncommon,
    effect=search_deck_or_discard_to_hand(pokemon_lv_x(), count=1)
)
