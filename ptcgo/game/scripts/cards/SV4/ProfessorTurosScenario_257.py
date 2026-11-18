from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import return_pokemon_to_hand

card = SupporterCardDef(
    guid="5aba40ac-f97f-591b-a9b7-7425a4d5ad63",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorTurosScenario.Name",
    display_name="Professor Turo's Scenario",
    searchable_by=["Professor Turo's Scenario", "Supporter", "Future"],
    subtypes=["Supporter", "Future"],
    collector_number=257,
    set_code="SV4",
    rarity=Rarities.Rare,
    effect=return_pokemon_to_hand(with_attachments="discard")
)
