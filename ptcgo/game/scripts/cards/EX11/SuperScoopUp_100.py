from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import return_pokemon_to_hand

card = ItemCardDef(
    guid="78146353-4088-5ba3-a5a5-3b82330fc63c",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperScoopUp.Name",
    display_name="Super Scoop Up",
    searchable_by=["Super Scoop Up", "Item"],
    subtypes=["Item"],
    collector_number=100,
    set_code="EX11",
    rarity=Rarities.Uncommon,
    effect=return_pokemon_to_hand(flip=True)
)
