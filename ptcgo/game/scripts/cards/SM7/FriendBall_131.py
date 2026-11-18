from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import search_same_type_as_opponent

card = ItemCardDef(
    guid="37bc31bf-b9da-5c15-b5bf-f8e0d25aead8",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FriendBall.Name",
    display_name="Friend Ball",
    searchable_by=["Friend Ball", "Item"],
    subtypes=["Item"],
    collector_number=131,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    effect=search_same_type_as_opponent(1)
)
