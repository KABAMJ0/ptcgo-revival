from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import each_player_return_bench_one

card = SupporterCardDef(
    guid="68a2abbd-7505-59cf-a68d-5fd5d401d6a1",
    key="HGSS4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Seeker.Name",
    display_name="Seeker",
    searchable_by=["Seeker", "Supporter"],
    subtypes=["Supporter"],
    collector_number=88,
    set_code="HGSS4",
    rarity=Rarities.Uncommon,
    effect=each_player_return_bench_one()
)
