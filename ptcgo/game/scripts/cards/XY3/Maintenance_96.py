from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import shuffle_hand_n_draw

card = ItemCardDef(
    guid="9ea50b4a-94e5-5594-bd1d-f5bf360a35c6",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Maintenance.Name",
    display_name="Maintenance",
    searchable_by=["Maintenance", "Item"],
    subtypes=["Item"],
    collector_number=96,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    effect=shuffle_hand_n_draw(2, draw=1)
)
