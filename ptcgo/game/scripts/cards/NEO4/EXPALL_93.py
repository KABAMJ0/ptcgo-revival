from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers, Activations
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import exp_all_energy_handoff

card = PokemonToolCardDef(
    guid="d9d5a4d1-738d-5b47-81de-9e3e2e52e3bc",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EXPALL.Name",
    display_name="EXP.ALL",
    searchable_by=["EXP.ALL", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=93,
    set_code="NEO4",
    rarity=Rarities.Rare,
    granted_abilities=exp_all_energy_handoff('EXP.ALL'),
)
