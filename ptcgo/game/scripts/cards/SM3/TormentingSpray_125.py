from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_supporter_card, random_opponent_card_discard_if

card = ItemCardDef(
    guid="6957d25d-fda7-5fb4-8096-e34502d64d7d",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TormentingSpray.Name",
    display_name="Tormenting Spray",
    searchable_by=["Tormenting Spray", "Item"],
    subtypes=["Item"],
    collector_number=125,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    effect=random_opponent_card_discard_if(is_supporter_card)
)
