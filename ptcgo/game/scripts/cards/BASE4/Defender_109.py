from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import (
    holder_takes_less, tool_discard_after_opponents_turn,
)

card = PokemonToolCardDef(
    guid="aeeaca71-e23c-593c-8c10-31b59816f315",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Defender.Name",
    display_name="Defender",
    searchable_by=["Defender", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=109,
    set_code="BASE4",
    rarity=Rarities.Uncommon,
    passive=holder_takes_less(20),
    granted_abilities=[tool_discard_after_opponents_turn("Defender")]
)
