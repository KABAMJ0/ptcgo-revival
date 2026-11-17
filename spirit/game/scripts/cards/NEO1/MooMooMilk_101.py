from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import flip_heal_chosen

card = ItemCardDef(
    guid="c8e3c6c2-8e83-583f-b734-d1f8d5c117da",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MooMooMilk.Name",
    display_name="Moo-Moo Milk",
    searchable_by=["Moo-Moo Milk"],
    subtypes=[],
    collector_number=101,
    set_code="NEO1",
    rarity=Rarities.Common,
    effect=flip_heal_chosen(2, 2)
)
