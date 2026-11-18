from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import all_of, card_named_contains, is_basic_energy_card, is_supporter_card, is_trainer_card, search_one_of_each

card = SupporterCardDef(
    guid="b34b0b77-fa1f-54bc-9209-1ab6011d73f2",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CyrussConspiracy.Name",
    display_name="Cyrus's Conspiracy",
    searchable_by=["Cyrus's Conspiracy", "Supporter"],
    subtypes=["Supporter"],
    collector_number=105,
    set_code="PL1",
    rarity=Rarities.Uncommon,
    effect=search_one_of_each([is_supporter_card, is_basic_energy_card, all_of(is_trainer_card, card_named_contains("team galactics invention"))])
)
