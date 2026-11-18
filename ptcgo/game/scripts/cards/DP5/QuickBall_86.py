from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import reveal_until_pokemon_to_hand

card = ItemCardDef(
    guid="f90c74cc-600a-5197-a31e-bb06f32abf7f",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.QuickBall.Name",
    display_name="Quick Ball",
    searchable_by=["Quick Ball", "Item"],
    subtypes=["Item"],
    collector_number=86,
    set_code="DP5",
    rarity=Rarities.Uncommon,
    effect=reveal_until_pokemon_to_hand()
)
