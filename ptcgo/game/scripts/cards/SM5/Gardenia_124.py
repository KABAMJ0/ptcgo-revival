from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import has_energy_of, heal_where

card = SupporterCardDef(
    guid="54942e2f-c703-50ee-b634-7b23d5a46a45",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Gardenia.Name",
    display_name="Gardenia",
    searchable_by=["Gardenia", "Supporter"],
    subtypes=["Supporter"],
    collector_number=124,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    effect=heal_where(80, "choice", has_energy_of("grass"))
)
