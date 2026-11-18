from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import pokemon_lv_x, search_deck_or_discard_to_hand

card = ItemCardDef(
    guid="5db00b25-470e-5f43-a62b-0d2ee554e6ec",
    key="DP4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PremierBall.Name",
    display_name="Premier Ball",
    searchable_by=["Premier Ball", "Item"],
    subtypes=["Item"],
    collector_number=101,
    set_code="DP4",
    rarity=Rarities.Uncommon,
    effect=search_deck_or_discard_to_hand(pokemon_lv_x(), count=1)
)
