from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import return_pokemon_to_hand

card = SupporterCardDef(
    guid="63320e6d-1d34-51a4-921d-302c1dd48065",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorTurosScenario.Name",
    display_name="Professor Turo's Scenario",
    searchable_by=["Professor Turo's Scenario", "Supporter", "Future"],
    subtypes=["Supporter", "Future"],
    collector_number=240,
    set_code="SV4",
    rarity=Rarities.Rare,
    effect=return_pokemon_to_hand(with_attachments="discard")
)
