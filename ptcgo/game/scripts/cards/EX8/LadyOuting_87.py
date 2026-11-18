from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_basic_energy_card, search_distinct_types

card = SupporterCardDef(
    guid="36d1a2b0-3ffe-5c76-8c00-213f72554996",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LadyOuting.Name",
    display_name="Lady Outing",
    searchable_by=["Lady Outing", "Supporter"],
    subtypes=["Supporter"],
    collector_number=87,
    set_code="EX8",
    rarity=Rarities.Uncommon,
    effect=search_distinct_types(is_basic_energy_card, 3)
)
