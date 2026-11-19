from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import (
    holder_no_weakness, tool_discard_after_opponents_turn,
)

card = PokemonToolCardDef(
    guid="49aba60a-3e19-5b0a-9239-3e9cf12ee117",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WeaknessGuard.Name",
    display_name="Weakness Guard",
    searchable_by=["Weakness Guard", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=141,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    passive=holder_no_weakness(),
    granted_abilities=[tool_discard_after_opponents_turn("Weakness Guard")]
)
