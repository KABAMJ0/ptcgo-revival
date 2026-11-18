from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers, Activations
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import evolve_holder_between_turns, team_magma_target

card = PokemonToolCardDef(
    guid="d7e857d0-9148-532f-8e60-72576f99906e",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamMagmaBelt.Name",
    display_name="Team Magma Belt",
    searchable_by=["Team Magma Belt", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=81,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    granted_abilities=evolve_holder_between_turns('Team Magma Belt', 'active', 0),
    attach_to=team_magma_target,
)
