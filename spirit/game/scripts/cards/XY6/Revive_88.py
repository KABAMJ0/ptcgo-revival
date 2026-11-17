from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import recover_basic_to_bench

card = ItemCardDef(
    guid="542cc576-c475-517e-bd7c-204db9742644",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Revive.Name",
    display_name="Revive",
    searchable_by=["Revive", "Item"],
    subtypes=["Item"],
    collector_number=88,
    set_code="XY6",
    rarity=Rarities.Uncommon,
    effect=recover_basic_to_bench(1)
)
