from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers, Activations
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import end_of_turn_while_active_tool

card = PokemonToolCardDef(
    guid="2e4c254c-2ba6-5da3-b384-20f321a87b9a",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Leftovers.Name",
    display_name="Leftovers",
    searchable_by=["Leftovers", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=163,
    set_code="SV3PT5",
    rarity=Rarities.Uncommon,
    granted_abilities=end_of_turn_while_active_tool('Leftovers', 0, 20),
)
