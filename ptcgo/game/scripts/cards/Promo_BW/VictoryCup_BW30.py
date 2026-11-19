from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import if_heads, is_pokemon_card

card = ItemCardDef(
    guid="56e5538f-f57c-5e2e-9d4b-8de6204257ea",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.trainer.VictoryCup.Name",
    display_name="Victory Cup",
    searchable_by=["Victory Cup", "Item"],
    subtypes=["Item"],
    collector_number=30,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    effect=if_heads(search_to_hand(is_pokemon_card, 1,
                                    prompt="Choose a Pokemon to reveal"))
)
