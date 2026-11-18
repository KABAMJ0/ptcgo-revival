from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers, Activations
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import prize_ahead_tool

card = PokemonToolCardDef(
    guid="e63f2388-03a8-589b-9934-82b875982113",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DefianceVest.Name",
    display_name="Defiance Vest",
    searchable_by=["Defiance Vest", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=162,
    set_code="SV4",
    rarity=Rarities.Uncommon,
    passive=prize_ahead_tool(40, False, False),
)
