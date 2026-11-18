from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_basic_energy_card, is_supporter_card, is_tool_card, search_one_of_each

card = SupporterCardDef(
    guid="e13d3738-9e26-5020-810f-a901b29d6c2b",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Castaway.Name",
    display_name="Castaway",
    searchable_by=["Castaway", "Supporter"],
    subtypes=["Supporter"],
    collector_number=72,
    set_code="EX14",
    rarity=Rarities.Uncommon,
    effect=search_one_of_each([is_supporter_card, is_tool_card, is_basic_energy_card])
)
