from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import opponent_bench_to_active

card = SupporterCardDef(
    guid="a1dcc4ec-3463-5c03-a295-68f0dada2c25",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lysandre.Name",
    display_name="Lysandre",
    searchable_by=["Lysandre", "Supporter"],
    subtypes=["Supporter"],
    collector_number=78,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    effect=opponent_bench_to_active()
)
