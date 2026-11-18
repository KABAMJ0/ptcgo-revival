from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import has_energy_of, heal_where

card = SupporterCardDef(
    guid="26e358be-9513-5754-b607-ed8ce789deaf",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lana.Name",
    display_name="Lana",
    searchable_by=["Lana", "Supporter"],
    subtypes=["Supporter"],
    collector_number=150,
    set_code="SM5",
    rarity=Rarities.RareUltra,
    effect=heal_where(50, "each_own", has_energy_of("water"))
)
