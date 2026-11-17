from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import return_pokemon_to_hand

card = ItemCardDef(
    guid="46ef9ba8-5b5e-5c99-b96e-db9179f3887a",
    key="SM35",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperScoopUp.Name",
    display_name="Super Scoop Up",
    searchable_by=["Super Scoop Up", "Item"],
    subtypes=["Item"],
    collector_number=66,
    set_code="SM35",
    rarity=Rarities.Uncommon,
    effect=return_pokemon_to_hand(flip=True)
)
