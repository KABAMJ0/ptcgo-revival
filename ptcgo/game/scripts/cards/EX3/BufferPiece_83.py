from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import (
    holder_takes_less, tool_discard_after_opponents_turn,
)

card = PokemonToolCardDef(
    guid="5ffa0469-3da3-5699-8e4a-1e3091973dfa",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BufferPiece.Name",
    display_name="Buffer Piece",
    searchable_by=["Buffer Piece", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=83,
    set_code="EX3",
    rarity=Rarities.Uncommon,
    passive=holder_takes_less(20),
    granted_abilities=[tool_discard_after_opponents_turn("Buffer Piece")]
)
