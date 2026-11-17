from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import shuffle_hand_n_draw

card = ItemCardDef(
    guid="942a3d6a-72f6-59df-a688-fa28456460b2",
    key="G1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Maintenance.Name",
    display_name="Maintenance",
    searchable_by=["Maintenance", "Item"],
    subtypes=["Item"],
    collector_number=64,
    set_code="G1",
    rarity=Rarities.Uncommon,
    effect=shuffle_hand_n_draw(2, draw=1)
)
