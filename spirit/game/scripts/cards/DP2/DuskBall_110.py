from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import is_pokemon_card, look_bottom_to_hand

card = ItemCardDef(
    guid="29d30129-414d-55d1-90f4-f77f7db81c8f",
    key="DP2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DuskBall.Name",
    display_name="Dusk Ball",
    searchable_by=["Dusk Ball", "Item"],
    subtypes=["Item"],
    collector_number=110,
    set_code="DP2",
    rarity=Rarities.Uncommon,
    effect=look_bottom_to_hand(7, 1, is_pokemon_card)
)
