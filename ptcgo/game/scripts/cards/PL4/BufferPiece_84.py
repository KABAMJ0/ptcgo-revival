from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import (
    holder_takes_less, tool_discard_after_opponents_turn,
)

card = PokemonToolCardDef(
    guid="ef4e8b2c-c025-5638-8c81-a6f129b46541",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BufferPiece.Name",
    display_name="Buffer Piece",
    searchable_by=["Buffer Piece", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=84,
    set_code="PL4",
    rarity=Rarities.Uncommon,
    passive=holder_takes_less(20),
    granted_abilities=[tool_discard_after_opponents_turn("Buffer Piece")]
)
