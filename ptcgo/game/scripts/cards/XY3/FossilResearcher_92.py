from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import card_named_any
from ptcgo.game.card_effects.support_common import search_to_bench

card = SupporterCardDef(
    guid="2be42883-d054-599b-a803-32ff6d6faba9",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FossilResearcher.Name",
    display_name="Fossil Researcher",
    searchable_by=["Fossil Researcher", "Supporter"],
    subtypes=["Supporter"],
    collector_number=92,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    effect=search_to_bench(card_named_any(("amaura", "tyrunt")), 2)
)
