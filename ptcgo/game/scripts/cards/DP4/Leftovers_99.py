from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers, Activations
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import end_of_turn_while_active_tool

card = PokemonToolCardDef(
    guid="94540bcd-b129-552a-8c67-7f0f0116b303",
    key="DP4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Leftovers.Name",
    display_name="Leftovers",
    searchable_by=["Leftovers", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=99,
    set_code="DP4",
    rarity=Rarities.Uncommon,
    granted_abilities=end_of_turn_while_active_tool('Leftovers', 0, 10),
)
