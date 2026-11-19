from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import heal_where

card = SupporterCardDef(
    guid="8a5e021e-5419-5ccd-a135-511b86cc1597",
    key="SWSH11TG",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Cook.Name",
    display_name="Cook",
    searchable_by=["Cook", "Supporter"],
    subtypes=["Supporter"],
    collector_number=25,
    set_code="SWSH11TG",
    rarity=Rarities.RareUltra,
    effect=heal_where(70, "active", None, min_energy=0)
)
