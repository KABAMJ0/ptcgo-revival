from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import return_pokemon_to_hand

card = ItemCardDef(
    guid="48433d75-29c2-57e7-b2dd-028d8e9c8731",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperScoopUp.Name",
    display_name="Super Scoop Up",
    searchable_by=["Super Scoop Up", "Item"],
    subtypes=["Item"],
    collector_number=87,
    set_code="DP5",
    rarity=Rarities.Uncommon,
    effect=return_pokemon_to_hand(flip=True)
)
