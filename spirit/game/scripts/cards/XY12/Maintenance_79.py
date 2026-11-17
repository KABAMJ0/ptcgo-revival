from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import shuffle_hand_n_draw

card = ItemCardDef(
    guid="4c25e3f7-ae72-5032-826e-19ab2b473fb3",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Maintenance.Name",
    display_name="Maintenance",
    searchable_by=["Maintenance", "Item"],
    subtypes=["Item"],
    collector_number=79,
    set_code="XY12",
    rarity=Rarities.Uncommon,
    effect=shuffle_hand_n_draw(2, draw=1)
)
