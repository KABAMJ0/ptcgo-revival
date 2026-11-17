from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import return_pokemon_to_hand

card = ItemCardDef(
    guid="acf0b955-5332-5671-9dc3-7dbe78e81a98",
    key="HGSS2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperScoopUp.Name",
    display_name="Super Scoop Up",
    searchable_by=["Super Scoop Up", "Item"],
    subtypes=["Item"],
    collector_number=83,
    set_code="HGSS2",
    rarity=Rarities.Uncommon,
    effect=return_pokemon_to_hand(flip=True)
)
