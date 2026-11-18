from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import shuffle_hand_flip_draw

card = ItemCardDef(
    guid="f7849688-e0a5-50cb-bbaf-58f734588de4",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Gambler.Name",
    display_name="Gambler",
    searchable_by=["Gambler"],
    subtypes=[],
    collector_number=60,
    set_code="BASE3",
    rarity=Rarities.Common,
    effect=shuffle_hand_flip_draw(8, 1)
)
