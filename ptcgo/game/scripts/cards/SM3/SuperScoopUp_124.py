from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import return_pokemon_to_hand

card = ItemCardDef(
    guid="d9469aa4-6859-537a-9dae-50ca13a6f394",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperScoopUp.Name",
    display_name="Super Scoop Up",
    searchable_by=["Super Scoop Up", "Item"],
    subtypes=["Item"],
    collector_number=124,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    effect=return_pokemon_to_hand(flip=True)
)
