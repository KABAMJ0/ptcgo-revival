from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_basic_pokemon, search_distinct_types

card = SupporterCardDef(
    guid="aafdd31e-3a3b-58fa-a406-3eb3bd99f3ab",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorOaksSetup.Name",
    display_name="Professor Oak's Setup",
    searchable_by=["Professor Oak's Setup", "Supporter"],
    subtypes=["Supporter"],
    collector_number=233,
    set_code="SM12",
    rarity=Rarities.RareUltra,
    effect=search_distinct_types(is_basic_pokemon, 3, to_bench=True)
)
