from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import search_basic_cards_either_zone

card = SupporterCardDef(
    guid="3ae7468f-1fa1-5ff7-8522-b7e5ba2477b8",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MrStonesProject.Name",
    display_name="Mr. Stone's Project",
    searchable_by=["Mr. Stone's Project", "Supporter"],
    subtypes=["Supporter"],
    collector_number=79,
    set_code="EX9",
    rarity=Rarities.Uncommon,
    effect=search_basic_cards_either_zone(2)
)
