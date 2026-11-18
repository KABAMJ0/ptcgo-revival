from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import reveal_until_pokemon_to_hand

card = ItemCardDef(
    guid="5f810ad0-d313-5637-9e24-dce7b700c9fd",
    key="DP2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.QuickBall.Name",
    display_name="Quick Ball",
    searchable_by=["Quick Ball", "Item"],
    subtypes=["Item"],
    collector_number=114,
    set_code="DP2",
    rarity=Rarities.Uncommon,
    effect=reveal_until_pokemon_to_hand()
)
