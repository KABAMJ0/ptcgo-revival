from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import recover_basic_to_bench, with_discard_typed_cost

card = ItemCardDef(
    guid="6c06b163-7499-5f94-a0ca-80499d4f493b",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MaxRevive.Name",
    display_name="Max Revive",
    searchable_by=["Max Revive"],
    subtypes=[],
    collector_number=117,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    effect=with_discard_typed_cost(2, recover_basic_to_bench(1))
)
