from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_basic_pokemon, search_distinct_types

card = SupporterCardDef(
    guid="4d13404d-e3ba-599c-9796-9bd2c3ac4808",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorOaksSetup.Name",
    display_name="Professor Oak's Setup",
    searchable_by=["Professor Oak's Setup", "Supporter"],
    subtypes=["Supporter"],
    collector_number=201,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    effect=search_distinct_types(is_basic_pokemon, 3, to_bench=True)
)
