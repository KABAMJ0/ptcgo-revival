from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import prevent_bench_damage_through_opponents_turn

card = ItemCardDef(
    guid="d96ee441-d01d-5157-b81e-7f79037771a3",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TransparentWalls.Name",
    display_name="Transparent Walls",
    searchable_by=["Transparent Walls"],
    subtypes=[],
    collector_number=125,
    set_code="GYM2",
    rarity=Rarities.Common,
    effect=prevent_bench_damage_through_opponents_turn()
)
