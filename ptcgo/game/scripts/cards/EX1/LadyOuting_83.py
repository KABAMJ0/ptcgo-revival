from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_basic_energy_card, search_distinct_types

card = SupporterCardDef(
    guid="ac7f1d27-12a0-5915-9d35-381764d4a119",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LadyOuting.Name",
    display_name="Lady Outing",
    searchable_by=["Lady Outing", "Supporter"],
    subtypes=["Supporter"],
    collector_number=83,
    set_code="EX1",
    rarity=Rarities.Uncommon,
    effect=search_distinct_types(is_basic_energy_card, 3)
)
