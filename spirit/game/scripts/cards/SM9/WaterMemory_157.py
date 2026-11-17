from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import gated_type, named_rule_box

card = PokemonToolCardDef(
    guid="bb508993-d0c7-55a3-9634-bbcb2834f7b1",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WaterMemory.Name",
    display_name="Water Memory",
    searchable_by=["Water Memory", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=157,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    passive=gated_type("water", named_rule_box("silvally", "gx"))
)
