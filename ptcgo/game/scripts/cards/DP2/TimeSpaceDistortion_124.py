from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import flip_recover_per_heads, is_pokemon_card

card = ItemCardDef(
    guid="9de91e32-e439-5bdf-b3b4-ff547d4ddbef",
    key="DP2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TimeSpaceDistortion.Name",
    display_name="Time-Space Distortion",
    searchable_by=["Time-Space Distortion", "Item"],
    subtypes=["Item"],
    collector_number=124,
    set_code="DP2",
    rarity=Rarities.RareSecret,
    effect=flip_recover_per_heads(3, is_pokemon_card)
)
