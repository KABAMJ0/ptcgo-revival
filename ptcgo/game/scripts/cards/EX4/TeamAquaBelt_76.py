from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers, Activations
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import evolve_holder_between_turns, team_aqua_target

card = PokemonToolCardDef(
    guid="cd2fc041-274c-5f40-bbbb-df945207e758",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamAquaBelt.Name",
    display_name="Team Aqua Belt",
    searchable_by=["Team Aqua Belt", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=76,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    granted_abilities=evolve_holder_between_turns('Team Aqua Belt', 'active', 0),
    attach_to=team_aqua_target,
)
