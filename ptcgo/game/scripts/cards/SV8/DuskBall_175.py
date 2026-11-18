from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_pokemon_card, look_bottom_to_hand

card = ItemCardDef(
    guid="a7ade2a0-bf73-5738-a9d9-91e516caa63c",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DuskBall.Name",
    display_name="Dusk Ball",
    searchable_by=["Dusk Ball", "Item"],
    subtypes=["Item"],
    collector_number=175,
    set_code="SV8",
    rarity=Rarities.Uncommon,
    effect=look_bottom_to_hand(7, 1, is_pokemon_card)
)
