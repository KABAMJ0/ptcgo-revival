from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import return_pokemon_to_hand

card = ItemCardDef(
    guid="38b6a143-0c08-5332-9763-2699e6c81e27",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperScoopUp.Name",
    display_name="Super Scoop Up",
    searchable_by=["Super Scoop Up", "Item"],
    subtypes=["Item"],
    collector_number=166,
    set_code="SM3",
    rarity=Rarities.RareSecret,
    effect=return_pokemon_to_hand(flip=True)
)
