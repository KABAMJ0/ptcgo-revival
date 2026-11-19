from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers, Activations
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import prize_ahead_tool

card = PokemonToolCardDef(
    guid="569fe763-9226-5205-8e9c-a50b6104208f",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DefianceBand.Name",
    display_name="Defiance Band",
    searchable_by=["Defiance Band", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=169,
    set_code="SV1",
    rarity=Rarities.Uncommon,
    passive=prize_ahead_tool(30, True, True),
)
