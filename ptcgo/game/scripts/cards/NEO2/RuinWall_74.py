from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_bench
from ptcgo.game.card_effects.trainers import card_named_contains

card = ItemCardDef(
    guid="a0881ca1-94ef-5432-a287-d0ba20123a69",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RuinWall.Name",
    display_name="Ruin Wall",
    searchable_by=["Ruin Wall"],
    subtypes=[],
    collector_number=74,
    set_code="NEO2",
    rarity=Rarities.Uncommon,
    effect=search_to_bench(card_named_contains('unown'), 1)
)
