from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import return_pokemon_to_hand

card = SupporterCardDef(
    guid="5888b7ab-7b43-53b1-9a10-afc9989196af",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorTurosScenario.Name",
    display_name="Professor Turo's Scenario",
    searchable_by=["Professor Turo's Scenario", "Supporter", "Future"],
    subtypes=["Supporter", "Future"],
    collector_number=171,
    set_code="SV4",
    rarity=Rarities.Uncommon,
    effect=return_pokemon_to_hand(with_attachments="discard")
)
