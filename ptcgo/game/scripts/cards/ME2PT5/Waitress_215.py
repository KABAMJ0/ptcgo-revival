from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import search_top_energy_attach

card = SupporterCardDef(
    guid="0730eece-5e4c-5ffa-a146-bd70b579fb2b",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Waitress.Name",
    display_name="Waitress",
    searchable_by=["Waitress", "Supporter"],
    subtypes=["Supporter"],
    collector_number=215,
    set_code="ME2PT5",
    rarity=Rarities.Common,
    effect=search_top_energy_attach(6)
)
