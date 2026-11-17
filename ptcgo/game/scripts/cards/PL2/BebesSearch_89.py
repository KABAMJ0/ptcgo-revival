from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import hand_to_top_then_search

card = SupporterCardDef(
    guid="16ea151b-4cff-51f9-b1a0-536d6f77478c",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BebesSearch.Name",
    display_name="Bebe's Search",
    searchable_by=["Bebe's Search", "Supporter"],
    subtypes=["Supporter"],
    collector_number=89,
    set_code="PL2",
    rarity=Rarities.Uncommon,
    effect=hand_to_top_then_search()
)
