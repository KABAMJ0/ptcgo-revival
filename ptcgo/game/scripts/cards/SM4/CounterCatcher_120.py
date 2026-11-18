from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import behind_on_prizes, opponent_bench_to_active

card = ItemCardDef(
    guid="8f9c9ca5-b3b6-5388-a3c6-651ee30c3d0b",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CounterCatcher.Name",
    display_name="Counter Catcher",
    searchable_by=["Counter Catcher", "Item"],
    subtypes=["Item"],
    collector_number=120,
    set_code="SM4",
    rarity=Rarities.RareSecret,
    effect=opponent_bench_to_active(), condition=behind_on_prizes()
)
