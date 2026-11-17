from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import behind_on_prizes, opponent_bench_to_active

card = ItemCardDef(
    guid="7977f03c-eb8c-59be-9806-1793358a0f94",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CounterCatcher.Name",
    display_name="Counter Catcher",
    searchable_by=["Counter Catcher", "Item"],
    subtypes=["Item"],
    collector_number=264,
    set_code="SV4",
    rarity=Rarities.Rare,
    effect=opponent_bench_to_active(), condition=behind_on_prizes()
)
