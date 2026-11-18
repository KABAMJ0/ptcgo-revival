from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import card_named_any
from ptcgo.game.card_effects.support_common import search_to_bench

card = SupporterCardDef(
    guid="c51e44de-fa49-56c8-a267-cad4ceeb693a",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FossilResearcher.Name",
    display_name="Fossil Researcher",
    searchable_by=["Fossil Researcher", "Supporter"],
    subtypes=["Supporter"],
    collector_number=110,
    set_code="XY3",
    rarity=Rarities.RareUltra,
    effect=search_to_bench(card_named_any(("amaura", "tyrunt")), 2)
)
