from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import return_pokemon_to_hand

card = ItemCardDef(
    guid="46a98064-f2bf-5c1a-bdaa-1f4a7b184474",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperScoopUp.Name",
    display_name="Super Scoop Up",
    searchable_by=["Super Scoop Up", "Item"],
    subtypes=["Item"],
    collector_number=100,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    effect=return_pokemon_to_hand(flip=True)
)
