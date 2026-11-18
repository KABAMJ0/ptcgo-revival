from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers, Activations
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import exp_all_energy_handoff

card = PokemonToolCardDef(
    guid="89b46eb3-469d-54ba-9b84-154d808a71c6",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EXPALL.Name",
    display_name="EXP.ALL",
    searchable_by=["EXP.ALL", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=91,
    set_code="EX6",
    rarity=Rarities.Uncommon,
    granted_abilities=exp_all_energy_handoff('EXP.ALL'),
)
