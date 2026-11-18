from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_pokemon_card, opponent_hand_card_to_bottom

card = ItemCardDef(
    guid="73389d31-b4e7-588f-b546-34c0860bc136",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Grabber.Name",
    display_name="Grabber",
    searchable_by=["Grabber", "Item"],
    subtypes=["Item"],
    collector_number=162,
    set_code="SV3PT5",
    rarity=Rarities.Uncommon,
    effect=opponent_hand_card_to_bottom(is_pokemon_card)
)
