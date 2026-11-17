from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import gated_type, named_rule_box

card = PokemonToolCardDef(
    guid="d246a228-e265-54ee-a7e9-b3bd6884945e",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FightingMemory.Name",
    display_name="Fighting Memory",
    searchable_by=["Fighting Memory", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=94,
    set_code="SM4",
    rarity=Rarities.Uncommon,
    passive=gated_type("fighting", named_rule_box("silvally", "gx"))
)
