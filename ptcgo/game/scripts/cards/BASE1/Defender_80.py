from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import (
    holder_takes_less, tool_discard_after_opponents_turn,
)

card = PokemonToolCardDef(
    guid="4fb149ab-c3e1-5859-9cc9-62e89c0bafd3",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Defender.Name",
    display_name="Defender",
    searchable_by=["Defender", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=80,
    set_code="BASE1",
    rarity=Rarities.Uncommon,
    passive=holder_takes_less(20),
    granted_abilities=[tool_discard_after_opponents_turn("Defender")]
)
