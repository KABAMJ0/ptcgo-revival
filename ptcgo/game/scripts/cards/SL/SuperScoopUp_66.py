from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import return_pokemon_to_hand

card = ItemCardDef(
    guid="46ef9ba8-5b5e-5c99-b96e-db9179f3887a",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperScoopUp.Name",
    display_name="Super Scoop Up",
    searchable_by=["Super Scoop Up", "Item"],
    subtypes=["Item"],
    collector_number=66,
    set_code="SL",
    rarity=Rarities.Uncommon,
    effect=return_pokemon_to_hand(flip=True)
)
