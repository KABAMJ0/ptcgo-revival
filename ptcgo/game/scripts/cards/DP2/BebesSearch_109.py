from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import hand_to_top_then_search

card = SupporterCardDef(
    guid="5a655dd5-62bd-53fc-8770-fda73350f5c2",
    key="DP2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BebesSearch.Name",
    display_name="Bebe's Search",
    searchable_by=["Bebe's Search", "Supporter"],
    subtypes=["Supporter"],
    collector_number=109,
    set_code="DP2",
    rarity=Rarities.Uncommon,
    effect=hand_to_top_then_search()
)
