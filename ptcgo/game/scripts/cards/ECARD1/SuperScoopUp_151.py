from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import return_pokemon_to_hand

card = ItemCardDef(
    guid="bcae4fe8-399d-52d0-913f-94576ffb37c0",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperScoopUp.Name",
    display_name="Super Scoop Up",
    searchable_by=["Super Scoop Up"],
    subtypes=[],
    collector_number=151,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    effect=return_pokemon_to_hand(flip=True)
)
