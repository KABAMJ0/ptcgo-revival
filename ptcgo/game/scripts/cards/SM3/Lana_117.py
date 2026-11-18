from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import has_energy_of, heal_where

card = SupporterCardDef(
    guid="08d08d68-ebe6-54a0-b651-9978fd2adb7d",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lana.Name",
    display_name="Lana",
    searchable_by=["Lana", "Supporter"],
    subtypes=["Supporter"],
    collector_number=117,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    effect=heal_where(50, "each_own", has_energy_of("water"))
)
