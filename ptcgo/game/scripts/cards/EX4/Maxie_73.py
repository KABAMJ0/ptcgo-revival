from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import bench_named_pokemon, team_magma_target

card = SupporterCardDef(
    guid="3006348b-81f8-5dab-9f15-6d35351216d8",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Maxie.Name",
    display_name="Maxie",
    searchable_by=["Maxie", "Supporter"],
    subtypes=["Supporter"],
    collector_number=73,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    effect=bench_named_pokemon(team_magma_target, "hand_or_discard", "Team Magma Pokemon")
)
