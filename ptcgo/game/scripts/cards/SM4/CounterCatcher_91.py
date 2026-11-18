from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import behind_on_prizes, opponent_bench_to_active

card = ItemCardDef(
    guid="ddc7dd43-0e60-5821-bf9d-f0f65e848a70",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CounterCatcher.Name",
    display_name="Counter Catcher",
    searchable_by=["Counter Catcher", "Item"],
    subtypes=["Item"],
    collector_number=91,
    set_code="SM4",
    rarity=Rarities.Uncommon,
    effect=opponent_bench_to_active(), condition=behind_on_prizes()
)
