from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_pokemon_card, look_bottom_to_hand

card = ItemCardDef(
    guid="43f0187a-fe1f-5ec4-ac49-dbf856ec752a",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DuskBall.Name",
    display_name="Dusk Ball",
    searchable_by=["Dusk Ball", "Item"],
    subtypes=["Item"],
    collector_number=80,
    set_code="DP5",
    rarity=Rarities.Uncommon,
    effect=look_bottom_to_hand(7, 1, is_pokemon_card)
)
