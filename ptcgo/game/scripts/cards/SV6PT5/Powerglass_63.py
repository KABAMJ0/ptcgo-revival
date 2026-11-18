from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers, Activations
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import powerglass_end_of_turn

card = PokemonToolCardDef(
    guid="9b13e2b2-c8fb-5e6a-90f6-0416af522c16",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Powerglass.Name",
    display_name="Powerglass",
    searchable_by=["Powerglass", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=63,
    set_code="SV6PT5",
    rarity=Rarities.Uncommon,
    granted_abilities=powerglass_end_of_turn('Powerglass'),
)
