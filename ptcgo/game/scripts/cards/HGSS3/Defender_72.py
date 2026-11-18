from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import (
    holder_takes_less, tool_discard_after_opponents_turn,
)

card = PokemonToolCardDef(
    guid="a286be9a-1393-5e9f-be55-82447c2d3133",
    key="HGSS3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Defender.Name",
    display_name="Defender",
    searchable_by=["Defender", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=72,
    set_code="HGSS3",
    rarity=Rarities.Uncommon,
    passive=holder_takes_less(20),
    granted_abilities=[tool_discard_after_opponents_turn("Defender")]
)
