from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import bench_named_pokemon, team_aqua_target

card = SupporterCardDef(
    guid="80e76ab7-4498-54c6-b2e6-6722fa6875e3",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Archie.Name",
    display_name="Archie",
    searchable_by=["Archie", "Supporter"],
    subtypes=["Supporter"],
    collector_number=71,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    effect=bench_named_pokemon(team_aqua_target, "deck", "Team Aqua Pokemon")
)
