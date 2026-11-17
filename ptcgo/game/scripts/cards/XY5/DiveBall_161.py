from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import pokemon_of

card = ItemCardDef(
    guid="6adcfc8e-7875-5de9-b36d-8f7b2ea10fb6",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DiveBall.Name",
    display_name="Dive Ball",
    searchable_by=["Dive Ball", "Item"],
    subtypes=["Item"],
    collector_number=161,
    set_code="XY5",
    rarity=Rarities.RareSecret,
    effect=search_to_hand(pokemon_of("water"), count=1)
)
