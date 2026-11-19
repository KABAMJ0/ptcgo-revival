from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import if_heads, is_pokemon_card

card = ItemCardDef(
    guid="cca8d164-4e24-5053-bd85-d712ecf4d3cb",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.trainer.VictoryCup.Name",
    display_name="Victory Cup",
    searchable_by=["Victory Cup", "Item"],
    subtypes=["Item"],
    collector_number=31,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    effect=if_heads(search_to_hand(is_pokemon_card, 1,
                                    prompt="Choose a Pokemon to reveal"))
)
