from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import has_energy_of, heal_where

card = SupporterCardDef(
    guid="d8030c3d-d696-5ca4-ad82-9480ea2213c8",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Gardenia.Name",
    display_name="Gardenia",
    searchable_by=["Gardenia", "Supporter"],
    subtypes=["Supporter"],
    collector_number=149,
    set_code="SM5",
    rarity=Rarities.RareUltra,
    effect=heal_where(80, "choice", has_energy_of("grass"))
)
